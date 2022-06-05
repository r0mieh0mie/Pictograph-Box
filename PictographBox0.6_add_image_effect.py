#IMPORTS
import time
import picamera
from PIL import Image
import RPi.GPIO as GPIO
import pygame

#GPIO SETUP
GPIO.setwarnings(False) #ignore GPIO warnings
GPIO.setmode(GPIO.BOARD) #use physical pin numbering (wip-folder, diagram, grey numbers)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 40 to be an input pin

#CAMERA SETUP
camera = picamera.PiCamera(resolution=(1296, 972), framerate=20) #resolution & framerate of preview
camera.start_preview() #start preview

#VIEWFINDER HUD
img = Image.open('HUD1.png') #load the image
pad = Image.new('RGBA', ( #create an image padded to the required size with RGBA mode
    ((img.size[0] + 31) // 32) * 32,
    ((img.size[1] + 15) // 16) * 16,
    ))
pad.paste(img, (0, 0)) #paste the original image into the padded one
o = camera.add_overlay(pad.tobytes(), size=img.size) #add the overlay with the padded image as the source, but the original image's dimensions
o.layer = 3 #move overlay above camera preview layer (which is layer 2 by default)

#PYGAME SETUP FOR SOUNDS
pygame.init()
pygame.mixer.init()
my_sound = pygame.mixer.Sound('Shutter.wav')

#-------------------------------------------------------------------------------------------------------------------------------------------------
#BUTTON PUSH
prev_input = 1 #initialise a previous input variable to 1 (assume button not pressed last)
while True:
  input = GPIO.input(40) #take a reading
  if ((not prev_input) and input): #if the last reading was low and this one high, then:

#PLAY SHUTTER SOUND    
    my_sound.play() #play the sound
    print("played shutter sound") #print success message
    
#TAKE PHOTO
    #tempphoto_name = "/home/pi/Desktop/PictographBox/1pictemp/pictograph_" + str(time.time()) + ".jpg" #where the temporary photo will be saved
    tempphoto_name = "/home/pi/Desktop/PictographBox/1pictemp/pictograph_temp" + ".jpg" #where the temporary photo will be saved
    camera.capture(tempphoto_name) #take the photo
    print("took photo") #print success message
    
  prev_input = input #update previous input
  time.sleep(0.05) #slight pause to debounce
#--------------------------------------------------------------------------------------------------------------------------------------------------
#PENIS
  