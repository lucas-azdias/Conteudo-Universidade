#include <WiFi.h>
#include <PubSubClient.h>
#define DHT_SENSOR_PIN  21 // ESP32 pin GIOP21 connected to DHT11 sensor
#define DHT_SENSOR_TYPE DHT11

#define LED_BUILTIN 2

int LDR_Val = 0;     /*Variable to store photoresistor value*/
int VALUE = LOW;
int sensor = 34;      /*Analogue Input for photoresistor*/
int led = 2;    
int control = LOW;     /*LED output Pin*/
int command = LOW;
//Conexão com o WiFI
const char *SSID = "Wokwi-GUEST";
const char *PWD = "";

//configurações de conexão MQTT
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient); 
char *mqttServer = "broker.hivemq.com";
int mqttPort = 1883;

//função para conectar ao WiFi
void ConectaNoWiFi() {
  Serial.print("Conectando ao WiFi");
  WiFi.begin(SSID, PWD);
  //Caso tenha dificuldades em conectar, imprime um “.” 
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  //Se conectado, imprime “Conectado” 
  Serial.print("Conectado.");
}

//Realiza a conceção com o Broker MQTT 
void conectaBrokerMQTT() {
  Serial.println("Conectando ao broker");
  //A função mqttClient.connected() verifica se existe uma conexão ativa.  Depende do Broker, a conexão pode se manter ativa, ou desativar a cada envio de msg.  
  while (!mqttClient.connected()) {
      //Se entrou aqui, é porque não está conectado. Então será feito uma tentativa de conexão infinita, até ser conectado.  
      Serial.println("Conectando ao Broker MQTT");
      //define o nome da ESP na conexão. Está sendo gerado um nome aleatório, para evitar ter duas ESPs com o mesmo nome. Neste caso, uma derrubaria a outra.  
      String clientId = "ESP32Client-";
      clientId += String(random(0xffff), HEX);
      //Realiza a conexão com a função “mqttClient.connect”. Caso seja um sucesso, entra no if e imprime “Conectado ao Broker MQTT.” 
      if (mqttClient.connect(clientId.c_str())) {
        Serial.println("Conectado ao Broker MQTT.");
      }
  }
  mqttClient.subscribe("/adviniski/control");
  mqttClient.subscribe("/adviniski/command");
}

void callback(char* topic, byte* payload, unsigned int length) {
    String msg;

  // Obtem a string do payload recebido
    for (int i = 0; i < length; i++) {
      char c = (char)payload[i];
      msg += c;
    }
    if (strcmp(topic,"/adviniski/control")==0){
      if(msg.equals("1")){
          control = HIGH;
      } else {
          control = LOW;
      }
    }
    if (strcmp(topic,"/adviniski/command")==0 and control == HIGH){
        if(msg.equals("1")){
            digitalWrite(LED_BUILTIN, HIGH);
            mqttClient.publish("/adviniski/infoLED", "Acendendo a lux");
            command = HIGH;
        } else {
            digitalWrite (LED_BUILTIN, LOW);
            mqttClient.publish("/adviniski/infoLED", "Desligando a luz");
            command = LOW;
        }
    }
    if(command == HIGH && control == HIGH){
        digitalWrite(LED_BUILTIN, HIGH);
        mqttClient.publish("/adviniski/infoLED", "Acendendo a lux");
    } else {
      digitalWrite (LED_BUILTIN, LOW);
      mqttClient.publish("/adviniski/infoLED", "Desligando a luz");
    }
    Serial.print("Control:");
    Serial.println(control);
    Serial.print("Command:");
    Serial.println(command);
}

//Realiza as configurações do MQTT 
void setupMQTT() {
  mqttClient.setServer(mqttServer, mqttPort);
  mqttClient.setCallback(callback);           // Atribui função de callback (função chamada quando qualquer informação de um dos tópicos subescritos chega)
}

void ldr(){
    if(control == LOW) { 
      int ACTUAL = LOW;
      LDR_Val = analogRead(sensor);   /*Analog read LDR value*/
      if(LDR_Val > 100) {       /*If light intensity is HIGH*/
        ACTUAL = LOW;
      }
      else if(LDR_Val <= 100){
        ACTUAL = HIGH;
      }

      if(ACTUAL != VALUE){
        if(ACTUAL == HIGH){
          mqttClient.publish("/adviniski/LDR", "Ligou a luz:");
        }else{
          mqttClient.publish("/adviniski/LDR", "Desligou a luz:");
        }
        digitalWrite(led,ACTUAL);
      }
      VALUE = ACTUAL;
    }    
}

//setup
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);   /*LED Pin set as output */
  ConectaNoWiFi();
  setupMQTT();
}


//loop
void loop() {
    
    //Verifica se a conexão está ativa, caso não esteja, tenta conectar novamente.  
    if (!mqttClient.connected()){
        conectaBrokerMQTT();
    }
    mqttClient.loop();
    ldr();
    delay(50);
}