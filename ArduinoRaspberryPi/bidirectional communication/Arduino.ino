const int led = 13;

void setup() {
  
  // This baud rate must match the one set up for Pi
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  // If there is a serial message available
  if (Serial.available() > 0) {
    
    // Read it into our string
    String data = Serial.readStringUntil('\n');
    
    Serial.print("You sent me: ");
    Serial.println(data);
    
    // If the data is our keyword
    if(data == "On"){
      
      // Do the action
      digitalWrite(led, HIGH);
    }else{
      digitalWrite(led, LOW); 
    }
  }
}
