# Color-Detection
Final B.Sc. Project, Color detection device using Image processing / Roy Ben Avraham 2021-2022

# Short Description:
This project was carried out as part of an internal engineering design (final project) consisting of two parts: Engineering Design A and Engineering Design B at the "Ort Braude Academic College of Engineering" located in Karmiel.
The purpose of this project is to identify the color of a certain object using a video camera, and present it to the end user using a dedicated screen and an audio message. The final device is a prototype that will hopefully help the user measure colors accurately for various home or business uses.
In order to operate the device, the user is expected to place the desired object in front of the camera lens (front of the device). The user has two ways to use this device, check a color against a pre-saved color or measure some color and save it in the system.
The device is based on the "Raspberry Pi 3 Model B" controller. The device works by connecting to the electriciy outlet with a suitable cable or a rechargeable portable battery, thus allowing the device to be portable.
In order to achieve the goals of this project, a variety of sensors are used that are essential for the proper operation of the device. The main sensor on which the device is based is the camera, through which the color of the object can be measured. However, two sensors are used that help the proper operation of the camera are distance sensor that verifies that the object is not too far from the camera, and a photoresistor sensor that turns on an array of LED lights in insufficient lighting conditions.

# System requirements:

- Algorithm for processing the image and locating the surface/object.
- Algorithm to detect the color of the surface/object.
- Displaying the detected color on the screen and playing a voice message from a speaker.
- Taking a picture of a surface/object.
- The device will be portable and powered by a rechargeable battery of up to 2 [A] current and voltage of up to 5 [V].
- The device will have the ability to save a color in the system and compare it with another detected color.
- The time of obtaining the color tone of the object under examination from the moment of pressing the button shall not exceed 2 seconds.

# Block diagram

![image](https://user-images.githubusercontent.com/105777016/190319969-8a83d7aa-52bb-4f45-b5d9-0407dbf8fe41.png)

## Planning and development stages 

# Platform
The platform chosen for implementation of this project is Raspberry Pi OS (also known as: "Raspbian") ![image](https://user-images.githubusercontent.com/105777016/190320285-f11e5c6c-2ca5-47d7-9449-0cd0f7c12719.png). The controller was programmed using the Python programming language, version 3.7.3. This programming language is the optimized and recommended language for working with this controller. For the Arduino nano controller the platform is Arduino IDE and the programming language for this controller is C++. OpenCV version 3.2 was used for the image processing operations.

OpenCV (Open-Source Computer Vision Library) - is a set of libraries for computer vision and image processing distributed as open source.

# Software design

Sensors
• For sensors: HC-SR04 (ultrasonic distance sensor) and LDR (light sensitive resistor) a suitable algorithm was written in the Arduino nano controller. The algorithm of the ultrasonic distance sensor frequently checks what the distance is called according to the principle of the sensor's operation (detailed later in this document). The LDR's algorithm allows sampling of the illumination intensity from the digital pin of the sensor so that the measurement result will lead to one of two options: Illuminated or dark, according to a set threshold value.

 Photography and image processing
 
 

• The controller (Raspberry Pi) is responsible for processing the data from the camera. When the user clicks the photo button, the controller with the help of the camera will take a picture. Next, it must locate the object the user photographed and characterize its color.

# Communication

The Arduino nano controller is responsible for receiving input from the user via the buttons and printing to the LCD screen. The communication between the Arduino nano controller and the Raspberry Pi controller will be done through a USB connector and the communication will be done by writing and reading through the Serial port.
Serial communication is used to transfer information bidirectionally between the two controllers. The information passes serially, one bit at a time. In fact, serial communication between the Arduino Nano controller and the Raspberry Pi controller uses the UART (Universal Asynchronous) protocol Reception and Transmission.) The simplest and most convenient way to have serial communication between the two controllers is through a USB (Universal Serial Bus) cable that connects the two.
On the Arduino nano controller - you can use hardware interrupts. These interrupts will be used to operate the system buttons, the Arduino nano controller supports 2 hardware interrupts - therefore the device will have 2 buttons to operate the system. As mentioned before, after pressing one of the buttons the information will be transferred from the Arduino serially to the Raspberry Pi using on the USB cable connecting the two.

The data transfer rate on the USB cable is set to 9600 bits per second (default value).
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
ser.flush()

By using the Serial library, I defined the communication ports and their speed as seen in the above code section.
In the iterative part (loop), the Arduino in each iteration will check whether information is sent in the Serial monitor, I will demonstrate a case where a green object was detected in the camera lens:
 Here a test is carried out to see if information is sent in the Serial monitor:
void loop() {
  // Set the cursor to column 0, line 1 in the LCD
  if(Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    cnt = data.toInt();
    temp = true;
  }

If a green object is detected, the Raspberry Pi controller will send the corresponding index to the Arduino controller (in this case, index number 1):
  elif text == "green":
            idx = 1
            
# Hardware design

Camera:
The chosen camera is the Raspberry Pi Camera Board V1.3. This camera has a dedicated socket in the Raspberry Pi controller, so it is recommended and convenient to work with this controller.

![image](https://user-images.githubusercontent.com/105777016/190323081-c7775f8c-0210-42fb-8f02-a06b2eae8f14.png)

Several technical parameters:
- The camera resolution is 5 megapixels.
- The maximum image resolution is 1944X2592.
- Viewing angle: 65 degrees.
- The connector type is 15-pin MIPI Camera Serial Interface.

This camera is suitable for the needs of this project and the images it produces are clear enough to be analyzed.

Sensors:     

- Ultrasonic distance sensor - HC-SR04: ![image](https://user-images.githubusercontent.com/105777016/190323042-7425bae4-0509-44a3-8859-55baffe5b4b8.png)
allows to measure the distance from the camera lens to the object. This sensor is installed close to the camera lens in order to find the distance of the object from the lens and not necessarily from the device itself. The sensor will make sure that the distance of the lens does not exceed one meter from the camera lens and will be connected directly to the GPIO (General Purpose Input/Output) of the Raspberry Pi controller.

- Lighting sensor (module) - LDR (Light Dependent Resistor): ![image](https://user-images.githubusercontent.com/105777016/190323059-b072b8f5-1b63-4281-9b25-e8bb9ababd83.png)
 This sensor is actually a resistor whose resistance changes according to the intensity of the illumination on its surface. With the help of a potentiometer installed on the module, it is possible to determine the threshold level from which any illuminance will be considered bright or dark. The measured illuminance is analog and converted to digital using the module to which the sensor is soldered, this feature makes working with this module easy since the Raspberry Pi controller has no analog pins. If the read illuminance value is below the set threshold (ie dark) the flash lighting system made of white LED lights will be turned on.

