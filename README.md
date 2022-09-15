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
