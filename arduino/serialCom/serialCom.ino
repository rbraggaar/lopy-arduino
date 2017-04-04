void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){ // at least one byte is available from the Lopy
    // read the message from the Lopy
    String msg = Serial.readStringUntil('\n');
    // and repeat the message back
    Serial.println("Lopy, did you say: " + msg + "?");
  }
}
