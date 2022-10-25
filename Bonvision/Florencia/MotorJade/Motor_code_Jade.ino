#include <Servo.h>


Servo myservo;
// create servo object to control a servo


int ledPin = 13;
int potpin = A0; // analog pin used to connect the potentiometer
int val;// variable to read the value from analog pin
int Convertval;
int Convertval2;

void setup () {
myservo.attach (9); // attaches the servo on pin 9 to the arduino board 
pinMode (ledPin, OUTPUT); //tells the board the servo is an output device
Serial.begin(9600);
}

void loop () {
 
  val = analogRead (potpin);
  Serial.print ("raw value: "); //Value of the potentiometer
  Serial.println(val);

  Convertval = map (val, 0, 1000, 110, 90);//play with the third muber to asjust the speed of motor further away from 90 increases speed. The other side on 90 changes polarity of the servo
  Serial.print ("converted value: ");
  Serial.println (Convertval);

  Convertval2 = (Convertval);
  Serial.print ("converted value 2: ");
  Serial.println (Convertval2);

  myservo.write (Convertval2); //Value sent to the servo
  delay (15);
  
}
