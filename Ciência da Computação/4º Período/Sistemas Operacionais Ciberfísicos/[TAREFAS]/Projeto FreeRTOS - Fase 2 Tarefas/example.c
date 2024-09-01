// Lucas Azevedo Dias - Ciência da Computação (4º Período)

#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
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
xSemaphoreHandle motorsSemaphore = NULL; // Semaphore for acessing the drone motors

volatile char orientation; // Row movement sense (left-right)
volatile char direction; // Pitch movement sense (forward-backward)
volatile char sense; // Yaw movement sense (clockwise-counterclockwise)
xSemaphoreHandle orientationSemaphore = NULL; // Semaphore for acessing the orientation (left-right)
xSemaphoreHandle directionSemaphore = NULL; // Semaphore for acessing the direction (forward-backward)
xSemaphoreHandle senseSemaphore = NULL; // Semaphore for acessing the sense (clockwise-counterclockwise)

unsigned int timesRow = 50; // Times per second for controlling row
unsigned int timesPitch = 25; // Times per second for controlling pitch
unsigned int timesYaw = 100; // Times per second for controlling yaw


void droneRowTask(void*);
void dronePitchTask(void*);
void droneYawTask(void*);
void droneMovementControllerTask(void*);

void incrementPowerMotor(int, double);


int main_(void)
{
	// Turning on all motors
	for (int i = 0; i < MOTORS_AMOUNT; i++)
	{
		motors[i] = MOTOR_LOW;
	}

	// Creating the drone motors semaphore
	vSemaphoreCreateBinary(motorsSemaphore);

	// Creating the movement variables semaphores
	vSemaphoreCreateBinary(orientationSemaphore);
	vSemaphoreCreateBinary(directionSemaphore);
	vSemaphoreCreateBinary(senseSemaphore);

	// Initial move set (ROW, PITCH, YAW)
	char initialMovement[3] = { 1, 1, 1 };

	// Task being created
	xTaskCreate(droneRowTask, "Drone row", 1000, NULL, 2, NULL);
	xTaskCreate(dronePitchTask, "Drone pitch", 1000, NULL, 2, NULL);
	xTaskCreate(droneYawTask, "Drone yaw", 1000, NULL, 2, NULL);
	xTaskCreate(droneMovementControllerTask, "Drone movement controller", 1000, initialMovement, 1, NULL);

	// Starts the Task Scheduler
	vTaskStartScheduler();

	// Main loop
	for (;;);

	return 0;
}


// Drone row movement (left-right)
void droneRowTask(void* pvParameters)
{
	double incPower = 1. / timesRow; // Increment for power of each motor

	for (;;)
	{
		// If possible, takes the semaphores and updates the motor
		if (motorsSemaphore != NULL && xSemaphoreTake(motorsSemaphore, 0) == pdTRUE)
		{
			if (orientationSemaphore != NULL && xSemaphoreTake(orientationSemaphore, 0) == pdTRUE)
			{
				if (orientation) // Right
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

				printf("ROW   %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);

				xSemaphoreGive(orientationSemaphore); // Frees the semaphore
			}

			xSemaphoreGive(motorsSemaphore); // Frees the semaphore

			vTaskDelay(portTICK_RATE_MS * 1000 / timesRow); // Delays the next update
		}
	}

	vTaskDelete(NULL);
}


// Drone pitch movement (forward-backward)
void dronePitchTask(void* pvParameters)
{
	double incPower = 1. / timesPitch; // Increment for power of each motor

	for (;;)
	{
		// If possible, takes the semaphores and updates the motor
		if (motorsSemaphore != NULL && xSemaphoreTake(motorsSemaphore, 0) == pdTRUE)
		{
			if (directionSemaphore != NULL && xSemaphoreTake(directionSemaphore, 0) == pdTRUE)
			{
				if (direction) // Forward
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

				printf("PITCH %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);

				xSemaphoreGive(directionSemaphore); // Frees the semaphore
			}

			xSemaphoreGive(motorsSemaphore); // Frees the semaphore

			vTaskDelay(portTICK_RATE_MS * 1000 / timesPitch); // Delays the next update
		}
	}

	vTaskDelete(NULL);
}


// Drone yaw movement (clockwise-counterclockwise)
void droneYawTask(void* pvParameters)
{
	double incPower = 1. / timesYaw; // Increment for power of each motor

	for (;;)
	{
		// If possible, takes the semaphores and updates the motor
		if (motorsSemaphore != NULL && xSemaphoreTake(motorsSemaphore, 0) == pdTRUE)
		{
			if (senseSemaphore != NULL && xSemaphoreTake(senseSemaphore, 0) == pdTRUE)
			{
				if (sense) // Clockwise
				{
					incrementPowerMotor(1, -incPower);
					incrementPowerMotor(3, -incPower);
					incrementPowerMotor(0, incPower);
					incrementPowerMotor(2, incPower);
				}
				else // Counterclockwise
				{
					incrementPowerMotor(1, incPower);
					incrementPowerMotor(3, incPower);
					incrementPowerMotor(0, -incPower);
					incrementPowerMotor(2, -incPower);
				}

				printf("YAW   %lf %lf %lf %lf\n", motors[0], motors[1], motors[2], motors[3]);

				xSemaphoreGive(senseSemaphore); // Frees the semaphore
			}

			xSemaphoreGive(motorsSemaphore); // Frees the semaphore

			vTaskDelay(portTICK_RATE_MS * 1000 / timesYaw); // Delays the next update
		}
	}

	vTaskDelete(NULL);
}


// Drone movement controller (simulates a radio frequency device)
void droneMovementControllerTask(void* pvParameters)
{
	char* initialMovement = pvParameters;

	volatile int randOrientation = initialMovement[0] + 1;
	volatile int randDirection = initialMovement[1] + 1;
	volatile int randSense = initialMovement[2] + 1;

	for (;;)
	{
		// Attributing a value to orientation if possible
		if (orientationSemaphore != NULL && xSemaphoreTake(orientationSemaphore, (portTickType) 10) == pdTRUE)
		{
			if (randOrientation % 2 == 0)
			{
				orientation = 1; // Right
			}
			else
			{
				orientation = 0; // Left
			}

			xSemaphoreGive(orientationSemaphore);
		}

		// Attributing a value to direction if possible
		if (directionSemaphore != NULL && xSemaphoreTake(directionSemaphore, (portTickType) 10) == pdTRUE)
		{
			if (randDirection % 2 == 0)
			{
				direction = 1; // Forward
			}
			else
			{
				direction = 0; // Backward
			}

			xSemaphoreGive(directionSemaphore);
		}

		// Attributing a value to sense if possible
		if (senseSemaphore != NULL && xSemaphoreTake(senseSemaphore, (portTickType) 10) == pdTRUE)
		{
			if (randSense % 2 == 0)
			{
				sense = 1; // Clockwise
			}
			else
			{
				sense = 0; // Counterclockwise
			}

			xSemaphoreGive(senseSemaphore);
		}
		
		// Sorting a value between 0 and 100 for each movement
		randOrientation = rand() % 100;
		randDirection = rand() % 100;
		randSense = rand() % 100;

		vTaskDelay(portTICK_RATE_MS * 100); // Delays into 100ms
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
