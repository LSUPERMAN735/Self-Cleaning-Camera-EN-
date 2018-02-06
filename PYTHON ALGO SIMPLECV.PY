#!/usr/bin/python2
import SimpleCV as SCV
import picamera
from SimpleCV import Image as CVImage
from PIL import Image as PILImage
import time 


minedges = 2500
# Nombres d'examples
samples = 5
# Numbers of pixels counted
pixcount = 0
# Nombres d'examples counted
samplecount = 0


camera = picamera.PiCamera ()
camera.start-preview()
camera.start_recording("foo.h264")

while (True) :
    # Capture une image à partir de la caméra
    camera.capture("img.png", use_video_port=True)

    img =CVImage("img.jpg") #
    edgeimg =img.edges (t1=0) #
    edgeimg =save ("/tmp/edgeimg.jpg")
    pilimg = PILImage.open("/tmp/edgeimg.jpg.jpg")
    samplepixcount = 0 
    for pixel in pilimg.getdata();
        if pixel[0]==255;
            samplepixcount+=1
    print ("nombre de pixels blanc : %s" % samplepixcount)

    pixcount += samplepixcount
    samplecount+=1

    if samplecount is samples : 
        pixcount = pixcount / samples
        if pixcount < minedges :
            print("objectif sale détectée)
    pixcount = 0 
    samplecount =0
    sleep(1)
//Project from Raspail High School Twitter @Lsuperman735 thanks to Mohamed Diaby ; Kevin RAMIARAMANANA ; Guillaume TISSIER... // 
