# This file operating the whole project, the initiation of the whole program & sub programs is based here
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from picamera import PiCamera # Import Raspberry Pi camera stuff
from picamera.array import PiRGBArray # Produces a 3-dimensional RGB array from an RGB capture
from color_detect as PROCESS # Color detection algorithm
from cv2 #OpenCV-Python is a library of python bindings designed to solve computer vision problems
import RPi.GPIO as GPIO # This pacage provides a Python module to control the GPIO on a Raspberry Pi
import pygame # cross-platform set of Python modules, it includes computer graphics and sound libraries designed to be used with Python
import time # This module provides various time-related functions
import serial # This module encapsulates the access for the serial port. It provides backends for Python running on OS
import photoresistor # For flash lighting mechanism
import hc04 # For HC-SR04 distance measuring module
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

button=18

# Legend: (Related to Arduino nano screen & voice messages)
# 0-6 colors (respectively): blue,green,red,pink,yellow,black
# 10 - Same color
# 11 - Different colors
# 80-87 saves color using cnt%10  (respectively):  blue,green,red,pink,yellow,black
# 90 - No object was found
# 91 - Object located too far from the camera
# 92 - Clear

msgs = [b"0\n", b"1\n", b"2\n", b"3\n", b"4\n", b"5\n", b"6\n", b"7\n", b"8\n", b"90\n", b"91\n"]
msgs_saved = [b"80\n", b"81\n", b"82\n", b"83\n", b"84\n", b"85\n", b"86\n", b"87\n"]

#Serial Communication using USB connection between Raspberry Pi to Arduino Nano
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except:
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
ser.flush()

def show_images(images, text, color_idx):
    # show the frame
    cv2.putText(images[0], "%s:%s" % (color_idx, text[0]), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Frame", images[0])

#Preparing the Camera for photographing:
def begin_capture():
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    pygame.mixer.init()

    # Camera resolution 640x480, a middle value (not the maximal resolution to go easy on the processing time)
    camera.resolution = (640,480)
    # 60Hz framerate
    camera.framerate = 60
    line = ""
    rem_color = ""
    idx = 0
    
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    
    #When the system print+play "ready" to the user
    pygame.mixer.music.load("/home/pi/audio/Ready_to_go.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

# - Begining of the project testing - Begin photographing: -
# capture frames from the camera
#for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # Infinite loop
    while True:
        # Grab the raw NumPy array representing the image
        camera.capture('image.jpg') #Take an image
        img = cv2.imread('image.jpg')

        images, text, color = PROCESS.process_image(img) #image proc
        photoresistor.read_photoresistor() #turn on photoresistor if needed
        dis = hc04.calc_distance() # calc distance using ultrasonic sensor
        print(dis)

        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            
        cur_color = text
        if text == "blue":
            idx = 0
            
        elif text == "green":
            idx = 1
           
        elif text == "red":
            idx = 2
            
        elif text == "pink":
            idx = 3
            
        elif text == "yellow":
            idx = 4
    
            
        elif text == "black":
            idx = 5
        
        elif text == "Not Found":
            idx = 9
            
            # line == button (A/B)
        if line == 'a' and rem_color == "":
            if dis <= 100:
                ser.write(msgs[idx])
                pygame.mixer.music.set_volume(1.0)
                dir = "/home/pi/audio/" + text + ".mp3"
                pygame.mixer.music.load(dir)
                pygame.mixer.music.play()
            else:
                ser.write(msgs[10])
                pygame.mixer.music.set_volume(1.0)
                dir = "/home/pi/audio/far.mp3"
                pygame.mixer.music.load(dir)
                pygame.mixer.music.play()


            

        
        if line == 'a' and rem_color != "":
            if dis <= 100:
                if rem_color == cur_color:
                    ser.write(b"10\n")
                    pygame.mixer.music.load("/home/pi/audio/Same colors.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
                else:
                    ser.write(b"11\n")
                    pygame.mixer.music.load("/home/pi/audio/Not same color.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
            else:
                ser.write(msgs[10])
                pygame.mixer.music.set_volume(1.0)
                dir = "/home/pi/audio/far.mp3"
                pygame.mixer.music.load(dir)
                pygame.mixer.music.play()
            
                
        elif line == 'b':
            if dis <= 100:
                if rem_color == "":
                    if idx != 9:
                        rem_color = cur_color
                        ser.write(msgs_saved[idx])
                        print(msgs_saved[idx])
                        pygame.mixer.music.load("/home/pi/audio/saved.mp3")
                        pygame.mixer.music.set_volume(1.0)
                        pygame.mixer.music.play()
                    else:
                        ser.write(msgs[idx])
                        pygame.mixer.music.set_volume(1.0)
                        dir = "/home/pi/audio/Not Found.mp3"
                        pygame.mixer.music.load(dir)
                        pygame.mixer.music.play() 
                else:
                    rem_color = ""
                    ser.write(b"92\n")
                    pygame.mixer.music.load("/home/pi/audio/clear.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play()
            else:
                ser.write(msgs[10])
                pygame.mixer.music.set_volume(1.0)
                dir = "/home/pi/audio/far.mp3"
                pygame.mixer.music.load(dir)
                pygame.mixer.music.play()            
                
                
                

        line = ""

        # clear the Greenstream in preparation for the next frame
        #GPIO.wait_for_edge(18, GPIO.FALLING)
        #if GPIO.input(18):
        rawCapture.truncate(0)

cur_color ="12"
print("Starting camera...")
begin_capture()

 

        
# End
