// Lucas Azevedo Dias - Ciência da Computação (4º Período)

#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"


#define MOTORS_AMOUNT 4 // Amount of drone motors
#define MOTOR_LOW 0 // Low motor state
#define MOTOR_HIGH 1 // High motor state
/*
Motors states:
	0 - LOW
	0..1 - intermediate state
	1 - HIGH
*/

double motors[MOTORS_AMOUNT]; // Drone motors

unsigned int timesRow = 50; // Times per second for controlling row
unsigned int timesPitch = 25; // Times per second for controlling pitch
unsigned int timesYaw = 100; // Times per second for controlling yaw


void droneRowTask(void*);
void dronePitchTask(void*);
void droneYawTask(void*);

void incrementPowerMotor(int, double);


int main_(void)
{
	// Turning on all motors
	for (int i = 0; i < MOTORS_AMOUNT; i++)
	{
		motors[i] = MOTOR_LOW;
	}

	// Task being created
	xTaskCreate(droneRowTask, "Drone row", 1000, (void*) 1, 1, NULL);
	xTaskCreate(dronePitchTask, "Drone pitch", 1000, (void*) 1, 1, NULL);
	xTaskCreate(droneYawTask, "Drone yaw", 1000, (void*) 1, 1, NULL);

	// Starts the Task Scheduler
	vTaskStartScheduler();

	// Main loop
	for (;;);

	return 0;
}


// Drone row movement
void droneRowTask(void* pvParameters)
{
	char movSense = (char*) pvParameters; // Sense of the movement
	double incPower = 1. / timesRow; // Increment for power of each motor

	volatile int counter = 0; // Counter of times updated

	for (;;)
	{
		if (movSense) // Right
		{
			incrementPowerMotor(0, incPower);
			incrementPowerMotor(3, incPower);
			incrementPowerMotor(1, -incPower);
			incrementPowerMotor(2, -incPower);
		}
		else // Left
		{
			incrementPowerMotor(0, -incPower);
			incrementPowerMotor(3, -incPower);
			incrementPowerMotor(1, incPower);
			incrementPowerMotor(2, incPower);
		}

		// Verifies if it has updated all times
		if (counter < timesRow) // Delays the next update
		{
			counter++;
			printf("ROW   %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);
			vTaskDelay(1000 / timesRow);
		}
		else // Deletes itself
		{
			break;
		}
	}

	vTaskDelete(NULL);
}


// Drone pitch movement
void dronePitchTask(void* pvParameters)
{
	char movSense = (char*) pvParameters; // Sense of the movement
	double incPower = 1. / timesPitch; // Increment for power of each motor

	volatile int counter = 0; // Counter of times updated

	for (;;)
	{
		if (movSense) // Forward
		{
			incrementPowerMotor(2, incPower);
			incrementPowerMotor(3, incPower);
			incrementPowerMotor(0, -incPower);
			incrementPowerMotor(1, -incPower);
		}
		else // Backward
		{
			incrementPowerMotor(2, -incPower);
			incrementPowerMotor(3, -incPower);
			incrementPowerMotor(0, incPower);
			incrementPowerMotor(1, incPower);
		}

		// Verifies if it has updated all times
		if (counter < timesPitch) // Delays the next update
		{
			counter++;
			printf("PITCH %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);
			vTaskDelay(1000 / timesPitch);
		}
		else // Deletes itself
		{
			break;
		}
	}

	vTaskDelete(NULL);
}


// Drone yaw movement
void droneYawTask(void* pvParameters)
{
	char movSense = (char*) pvParameters; // Sense of the movement
	double incPower = 1. / timesYaw; // Increment for power of each motor

	volatile int counter = 0; // Counter of times updated

	for (;;)
	{
		if (movSense) // Counterclockwise
		{
			incrementPowerMotor(1, incPower);
			incrementPowerMotor(3, incPower);
			incrementPowerMotor(0, -incPower);
			incrementPowerMotor(2, -incPower);
		}
		else // Clockwise
		{
			incrementPowerMotor(1, -incPower);
			incrementPowerMotor(3, -incPower);
			incrementPowerMotor(0, incPower);
			incrementPowerMotor(2, incPower);
		}

		// Verifies if it has updated all times
		if (counter < timesYaw) // Delays the next update
		{
			counter++;
			printf("YAW   %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);
			vTaskDelay(1000 / timesYaw);
		}
		else // Deletes itself
		{
			break;
		}
	}

	vTaskDelete(NULL);
}


// Increments the power of the motor given
void incrementPowerMotor(int index, double incPower)
{
	if (motors[index] + incPower > MOTOR_HIGH)
	{
		motors[index] = MOTOR_HIGH;
	}
	else if (motors[index] + incPower < MOTOR_LOW)
	{
		motors[index] = MOTOR_LOW;
	}
	else
	{
		motors[index] += incPower;
	}
}
