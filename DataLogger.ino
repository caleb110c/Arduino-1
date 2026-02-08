#include <OneWire.h>
#include <DallasTemperature.h>


int LedPinR = 8;
float maxtemp = 22;

float temp = 0.0;

int LedPinB = 4;
float mintemp = 18.0;

int Buzzer = 2;

int oneWireBus = 12;
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);


void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(8, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(8, LOW);

  Serial.begin(9600);
  sensors.begin();
}


void loop(void)
{
  sensors.requestTemperatures();
  temp = sensors.getTempCByIndex(0);
  Serial.println(temp);
  delay(100);

  if (temp > maxtemp){
    digitalWrite(8, HIGH);
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(8, LOW);
    digitalWrite(2, LOW);
    delay(500);
  }
  else if(temp < mintemp)
  {
    digitalWrite(4, HIGH);
    delay(1000);
    digitalWrite(4, LOW);
    delay(1000);
  }
  else{
    digitalWrite(8, LOW);
    digitalWrite(4, LOW);
    digitalWrite(2, LOW);
    delay(2000);
  }
} 

