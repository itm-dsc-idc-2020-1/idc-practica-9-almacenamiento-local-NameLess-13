int LDRPin = 0;
int max = 1023;
int min = 0;
int valor = 0;
void setup() {
  Serial.begin(9600);  
}

void loop() {
  valor = analogRead(LDRPin);
  Serial.println(valor);
}
