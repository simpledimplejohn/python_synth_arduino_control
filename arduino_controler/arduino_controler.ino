void setup() {
    Serial.begin(9600);
}

void loop() {
    int freqPot = analogRead(A0);
    int ampPot = analogRead(A1);

    // Reverse the values (0 → 1023, 1023 → 0)
    freqPot = map(freqPot, 0, 1023, 1023, 0);
    ampPot = map(ampPot, 0, 1023, 1023, 0);

    Serial.print(freqPot);
    Serial.print(",");
    Serial.println(ampPot);
    delay(50);
}
