# Pictograph-Box
Python-Software for a Raspberry Pi with camera to emulate the camera from the Legend of Zelda - Majora's Mask.
I am a videographer/photographer and no programmer.
I built a life size model of the pictograph box from wood and 3D-printed parts.
3D models are also available.

# Here's a list of bash commands for repositories/programs that might be needed ('cause I did):
you have to install some python addons and use python3.

make a folder with all files and in that make another folder called "1Album". your photos will be saved here.

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
