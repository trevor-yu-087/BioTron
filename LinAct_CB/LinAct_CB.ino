// Declare pins
int buttonPin = 3;
int actPin = 5;

bool act_state = false;     // state of the actuator
bool button_state = false;  // check if button has been pressed
bool prev_state = false;    // what it was before

// act_state 1 -> hand closed
// act_state 0 -> hand open

void setup() {
 // put your setup code here, to run once:
 pinMode(actPin, OUTPUT);
 pinMode(buttonPin, INPUT);

 // to read out numbers and debug

 // rate at which data was sent, need to match with computer but 9600 is fine
 //Serial.begin(9600);

}

void loop() {
 // put your main code here, to run repeatedly:
 //checkButton(); // Update what button state is

 button_state = debounce(prev_state);

 if(button_state != prev_state) {
   if(button_state == true){
     // Do action
     act_state = !act_state; // switch actuator state
   }
   button_state = prev_state;
 }

 Actuate(act_state);
 delay(100);

}

void checkButton() {
 button_state = digitalRead(buttonPin);
 // need a time delay and check again
}

void Actuate(bool state) {
 if(state == false) {
   analogWrite(actPin, 250);
 }
 else{
   analogWrite(actPin, 20); // realistically around 20 cause 0 stalls
 }
}

bool debounce(bool last) {
  boolean current = digitalRead(buttonPin);
  if(last != current){
    delay(5);
    current = digitalRead(buttonPin);
  }
  return current;
}
