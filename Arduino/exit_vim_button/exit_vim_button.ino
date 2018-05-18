#include <Arduino.h> // Support IntelliSense in VS Code
/*
   Exit Vim Button
   by Reynir Aron
   Arduino sketch
*/
const int BUTTON = 7;        // Pin no. of pushbutton
const int ACTIVE = LOW;      // Button is active low
const int PUSH_DELAY = 1000; // Cooldown in ms between button presses
const char MSG = '1';        // Message to write when button is pressed
int button_state;

void setup() {
    Serial.begin(9600);
}

void loop() {
    button_state = digitalRead(BUTTON);
    if (button_state == ACTIVE) {
        Serial.println(MSG);
        delay(PUSH_DELAY);
    }
}
