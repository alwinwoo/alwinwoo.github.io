# [Arduino](https://alwinwoo.github.io/pages/arduino.html)
[home](https://alwinwoo.github.io/) | [edit](https://github.com/alwinwoo/alwinwoo.github.io/edit/master/pages/arduino.md)

# Basics
  - need to download arduino IDE
  - switching analog pins in close temporal proximity may cause electrical noise and introduce jitter in the analog system. It may be desirable, after manipulating analog pins (in digital mode) to add a short delay before using analogRead() to read other analog pins.
  - (Board dependent?)
  - using millis instead of delay
    - <https://www.programmingelectronics.com/arduino-sketch-with-millis-instead-of-delay/>

# Code Example
  ```code
  
  #define ledPin  1     // compiler will replace any mention of ledPin with the value 1 at compile time - no semicolon or equal sign
  int inPin     = 2;   // pushbutton connected to digital pin 2
  int analogPin = A3;  // potentiometer wiper (middle terminal) connected to analog pin 3
                       // outside leads to ground and +5V
  int val  = 0;        // variable to store the read value
  int val2 = 0;        // variale to store analogue output
  
  bool start = false;       // data types - array, bool(ean), char, double, float, int, long, short, string, word
  string msg = String(10);  // 10 characters
  
  int myMultiplyFunction(int x, int y)  {       // defines a function called myMultiply Function with 2 input variables
    int result;
       result = x * y;
    return result;
  }
  
  
  void setup() {
    pinMode(ledPin, OUTPUT);  // sets the digital pin 1 as output
    pinMode(inPin, INPUT);    // sets the digital pin 2 as input
    
    Serial.begin(9600);       //  setup serial
  }

  void loop() {
    val = digitalRead(inPin);   // read the input pin
    digitalWrite(ledPin, val);  // sets the LED to the button's value
    delay(1000);                // waits for a second
    
    val2 = analogRead(analogPin);  // read the analog input pin
    Serial.println(val2);          // prints the value to be viewed on the IDE serial monitor (Tools)
    analogWrite(ledPin, val2 / 4); // analogRead values go from 0 to 1023, analogWrite values from 0 to 255    
  }
  
  for (initialization; condition; increment) {
    // commented statement(s);
  }
  
  switch (var) {
    case label1:
      // statements
      break;
    case label2:
      // statements
      break;
    default:
      // statements
      break;
  }
  
  Boolean     ! && || 
  Comparison  != == < <= >= > 
  
  ```
  - <https://www.arduino.cc/reference/en/>
  - <https://www.programmingelectronics.com/category/programming-based/>

# Digispark ATtiny85
  - open Arduino ide and then go to preferences and then in additional board manager, paste this given url for Digispark :-
    - <http://digistump.com/package_digistump_index.json>
  - Now go to boards manager and download the Digispark boards
    - <https://digistump.com/wiki/digispark/tutorials/connecting>
  - Window / Linux drivers are required to communicate with the Digispark in USB
    - <https://github.com/digistump/DigistumpArduino/releases>

  # Digispark Keyboard
    ```code
    #include <DigiKeyboard.h>             // include the library to print text
    DigiKeyboard.delay(1000);             // delay for 1 second
    DigiKeyboard.println("Hello World");  // print text like a keyboard
    ```

# ESP8266 wifi module
  - <https://www.instructables.com/id/Control-ESP8266-Over-the-Internet-from-Anywhere/>
  - <https://tttapa.github.io/ESP8266/Chap01%20-%20ESP8266.html>
  - <https://randomnerdtutorials.com/esp8266-web-server/>
  - <https://www.arduino.cc/reference/en/>

# Projects
  - <http://arduinolearning.com/digispark/basic-digispark-example.php>
  - <https://www.raspberry-pi-geek.com/Archive/2014/03/Adding-analog-input-to-the-Pi-using-the-Digispark>
