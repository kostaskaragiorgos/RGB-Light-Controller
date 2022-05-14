int red_light_pin= 11;
int green_light_pin = 10;
int blue_light_pin = 9;
int red_light_value=255,green_light_value=255,blue_light_value=255;

void setup() {
  Serial.begin(9600);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}
void loop() {
  while(Serial.available() == 0){
    
  }
  red_light_value =Serial.readStringUntil(':').toInt();
  green_light_value =Serial.readStringUntil(':').toInt();
  blue_light_value =Serial.readStringUntil('\r').toInt();

  
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
