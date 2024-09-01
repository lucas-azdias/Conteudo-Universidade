// Lucas Azevedo Dias - Ciência da Computação (4º Período)

#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"


typedef struct { // Struct of the data to initialize a monitorDeviceSimulatorTask
	char* msg; // Message to show data
	char* unit; // Unit for the data generated
	double min; // Minimum value for the data generated
	double max; // Maximum value for the data generated
	char* msg_low; // Message if it gets lower than "low"
	double low; // Reference value for the "low" status
	char* msg_high; // Message if it gets higher than "high"
	double high; // Reference value for the "high" status
} MonitorInfo;


void monitorDeviceSimulatorTask(void* pvParameters);
double linearInterpolation(double, double, double, double, double);


// MAIN
int main_(void)
{
	// Info for each task
	MonitorInfo beatsInfo = {
		"Batimentos:",
		"bpm",
		20,
		140,
		"Batimentos cardíacos baixos\n",
		50,
		"Batimentos cardíacos altos\n",
		90
	};
	MonitorInfo oxygenInfo = {
		"Saturação:",
		"%",
		80,
		100,
		"Saturação de oxigênio do sangue baixa\n",
		90,
		"INVÁLIDO\n",
		101
	};
	MonitorInfo temperatureInfo = {
		"Temperatura:",
		"°",
		34,
		41,
		"Hipotermia detectada\n",
		35,
		"Febre detectada\n",
		37.5
	};

	// Task being created
	xTaskCreate(monitorDeviceSimulatorTask, "Beats monitoring program", 1000, &beatsInfo, 1, NULL);
	xTaskCreate(monitorDeviceSimulatorTask, "Oxygen monitoring program", 1000, &oxygenInfo, 1, NULL);
	xTaskCreate(monitorDeviceSimulatorTask, "Temperature monitoring program", 1000, &temperatureInfo, 1, NULL);

	// Starts the Task Scheduler
	vTaskStartScheduler();
	
	// Main loop
	for (;;);

	return 0;
}


// Task function for the monitor device simulator
void monitorDeviceSimulatorTask(void* pvParameters)
{
	MonitorInfo* monitorInfo = pvParameters; // Data of the simulator
	double dataGenerated; // Variable for the data randomly generated

	srand(time(NULL)); // Setting the seed for randoms

	for (;;) // Task inifite loop
	{
		dataGenerated = linearInterpolation(rand(), 0, RAND_MAX, monitorInfo->min, monitorInfo->max); // Generating a random number in the range of 0 to 1

		vPrintStringAndNumber(monitorInfo->msg, dataGenerated); // Displays the message and the data

		// Message when the data enters "low" status
		if (dataGenerated < monitorInfo->low)
		{
			vPrintString(monitorInfo->msg_low);
		}

		// Message when the data enters "high" status
		if (dataGenerated > monitorInfo->high)
		{
			vPrintString(monitorInfo->msg_high);
		}

		vTaskDelay(1000 / portTICK_PERIOD_MS); // Delay the program for ~1s
	}

	vTaskDelete(NULL); // Ends the task
}


// Maps a value from one range to another using linear interpolation
double linearInterpolation(double value, double old_min, double old_max, double new_min, double new_max) {
	return (value - old_min) * (new_max - new_min) / (old_max - old_min) + new_min;
}
