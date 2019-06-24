import time
import cv2
import mss
import numpy
from PIL import ImageGrab
from grabscreen import grab_screen
from boxfinder import full_box

# title of our window
title = "FPS benchmark"
# set start time to current time
start_time = time.time()
# displays the frame rate every 2 second
display_time = 2
# Set primarry FPS to 0
fps = 0
# Load mss library as sct
sct = mss.mss()
x=full_box()
# Set monitor size to capture to MSS
monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
# Set monitor size to capture
mon = x

def screen_grab():
    global fps, start_time
    while True:
        # Get raw pixels from the screen 
        img = grab_screen(region=mon)
        # Display the picture
        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        fps+=1
        TIME = time.time() - start_time
        if (TIME) >= display_time :
            print("FPS: ", fps / (TIME))
            fps = 0
            start_time = time.time()
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

def screen_recordPIL():
    # set variables as global, that we could change them
    global fps, start_time
    # begin our loop
    while True:
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.asarray(ImageGrab.grab(bbox=mon))
        # Display the picture
        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # add one to fps
        fps+=1
        # calculate time difference
        TIME = time.time() - start_time
        # check if our 2 seconds passed
        if (TIME) >= display_time :
            print("FPS: ", fps / (TIME))
            # set fps again to zero
            fps = 0
            # set start time to current time again
            start_time = time.time()
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

def screen_grab():
    global fps, start_time
    while True:
        # Get raw pixels from the screen 
        img = grab_screen(region=(1,100,415,375))
        # Display the picture
        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        fps+=1
        TIME = time.time() - start_time
        if (TIME) >= display_time :
            print("FPS: ", fps / (TIME))
            fps = 0
            start_time = time.time()
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

def screen_recordMSS():
    global fps, start_time
    while True:
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        # to get real color we do this:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        fps+=1
        TIME = time.time() - start_time
        if (TIME) >= display_time :
            print("FPS: ", fps / (TIME))
            fps = 0
            start_time = time.time()
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

#screen_recordMSS()   #Fastest
#screen_recordPIL()  #sloww waste!
#screen_grab()       #slower by 0.01 fps
