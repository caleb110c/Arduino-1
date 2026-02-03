#include <OneWire.h>
#include <DallasTemperature.h>

float temp = 0.0;
int oneWireBus = 12;
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);


void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Serial.begin(9600);
  Serial.println("Sunny -- 1-wire temperature sensor");
  sensors.begin();
}

void loop(void)
{
  sensors.requestTemperatures();
  temp = sensors.getTempCByIndex(0);
  Serial.print("Temperature is: ");
  Serial.println(temp);

  delay(1000);
} 
