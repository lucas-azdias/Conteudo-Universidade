// Lucas Azevedo Dias - Ciência da Computação 4º Período N

#include "FreeRTOS.h"
#include "basic_io.h"
#include "semphr.h"
#include "task.h"
#include "time.h"


struct Task3Params {
	char* location;
	int min;
	int max;
};


int maxDisplaySize;  // Maximum size of the display
char* displayText;  // Text simulating a public display text
int displayDelayingTime;  // Time for each message in the display
SemaphoreHandle_t displaySemaphore;  // Mutex to access the display text

TaskHandle_t task1Handler;  // Identifies the task 1
TaskHandle_t task2Handler;  // Identifies the task 2
TaskHandle_t task3Handler;  // Identifies the task 3


void vTask1(void *pvParameters);
void vTask2(void* pvParameters);
void vTask3(void* pvParameters);

double linearInterpolation(double, double, double, double, double);


int main_(void)
{
	maxDisplaySize = 20;
	displayText = (char*) malloc((maxDisplaySize + 1) * sizeof(char));  // Initializing the display text
	displayDelayingTime = 500;
	displaySemaphore = xSemaphoreCreateMutex();  // Creating the mutex

	if (displaySemaphore)  // Checks if the mutex has been created successfully
	{
		struct Task3Params task3Params = { "Curitiba", -5, 40 };  // Defining the task 3 parameters

		xTaskCreate(vTask1, "Task 1 - Date", 1000, NULL, 1, &task1Handler);
		xTaskCreate(vTask2, "Task 2 - Time", 1000, NULL, 1, &task2Handler);
		xTaskCreate(vTask3, "Task 3 - Location and temperature", 1000, (void*)&task3Params, 1, &task3Handler);
	}
	else
	{
		vPrintString("An error has occured when creating the mutex.");
	}

	vTaskStartScheduler();  // Initializing the task scheduler

	for (;;);  // Main loop

	return 0;
}


// Date monitoring task
void vTask1(void* pvParameters)
{
	for (;;)
	{
		// Takes the mutex if possible
		if (xSemaphoreTake(displaySemaphore, (TickType_t)0))
		{
			time_t seconds;
			time(&seconds);  // Getting time in seconds
			struct tm* nowDatetime = localtime(&seconds);  // Converting time in seconds to datetime

			int day = nowDatetime->tm_mday;  // Gets day
			int month = nowDatetime->tm_mon + 1;  // Gets month
			int year = nowDatetime->tm_year + 1900;  // Gets year

			// Converting date as a string
			char* dateString = (char*) malloc((maxDisplaySize + 1) * sizeof(char));
			if (0 > snprintf(dateString, 11, "%02d/%02d/%04d", day, month, year))
			{
				vPrintString("An error has occured when formatting the date into a string.");
			}

			strcpy(displayText, dateString); // Copies the date into the display

			// Prints the display
			vPrintString(displayText);
			vPrintString("\n");

			// Frees allocated memory
			free(dateString);

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Keeps the display with this message

			xSemaphoreGive(displaySemaphore);  // Gives back the mutex

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Lets another task change the display
		}
	}

	vTaskDelete(NULL);
}


// Time monitoring task
void vTask2(void* pvParameters)
{
	for (;;)
	{
		// Takes the mutex if possible
		if (xSemaphoreTake(displaySemaphore, (TickType_t)0))
		{
			time_t seconds;
			time(&seconds);  // Getting time in seconds
			struct tm* nowDatetime = localtime(&seconds);  // Converting time in seconds to datetime

			int hour = nowDatetime->tm_hour;  // Gets hour
			int mins = nowDatetime->tm_min;  // Gets minutes
			int secs = nowDatetime->tm_sec;  // Gets seconds

			// Converting time as a string
			char* timeString = (char*) malloc((maxDisplaySize + 1) * sizeof(char));
			if (0 > snprintf(timeString, 11, "%02d:%02d:%02d", hour, mins, secs))
			{
				vPrintString("An error has occured when formatting the time into a string.");
			}

			strcpy(displayText, timeString); // Copies the time into the display

			// Prints the display
			vPrintString(displayText);
			vPrintString("\n");

			// Frees allocated memory
			free(timeString);

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Keeps the display with this message

			xSemaphoreGive(displaySemaphore);  // Gives back the mutex

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Lets another task change the display
		}
	}

	vTaskDelete(NULL);
}


// Location and temperature monitoring task
void vTask3(void* pvParameters)
{
	struct Task3Params* params = (struct Task3Params*) pvParameters;

	char* sep = " ";  // Separator between location and temperature
	char* end = " oC";  // End part after temperature
	int maxTempSize = 2;  // Maximum temperature string size

	for (;;)
	{
		// Takes the mutex if possible
		if (xSemaphoreTake(displaySemaphore, (TickType_t)0))
		{
			// Generating a random number in the range of 0 to 1 and mapping it to the temperature range
			int temperature = linearInterpolation(rand(), 0, RAND_MAX, params->min, params->max);

			// Converting the temperature as a string
			char* tempString = (char*) malloc((maxTempSize + 1) * sizeof(char));
			if (0 > snprintf(tempString, maxTempSize + 1, "%02d", temperature))
			{
				vPrintString("An error has occured when formatting the temperature into a string.");
			}

			// Concatenates the location with the temperature
			char* locTempString = (char*)malloc((maxDisplaySize + 1) * sizeof(char));
			strcpy(locTempString, params->location);
			strcat(locTempString, sep);
			strcat(locTempString, tempString);
			strcat(locTempString, end);

			strcpy(displayText, locTempString); // Copies the location and the temperature into the display

			// Prints the display
			vPrintString(displayText);
			vPrintString("\n");

			// Frees allocated memory
			free(tempString);
			free(locTempString);

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Keeps the display with this message

			xSemaphoreGive(displaySemaphore);  // Gives back the mutex

			vTaskDelay(displayDelayingTime / portTICK_RATE_MS);  // Lets another task change the display
		}
	}

	vTaskDelete(NULL);
}


// Maps a value from one range to another using linear interpolation
double linearInterpolation(double value, double old_min, double old_max, double new_min, double new_max) {
	return (value - old_min) * (new_max - new_min) / (old_max - old_min) + new_min;
}
