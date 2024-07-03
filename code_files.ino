void setup() {
  Serial.begin(9600); 
  pinMode(11, OUTPUT)
  pinMode(10, OUTPUT)
  pinMode(9, OUTPUT)
}

void loop() {
  if (serial.available > 0){
    incoming_action = serial.read();
  }
  if (incoming_action == "a"){
    digitalWrite(11, HIGH);
    delay(1000);
  }
  if (incoming_action == "b"){
    digitalWrite(10, HIGH);
    delay(1000);
  }
  if (incoming_action == "c"){
    digitalWrite(9, HIGH);
    delay(1000);
  }
}