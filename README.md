# Pictograph-Box
Python-Software for a Raspberry Pi with camera to emulate the camera from the Legend of Zelda - Majora's Mask.
I am a videographer/photographer and no programmer.
I built a life size model of the pictograph box from wood and 3D-printed parts. I will provide all the 3D models once the project is done, too.
I got stuck trying to apply a custom color map to a picture.
I looked into a lot of resources but they all failed to describe to me how to do it.
I tried command line image processing too, but it is slow and doesn't have the right tools.
Please help me :(


# I want the program to do the following:
Show a live picture from the camera with the viewfinder from the game (I re-made this in a decent resolution). DONE
Take a photo when I press an IO-button. DONE
EITHER save the photo to a temp folder to apply an effect OR apply the effect before saving in temp folder. DONE
Apply the effect (I made a colormap, but I can't apply it).
Overlay the photo (with a white border) and a text box (I re-made it from the game) over the live picture.
Press the button once again to save the photo to an album folder and reset the program.

# Resources I found for custom color maps:

https://pythonexamples.org/python-opencv/
https://learnopencv.com/applycolormap-for-pseudocoloring-in-opencv-c-python/
https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/
https://github.com/yoonsikp/pycubelut
https://github.com/prepkg/opencv-raspberrypi
https://raw.githubusercontent.com/spmallick/learnopencv/master/Colormap/custom_colormap.py
https://github.com/KerryHalupka/custom_colormap/blob/master/generate_colormap.py
https://matplotlib.org/stable/tutorials/colors/colormaps.html

# Here's a list of bash commands for repositories/programs that might be needed ('cause I did):
you have to install some python addons and use python3.

pip install numpy
pip install opencv-python

if pip tries to install in an older version of python do this:

Check executables (optional):

$ python2 --version
Python 2.7.10
$ python3 --version
Python 3.6.4
Download the installer script:

$ wget https://bootstrap.pypa.io/get-pip.py
Now, if you want to use pip3 as pip, you need to install pip2 first, which I recommend.

Install pip2:

$ sudo python2 get-pip.py
Finally, install pip3:

$ sudo python3 get-pip.py
Now, check their versions:

$ pip2 --version
pip 18.0 from /Library/Python/2.7/site-packages/pip (python 2.7)
$ pip3 --version
pip 18.0 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
$ pip --version
pip 18.0 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
As you see now we have both, and the default pip points to Python 3.6 installation.

if opencv shows an error about missing paths install the following dependencies:

sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
