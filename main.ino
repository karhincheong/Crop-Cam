const int bufferSize = 32;
char inputBuffer[bufferSize];

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    int len = Serial.readBytesUntil('\n', inputBuffer, bufferSize - 1);
    inputBuffer[len] = 0; // Null-terminate the string

    // Split the string into pin and value
    char* token = strtok(inputBuffer, " ");
    if (token != NULL) {
      int pin = atoi(token); // Convert the first part to an integer (pin number)
      
      token = strtok(NULL, " ");
      if (token != NULL) {
        int value = atoi(token); // Convert the second part to an integer (PWM value)

        // Ensure the pin and value are within valid range
        if (pin >= 2 && pin <= 13 && value >= 0 && value <= 255) {
          pinMode(pin, OUTPUT); // Set the specified pin as output
          analogWrite(pin, value); // Write the PWM value to the specified pin
      }
    }
  }
}
