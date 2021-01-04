#define SEG_A 9
#define SEG_B 9
#define SEG_C 7
#define SEG_D 5
#define SEG_E 4
#define SEG_F 2
#define SEG_G 11
#define SEG_DP 6

void setup() {
  Serial.begin(9600);

  pinMode(SEG_A, OUTPUT);
  pinMode(SEG_B, OUTPUT);
  pinMode(SEG_C, OUTPUT);
  pinMode(SEG_D, OUTPUT);
  pinMode(SEG_E, OUTPUT);
  pinMode(SEG_F, OUTPUT);
  pinMode(SEG_G, OUTPUT);
  pinMode(SEG_DP, OUTPUT);
}

void loop() {
  switch (Serial.read()) {
  case '0':
    reset_pin();
    digitalWrite(SEG_G, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '1':
    reset_pin();
    digitalWrite(SEG_A, HIGH);
    digitalWrite(SEG_D, HIGH);
    digitalWrite(SEG_E, HIGH);
    digitalWrite(SEG_F, HIGH);
    digitalWrite(SEG_G, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '2':
    reset_pin();
    digitalWrite(SEG_C, HIGH);
    digitalWrite(SEG_F, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '3':
    reset_pin();
    digitalWrite(SEG_E, HIGH);
    digitalWrite(SEG_F, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '4':
    reset_pin();
    digitalWrite(SEG_A, HIGH);
    digitalWrite(SEG_D, HIGH);
    digitalWrite(SEG_E, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '5':
    reset_pin();
    digitalWrite(SEG_B, HIGH);
    digitalWrite(SEG_E, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '6':
    reset_pin();
    digitalWrite(SEG_B, HIGH);
    break;

  case '7':
    reset_pin();
    digitalWrite(SEG_D, HIGH);
    digitalWrite(SEG_E, HIGH);
    digitalWrite(SEG_G, HIGH);
    digitalWrite(SEG_DP, HIGH);
    break;

  case '8':
    reset_pin();
    digitalWrite(SEG_DP, HIGH);
    break;

  case '9':
    reset_pin();
    digitalWrite(SEG_E, HIGH);
    break;

  default:
    break;
  }
}

void reset_pin() {
  digitalWrite(SEG_A, LOW);
  digitalWrite(SEG_B, LOW);
  digitalWrite(SEG_C, LOW);
  digitalWrite(SEG_D, LOW);
  digitalWrite(SEG_E, LOW);
  digitalWrite(SEG_F, LOW);
  digitalWrite(SEG_G, LOW);
  digitalWrite(SEG_DP, LOW);
}
