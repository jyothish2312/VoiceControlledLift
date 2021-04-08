//For now it's just a quick and dirty code... under development!
//this arduino code is designed to work with the arduino connected to a computer which is running the main.py script.
//That computer can be a raspberry pi or any other single board computer capable of running the python program for speech recognition (main.py)
#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
byte x;
void setup() {
  
  Serial.begin(9600);
  servo1.attach(4);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(7);
  servo5.attach(8);
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  servo5.write(0);
 }

void loop() {
while(Serial.available()==0){
}
x = Serial.read();

if (x==1){
  servo1.write(120);
  delay(50);
  servo1.write(0);
}

if (x==2){
  servo2.write(120);
  delay(50);
  servo2.write(0);
}

if (x==3){
  servo3.write(120);
  delay(50);
  servo3.write(0);
}
if (x==4){
  servo4.write(120);
  delay(50);
  servo4.write(0);
}

if (x==5){
  servo5.write(120);
  delay(50);
  servo5.write(0);
}

}
