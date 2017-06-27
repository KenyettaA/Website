#include <Servo.h>  

Servo servoLeft;   
Servo servoRight; 

void setup()                                 // Built-in initialization block
{
  Serial.begin(9600);
  
  tone(4, 500, 1000);                       // (port, tone, length)
  delay(1000);                               
  pinMode(13, INPUT);                         // Set RIGHT whisker pin to input
  pinMode(12, INPUT);                         // Set LEFT whisker pin to input  

  servoLeft.attach(13);                
  servoRight.attach(12);    
                          // Set data rate to 9600 bps
}  

  void moveForward(){
    servoLeft.writeMicroseconds(1700);         
    servoRight.writeMicroseconds(1300);        
  } 
  void moveBackward(int x){
    servoLeft.writeMicroseconds(1700);         
    servoRight.writeMicroseconds(1300);
      delay(x);        
  } 
  void turnLeft(){
    servoLeft.writeMicroseconds(1300);         // Turns left
    servoRight.writeMicroseconds(1300);        
      delay(544);
  }

 
void loop()                                  // Main loop auto-repeats
{    
   
  byte wLeft = digitalRead(13);               // Copy left result to wLeft  
  byte wRight = digitalRead(12);              // Copy right result to wRight
  
  Serial.print(wLeft);                       // Display left whisker state
  Serial.println(wRight);                    // Display right whisker state

                                  // Pause for 50 ms
  
        

  if (wLeft==0 or wRight==0){
    moveBackward(500); 
    turnLeft();        
    }
  else {
    moveForward();
  }
  
  delay(50);       
}    

