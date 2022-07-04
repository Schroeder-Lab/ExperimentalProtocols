

#define wheelPin_1 5        // Wheel
#define wheelPin_2 3        // Wheel
#define cameraPin 7             // digital pin of sync
#define syncPin 3             // digital pin of sync

/*
int photodiodePin = 0;    
int syncPin = 0;
*/

unsigned int wheelVal1;
unsigned int wheelVal2;
unsigned int CameraVal;

unsigned long lastTime = millis();
unsigned int toggle = 0 ;

void setup()

{
  pinMode(wheelPin_1, INPUT);   // PhotoDiode
  pinMode(wheelPin_1, INPUT);   // digital pin of sync
  pinMode(cameraPin, INPUT);
  pinMode(syncPin,OUTPUT);

  digitalWrite(syncPin,LOW);
  
  Serial.begin(128000);          //  setup serial
  delay(500);
}



void loop()

{

  wheelVal1 = analogRead(wheelPin_1);    // read the input pin
  wheelVal2 = analogRead(wheelPin_2);
  CameraVal = analogRead(cameraPin);

  if ((millis()-lastTime)>random(5,20))
  {
    toggle = !toggle;
    digitalWrite(syncPin,toggle);
    lastTime  = millis();
  }

  Serial.print(wheelVal1);
  Serial.print("\t");
  Serial.print(wheelVal2);
  Serial.print("\t");
  Serial.print(CameraVal);
  Serial.print("\t");
  Serial.println(toggle);

  delay(0);
}
