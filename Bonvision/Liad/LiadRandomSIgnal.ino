unsigned long lastTime = millis();
int toggle = 0 ;

void setup() {
  // put your setup code here, to run once:
  pinMode(5,OUTPUT);

  digitalWrite(5,LOW);

}

void loop() {

  if ((millis()-lastTime)>random(5,20))
  {
    toggle = !toggle;
    digitalWrite(5,toggle);
    lastTime  = millis();
  }
  // put your main code here, to run repeatedly:

}
