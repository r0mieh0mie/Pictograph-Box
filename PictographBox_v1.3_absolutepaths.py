#!/usr/bin/env python3

#IMPORTS
import time
import datetime
from pathlib import Path
import picamera
from PIL import Image, ImageOps
import RPi.GPIO as GPIO
import pygame
import numpy as np
import io

#PATHS SETUP
script_dir = Path( __file__ ).parent.absolute()

#GPIO SETUP
GPIO.setwarnings(False) #ignore GPIO warnings
GPIO.setmode(GPIO.BOARD) #use physical pin numbering (wip-folder, diagram, grey numbers)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pin 40 to be an input pin

#PYGAME SETUP FOR SOUNDS
pygame.init()
pygame.mixer.init()
shuttersound = pygame.mixer.Sound(str(script_dir)+'/Shutter.wav')
savesound = pygame.mixer.Sound(str(script_dir)+'/Save.wav')

#LUT SETUP
lut = np.array(Image.open(str(script_dir)+'/LUT.png')).reshape(-1,3).T.flatten() #read lut from a 256x1 png and make it the right format, then flatten

#CAMERA SETUP & PREVIEW START
camera = picamera.PiCamera(resolution=(1296, 972), framerate=20) #resolution & framerate of preview
camera.start_preview() #start preview

#START THE LOOP
while True:
    #HUD 1: VIEWFINDER
    hud1 = Image.open(str(script_dir)+'/HUD1.png') #load the image
    pad1 = Image.new('RGBA', ( #create an image padded to the required size with RGBA mode
        ((hud1.size[0] + 31) // 32) * 32,
        ((hud1.size[1] + 15) // 16) * 16,
        ))
    pad1.paste(hud1, (0, 0)) #paste the original image into the padded one
    o1 = camera.add_overlay(pad1.tobytes(), size=hud1.size) #add the overlay with the padded image as the source, but the original image's dimensions
    o1.layer = 3 #move overlay above camera preview layer (which is layer 2 by default)

    #CREATING A BYTESTREAM TO WRITE THE IMAGE TO
    stream = io.BytesIO()

#CAN SOMEONE RELEASE THE SHUTTER ALREADY?
#-------------------------------------------------------------------------------------------------------------------------------------------------
    #BUTTON PUSH
    prev_input = 1 #initialise a previous input variable to 1 (assume button not pressed last)
    button_press_count = 0 #initialize button press count variable
    while True:
        input = GPIO.input(40) #take a reading
        if ((not prev_input) and input): #if the last reading was low and this one high, then:

            button_press_count += 1 #increment button press count
            if button_press_count == 1:
                #PRINT THAT THE SHUTTER HAS BEEN RELEASED
                print("shutter released") #print success message
    
                #PLAY SHUTTER SOUND
                shuttersound.play() #play the shutter sound
                print("played shutter sound") #print success message
    
                #TAKE PHOTO
                camera.capture(stream, format='jpeg') #take the photo
                print("took photo") #print success message
    
                #READ PHOTO
                stream.seek(0) #set bytestream pointer to start of stream (for reading it)
                photo = Image.open(stream) #open image from stream

                #APPLY LUT
                photo = photo.convert('L') ; photo = photo.convert('RGB') #convert to greyscale and make it RGB again, so it has 3 channels
                photo = photo.point(lut) #use the lut on the image
    
                #CREATE BORDER
                border_size = 70 #set border size
                photo = ImageOps.expand(photo, border=border_size, fill=(200, 200, 200)) #set size & color and generate the border
                print("applied effect") #print success message
    
                #FRAME THE PHOTO TO MAKE IT WORK AS A HUD
                preview = photo.resize((754, 584)) #resize
                framedpreview = Image.new("RGBA", (1296, 972), (0, 0, 0, 0)) #create transparent frame
                framedpreview.paste(preview, (271, 65)) #paste photo in upper half of frame
    
                #HUD 2: PHOTO PREVIEW
                hud2 = framedpreview #define the image
                pad2 = Image.new('RGBA', ( #create an image padded to the required size with RGBA mode
                    ((hud2.size[0] + 31) // 32) * 32,
                    ((hud2.size[1] + 15) // 16) * 16,
                    ))
                pad2.paste(hud2, (0, 0)) #paste the original image into the padded one
                o2 = camera.add_overlay(pad2.tobytes(), size=hud2.size) #add the overlay with the padded image as the source, but the original image's dimensions
                o2.layer = 3 #move overlay above camera preview layer (which is layer 2 by default)
                camera.remove_overlay(o1) #remove the old overlay
                o1 = o2 #update o to the new overlay
    
                #HUD 3: TEXT BOX
                hud3 = Image.open(str(script_dir)+'/HUD3.png') #load the image
                pad3 = Image.new('RGBA', ( #create an image padded to the required size with RGBA mode
                    ((hud3.size[0] + 31) // 32) * 32,
                    ((hud3.size[1] + 15) // 16) * 16,
                    ))
                pad3.paste(hud3, (0, 0)) #paste the original image into the padded one
                o3 = camera.add_overlay(pad3.tobytes(), size=hud3.size) #add the overlay with the padded image as the source, but the original image's dimensions
                o3.layer = 4 #move overlay above camera preview layer (which is layer 2 by default)
                
                print("showed preview") #print success message
    
            elif button_press_count == 2:
                
                #PRINT THAT THE BUTTON HAS BEEN PUSHED AGAIN
                print("second button push") #print success message
    
                #PLAY SAVE SOUND
                savesound.play() #play the save sound
                print("played save sound") #print success message
                camera.remove_overlay(o2) #remove preview
                camera.remove_overlay(o3) #remove text box
                button_press_count = 0 # reset button press count to 0
                
                #SAVE THE PICTURE
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") #create a timestamp
                photo.save(str(script_dir)+"/1Album/"+timestamp+".jpg") #save photo with timestamp as name in album
                
                print("saved photo") #print success message
                
                break # exit the inner while loop
  
        #END OF BUTT(ON PUSH) STUFF
        prev_input = input #update previous input variable
        time.sleep(0.05) #slight pause to debounce
#--------------------------------------------------------------------------------------------------------------------------------------------------