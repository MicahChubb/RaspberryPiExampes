void setup() {
  // This baud rate needs to match the setup on the Pi
  Serial.begin(9600);
}
void loop() {
  // Text you want to send to the Pi
  Serial.println("Hello from Arduino!");
  delay(1000);
}
