#include <Servo.h>
Servo myservo;

void setup() {
  
  // This baud rate must match the one set up for Pi
  Serial.begin(9600);
  myservo.attach(9);
}
void loop() {
  
  // If there is a serial message available
  if (Serial.available() > 0) {
    
    // Read it into our string
    String data = Serial.readStringUntil('\n');

    // If the data is our keyword
    if(data == "move"){
      
      // Do the action (move servo to a random degree)
      int degree = random(180);
      myservo.write(degree);
     
      // Inform the Raspberry Pi about the action
      Serial.print("Degree set to: ");
      Serial.println(degree);
    }
  }
}
