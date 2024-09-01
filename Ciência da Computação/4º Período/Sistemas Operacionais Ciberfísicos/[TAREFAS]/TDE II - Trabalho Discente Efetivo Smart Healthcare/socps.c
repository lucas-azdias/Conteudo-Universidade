// Lucas Azevedo Dias - Ciência da Computação (4o Período - Noturno)

#include "contiki.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RESP_TIME_MONITORS 3

// Struct type for the monitoring processes
typedef struct
{
  char *msg;      // Message to show data
  char *unit;     // Unit for the data generated
  double min;     // Minimum value for the data generated
  double max;     // Maximum value for the data generated
  char *msg_low;  // Message if it gets lower than "low"
  double low;     // Reference value for the "low" status
  char *msg_high; // Message if it gets higher than "high"
  double high;    // Reference value for the "high" status
} MonitorInfo;

// Data for the monitoring processes
MonitorInfo beatsInfo = {
  "Batimentos:",
  "bpm",
  20,
  140,
  "Batimentos cardiacos baixos",
  50,
  "Batimentos cardiacos altos",
  90
};
MonitorInfo oxygenInfo = {
  "Saturacao:",
  "%",
  80,
  100,
  "Saturacao de oxigenio do sangue baixa",
  90,
  "INVALIDO",
  101
};
MonitorInfo temperatureInfo = {
  "Temperatura:",
  "oC",
  34,
  41,
  "Hipotermia detectada",
  35,
  "Febre detectada",
  37
};

// Prototypes
double linearInterpolation(double, double, double, double, double);

// Initializing the processes
PROCESS(beat_process, "Beats monitoring program");
PROCESS(oxyg_process, "Oxygen monitoring program");
PROCESS(temp_process, "Temperature monitoring program");
PROCESS(alert_process, "Temperature monitoring program");

// Scheduling the processes
AUTOSTART_PROCESSES(&beat_process, &oxyg_process, &temp_process, &alert_process);

// BEATS monitoring process
PROCESS_THREAD(beat_process, ev, data)
{
  static struct etimer timer; // Event timer of the simulator
  
  MonitorInfo *monitorInfo = &beatsInfo; // Data of the simulator
  double dataGenerated; // Variable for the data randomly generated

  PROCESS_BEGIN(); // Starts the process

  etimer_set(&timer, RESP_TIME_MONITORS * CLOCK_SECOND); // Setting the timer event
  srand(time(NULL)); // Setting the seed for randoms

  for (;;) // Process inifite loop
  {
    // Generating a random number in the range of 0 to 1 and mapping it to the range passed
    dataGenerated = linearInterpolation(rand(), 0, RAND_MAX, monitorInfo->min, monitorInfo->max);

    // Displays the message and the data
    printf("%s %.2lf%s\n", monitorInfo->msg, dataGenerated, monitorInfo->unit);

    // Alerts when the data enters "low" status
    if (dataGenerated < monitorInfo->low)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_low);
    }

    // Alerts when the data enters "high" status
    if (dataGenerated > monitorInfo->high)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_high);
    }

    // Awaits the timer event triggering
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&timer));

    // Resets the timer
    etimer_reset(&timer);
  }

  PROCESS_END(); // Ends the process
}

// OXYGEN monitoring process
PROCESS_THREAD(oxyg_process, ev, data)
{
  static struct etimer timer; // Event timer of the simulator

  MonitorInfo *monitorInfo = &oxygenInfo; // Data of the simulator
  double dataGenerated; // Variable for the data randomly generated

  PROCESS_BEGIN(); // Starts the process

  etimer_set(&timer, RESP_TIME_MONITORS * CLOCK_SECOND); // Setting the timer event
  srand(time(NULL)); // Setting the seed for randoms

  for (;;) // Process inifite loop
  {
    // Generating a random number in the range of 0 to 1 and mapping it to the range passed
    dataGenerated = linearInterpolation(rand(), 0, RAND_MAX, monitorInfo->min, monitorInfo->max);

    // Displays the message and the data
    printf("%s %.2lf%s\n", monitorInfo->msg, dataGenerated, monitorInfo->unit);

    // Alerts when the data enters "low" status
    if (dataGenerated < monitorInfo->low)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_low);
    }

    // Alerts when the data enters "high" status
    if (dataGenerated > monitorInfo->high)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_high);
    }

    // Awaits the timer event triggering
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&timer));

    // Resets the timer
    etimer_reset(&timer);
  }

  PROCESS_END(); // Ends the process
}

// TEMPERATURE monitoring process
PROCESS_THREAD(temp_process, ev, data)
{
  static struct etimer timer; // Event timer of the simulator

  MonitorInfo *monitorInfo = &temperatureInfo; // Data of the simulator
  double dataGenerated; // Variable for the data randomly generated

  PROCESS_BEGIN(); // Starts the process

  etimer_set(&timer, RESP_TIME_MONITORS * CLOCK_SECOND); // Setting the timer event
  srand(time(NULL)); // Setting the seed for randoms

  for (;;) // Process inifite loop
  {
    // Generating a random number in the range of 0 to 1 and mapping it to the range passed
    dataGenerated = linearInterpolation(rand(), 0, RAND_MAX, monitorInfo->min, monitorInfo->max);

    // Displays the message and the data
    printf("%s %.2lf%s\n", monitorInfo->msg, dataGenerated, monitorInfo->unit);

    // Alerts when the data enters "low" status
    if (dataGenerated < monitorInfo->low)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_low);
    }

    // Alerts when the data enters "high" status
    if (dataGenerated > monitorInfo->high)
    {
      process_post(&alert_process, PROCESS_EVENT_MSG, monitorInfo->msg_high);
    }

    // Awaits the timer event triggering
    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&timer));

    // Resets the timer
    etimer_reset(&timer);
  }

  PROCESS_END(); // Ends the process
}

// ALERT process
PROCESS_THREAD(alert_process, ev, data)
{
  PROCESS_BEGIN(); // Starts the process

  for (;;) // Process inifite loop
  {
    PROCESS_WAIT_EVENT();

    // Prints the message passed if the event is correct
    if (ev == PROCESS_EVENT_MSG)
    {
      printf("ALERTA! %s\n", (char*) data);
    }
  }

  PROCESS_END(); // Ends the process
}

// Maps a value from one range to another using linear interpolation
double linearInterpolation(double value, double old_min, double old_max, double new_min, double new_max) {
	return (value - old_min) * (new_max - new_min) / (old_max - old_min) + new_min;
}
