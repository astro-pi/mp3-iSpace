# All Code Created by <NAME REDACTED>
################################################### Initialisation of Python Modules ##########################################
"""
Import all relevant modules for use
"""
import pygame as p
import os, glob, time, threading, subprocess
from sense_hat import SenseHat
import random
###############################################################################################################################

############################################## Changing the Audio Output and Creating a Pygame Window #########################
"""
Sets the audio to come through the Audio Jack and initialises the Pygame display so that keyboard events can be recorded
"""
os.system("sudo amixer cset numid=3 1")
os.system("sudo amixer cset numid=1 90%")
p.init()
p.display.init()
p.display.set_mode((100,100))
###############################################################################################################################

############################################### List of Variables #############################################################
"""
Initialises all of the variables needed throughout the code
"""
current = 0 #The position in the List of the song currently Playing

start = True #Whether the MP3 Player has just started or has already played a piece of music

nowDisplaying = 0 #The position in the List of the song currently displaying on the screen. This may not be the song currently playing

songPlaying = False #Whether the song is playing or not

volume = 0 #The Volume in terms of how many steps down from the full volume the song is, e.g one key press

leave = False #Whether to exit the main loop of the code

isPause = False #Check to see if the music is currently paused

newVar = None #Used to store the value of the current variable so that the current variable is separate from the display thread

newVar2 = None #""

newVar3 = None #""

newVar4 = None #""

newVar5 = None #""

overTime = 0 #Used to get the change in time from the top of the while loop to the bottom of the while loop

middleTime = 0 #Used to get the current time the song has been playing for

increase = False #Used to control whether the middleTime Variable needs to increase or not

hello = None # Used to store the value of Variables that need to be accessed by both threads so that the value can be used but the variables are not locked for a long time

check2 = None #""

check3 = None #""

check4 = None #""

check5 = None #""

check6 = None #""

check7 = None #""

check8 = None #""

check9 = None #""

check10 = None #""

check11 = None #""

check12 = None #""

check13 = 0 #""

check14 = None #""

check15 = None #""

check16 = None #""

check17 = None #""

check18 = None #""

check19 = None #""

check20 = None #""

check21 = None #""

helpCheck1 = None #""

isPlay = False #Checks whether the play symbol should be shown

canPause = False #Checks whether the pause symbol should be shown

isNextTrack = False #Checks whether the next track symbol should be shown

isPreviousTrack = False #Checks whether the previous track symbol should be shown

whatSound1 = False #Checks whether the no sound symbol should be shown

whatSound2 = False #Checks whether the low sound symbol should be shown

whatSound3 = False #Checks whether the medium sound symbol should be shown

whatSound4 = False #Checks whether the high sound symbol should be shown

placeHolder = None #A list of words in the song title

listWords = [] #Used to store the song title

pitch = 0 #Used to store the value of pitch

roll = 0 #Used to store the value of roll

yaw = 0 #Used to store the value of yaw

isOrientation = False #Checks whether the orientation is locked or unlocked

canOrientation1 = False #Checks whether the orientation symbol should show locked 

canOrientation2 = False #Checks whether the orientation symbol should show unlocked

music = None #Is the variable where the subprocess to omxplayer is opened

showName = True #Checks whether the display should show the name of the song

showHelp = False #Checks whether the display should show the help menu

angle = 270 #Stores the angle of the Raspberry Pi

checkAngle = 270 #Is used to check to see whether the angle has moved to a different quadrant of the circle

xAxis = 0 #Stores the x axis value of the accelerometer

yAxis = 0 #Stores the y axis value of the accelerometer

zAxis = 0 #Stores the z axis value of the accelerometer

shakeTime = 0 #Stores the cooldown time for the shake to shuffle function

isShake = True #Checks whether the device is allowed to recieve shake input

randomNumber = 0 #Stores a random number in the range of the number of songs on the device

temperature = None #Stores the temperature in degrees

backgroundColour = [0,0,255] #Stores the background colour for the display text which changes depending on the temperature

checkRewind = None #Checks to see if the rewind symbol should be shown on the help menu

checkFastForward = None #Checks to see if the FastForward symbol should be shown on the help menu

checkScrollUp = None #checks to see if the up scroll button should be seen on the help menu

checkScrollDown = None #checks to see if the down scroll button should be seen on the help menu

c = [0,0,0] #colourless colour

r = [255,0,0] #red colour

g = [0,255,0] #green colour

b = [0,0,255] #blue colour

playButton = [
	c,c,c,c,c,c,c,c,
	c,c,g,c,c,c,c,c,
	c,c,g,g,c,c,c,c,
	c,c,g,g,g,c,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,c,c,c,
	c,c,g,g,c,c,c,c,
	c,c,g,c,c,c,c,c
]

pauseButton = [
	c,c,c,c,c,c,c,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c,
	c,g,g,c,c,g,g,c
]

infoButton = [
	c,c,c,g,g,c,c,c,
	c,c,c,g,g,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,g,g,c,c,c,
	c,c,c,g,g,c,c,c,
	c,c,c,g,g,c,c,c,
	c,c,c,g,g,c,c,c
]

lockedButton = [
	c,c,c,c,c,c,c,c,
	c,c,c,g,g,c,c,c,
	c,c,g,c,c,g,c,c,
	c,c,g,c,c,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c
]

unlockedButton = [
	c,c,c,g,g,c,c,c,
	c,c,g,c,c,g,c,c,
	c,c,c,c,c,g,c,c,
	c,c,c,c,c,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c,
	c,c,g,g,g,g,c,c
]

nextTrackButton = [
	c,c,c,c,c,c,c,c,
	c,g,c,c,g,c,c,c,
	c,c,g,c,c,g,c,c,
	c,c,c,g,c,c,g,c,
	c,c,c,c,g,c,c,g,
	c,c,c,g,c,c,g,c,
	c,c,g,c,c,g,c,c,
	c,g,c,c,g,c,c,c
]

previousTrackButton = [
	c,c,c,c,c,c,c,c,
	c,c,c,g,c,c,g,c,
	c,c,g,c,c,g,c,c,
	c,g,c,c,g,c,c,c,
	g,c,c,g,c,c,c,c,
	c,g,c,c,g,c,c,c,
	c,c,g,c,c,g,c,c,
	c,c,c,g,c,c,g,c
]

rewindButton = [
	c,c,c,c,c,c,c,c,
	c,c,c,g,c,c,c,c,
	c,c,g,c,c,c,c,c,
	c,g,c,c,c,c,c,c,
	g,c,c,c,c,c,c,c,
	c,g,c,c,c,c,c,c,
	c,c,g,c,c,c,c,c,
	c,c,c,g,c,c,c,c
] 

fastForwardButton = [
	c,c,c,c,c,c,c,c,
	c,c,c,c,g,c,c,c,
	c,c,c,c,c,g,c,c,
	c,c,c,c,c,c,g,c,
	c,c,c,c,c,c,c,g,
	c,c,c,c,c,c,g,c,
	c,c,c,c,c,g,c,c,
	c,c,c,c,g,c,c,c
]

scrollDownButton = [
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,g,c,c,c,c,c,g,
	c,c,g,c,c,c,g,c,
	c,c,c,g,c,g,c,c,
	c,c,c,c,g,c,c,c
]

scrollUpButton = [
	c,c,c,c,g,c,c,c,
	c,c,c,g,c,g,c,c,
	c,c,g,c,c,c,g,c,
	c,g,c,c,c,c,c,g,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c
]

noSoundButton = [
	c,c,c,g,c,c,c,c,
	c,c,g,g,c,c,c,c,
	g,g,g,g,c,c,c,c,
	g,g,g,g,c,c,c,c,
	g,g,g,g,c,c,c,c,
	g,g,g,g,c,c,c,c,
	c,c,g,g,c,c,c,c,
	c,c,c,g,c,c,c,c
]

lowSoundButton = [
	c,c,c,g,c,c,c,c,
	c,c,g,g,c,c,c,c,
	g,g,g,g,r,c,c,c,
	g,g,g,g,r,c,c,c,
	g,g,g,g,r,c,c,c,
	g,g,g,g,r,c,c,c,
	c,c,g,g,c,c,c,c,
	c,c,c,g,c,c,c,c
]

mediumSoundButton = [
	c,c,c,g,c,c,c,c,
	c,c,g,g,c,b,c,c,
	g,g,g,g,r,b,c,c,
	g,g,g,g,r,b,c,c,
	g,g,g,g,r,b,c,c,
	g,g,g,g,r,b,c,c,
	c,c,g,g,c,b,c,c,
	c,c,c,g,c,c,c,c
]

highSoundButton = [
	c,c,c,g,c,c,g,c,
	c,c,g,g,c,b,g,c,
	g,g,g,g,r,b,g,c,
	g,g,g,g,r,b,g,c,
	g,g,g,g,r,b,g,c,
	g,g,g,g,r,b,g,c,
	c,c,g,g,c,b,g,c,
	c,c,c,g,c,c,g,c
]

"""
Sets the pixels that are needed to make up the numbers for the time display, the seconds bar and the letters for the loading screen
"""

number01 = [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(2,2),(0,3),(2,3),(0,4),(2,4),(1,4)]
number11 = [(2,0),(2,1),(2,2),(2,3),(2,4)]
number21 = [(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(0,4),(1,4),(2,4)]
number31 = [(0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(2,3),(2,4),(1,4),(0,4)]
number41 = [(0,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2),(2,3),(2,4)]
number51 = [(2,0),(1,0),(0,0),(0,1),(0,2),(1,2),(2,2),(2,3),(2,4),(1,4),(0,4)]
number61 = [(2,0),(1,0),(0,0),(0,1),(0,2),(1,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)]
number71 = [(0,0),(1,0),(2,0),(2,1),(2,2),(2,3),(2,4)]
number81 = [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)]
number91 = [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2),(2,3),(2,4)]

number02 = [(4,0),(5,0),(6,0),(4,1),(6,1),(4,2),(6,2),(4,3),(6,3),(4,4),(6,4),(5,4)]
number12 = [(6,0),(6,1),(6,2),(6,3),(6,4)]
number22 = [(4,0),(5,0),(6,0),(6,1),(6,2),(5,2),(4,2),(4,3),(4,4),(5,4),(6,4)]
number32 = [(4,0),(5,0),(6,0),(6,1),(6,2),(5,2),(4,2),(6,3),(6,4),(5,4),(4,4)]
number42 = [(4,0),(6,0),(4,1),(6,1),(4,2),(5,2),(6,2),(6,3),(6,4)]
number52 = [(6,0),(5,0),(4,0),(4,1),(4,2),(5,2),(6,2),(6,3),(6,4),(5,4),(4,4)]
number62 = [(6,0),(5,0),(4,0),(4,1),(4,2),(5,2),(6,2),(4,3),(6,3),(4,4),(5,4),(6,4)]
number72 = [(4,0),(5,0),(6,0),(6,1),(6,2),(6,3),(6,4)]
number82 = [(4,0),(5,0),(6,0),(4,1),(6,1),(4,2),(5,2),(6,2),(4,3),(6,3),(4,4),(5,4),(6,4)]
number92 = [(4,0),(5,0),(6,0),(4,1),(6,1),(4,2),(5,2),(6,2),(6,3),(6,4)]

secondBar0 = [(1,5),(2,5),(3,5),(4,5),(5,5),(1,6),(2,6),(3,6),(4,6),(5,6),(1,7),(2,7),(3,7),(4,7),(5,7)]
secondBar1 = [(1,5),(1,6),(1,7)]
secondBar2 = [(2,5),(2,6),(2,7)]
secondBar3 = [(3,5),(3,6),(3,7)]
secondBar4 = [(4,5),(4,6),(4,7)]
secondBar5 = [(5,5),(5,6),(5,7)]

letterM = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(2,2),(3,1),(4,0),(4,1),(4,2),(4,3),(4,4)]
letterP = [(5,0),(5,1),(5,2),(5,3),(5,4),(6,0),(6,2),(7,0),(7,1),(7,2)]

loadingBar1 = [(0,6),(0,7)]
loadingBar2 = [(1,6),(1,7)]
loadingBar3 = [(2,6),(2,7)]
loadingBar4 = [(3,6),(3,7)]
loadingBar5 = [(4,6),(4,7)]
loadingBar6 = [(5,6),(5,7)]
loadingBar7 = [(6,6),(6,7)]
loadingBar8 = [(7,6),(7,7)]

sense = SenseHat() # Initialises the sense hat module

lock = threading.RLock() #Creates a lock to be able to allow both threads to change global variables with out causing problems. One lock for each shared variable so that the variables also don't interfere with each other

lock1 = threading.RLock() #""

lock2 = threading.RLock() #""

lock3 = threading.RLock() #""

lock4 = threading.RLock() #""

lock5 = threading.RLock() #""

lock6 = threading.RLock() #""

lock7 = threading.RLock() #""

lock8 = threading.RLock() #""

lock9 = threading.RLock() #""

lock10 = threading.RLock() #""

lock11 = threading.RLock() #""

lock12 = threading.RLock() #""

lock13 = threading.RLock() #""

lock14 = threading.RLock() #""

lock15 = threading.RLock() #""

lock16 = threading.RLock() #""

lock17 = threading.RLock() #""

lock18 = threading.RLock() #""

lock19 = threading.RLock() #""

lock20 = threading.RLock() #""

#################################################################################################################################

######################## Sets the rotation, Displays the start screen and Finds the list of MP3 songs ###########################
"""
Sets the rotation of the screen to the correct position, Creates the start screen which consists of my Initials MP, and also finds
the songs and their file paths in the correct folder
"""
sense.set_rotation(270)

for x in letterM:
	sense.set_pixel(x[0],x[1],255,0,0)
for y in letterP:
	sense.set_pixel(y[0],y[1],0,0,255)
	
List = glob.glob("/boot/mp3/*.mp3")

#################################################################################################################################

################################################### Secondary Display Thread ####################################################
"""
Function getSong takes the current song's filepath and splits it into the name of the song only. It then returns this name, which
is further split into the individual words of the name. If no songs are on the device, it will say so and then quit the program
"""
def getSong(x):
	global List
	global listWords
	try:
		display1 = List[x].split("/")
		display = display1[(len(display1) - 1)].split(".", 1)[0]
		listWords = display.split()
		return listWords
	except:
		display = "No Songs are on This Device"
		listWords = display.split()
		return listWords
		check2 = True
"""
Function showNumber shows the number of the song currently selected
"""
def showNumber(x):
	global sense
	sense.show_letter(str(x + 1))
	time.sleep(1.5)
"""
Function loading displays the loading bars of the start screen with a time delay between each bar
"""
def loading():
	global loadingBar1
	global loadingBar2
	global loadingBar3
	global loadingBar4
	global loadingBar5
	global loadingBar6
	global loadingBar7
	global loadingBar8
	for x in loadingBar1:
		sense.set_pixel(x[0],x[1],255,0,0)
	time.sleep(0.5)
	for x in loadingBar2:
		sense.set_pixel(x[0],x[1],255,165,0)
	time.sleep(0.5)
	for x in loadingBar3:
		sense.set_pixel(x[0],x[1],255,255,0)
	time.sleep(0.5)
	for x in loadingBar4:
		sense.set_pixel(x[0],x[1],124,252,0)
	time.sleep(0.5)
	for x in loadingBar5:
		sense.set_pixel(x[0],x[1],0,128,0)
	time.sleep(0.5)
	for x in loadingBar6:
		sense.set_pixel(x[0],x[1],0,255,127)
	time.sleep(0.5)
	for x in loadingBar7:
		sense.set_pixel(x[0],x[1],0,255,255)
	time.sleep(0.5)
	for x in loadingBar8:
		sense.set_pixel(x[0],x[1],0,0,255)
	time.sleep(0.5)
"""
Function setTime1 takes the current time of the song and displays it in minutes at the top of the display and
every ten seconds a bar increases along the bottom of the display
"""
def setTime1(Time):
	global number01
	global number11
	global number21
	global number31
	global number41
	global number51
	global number61
	global number71
	global number81
	global number91
	global number02
	global number12
	global number22
	global number32
	global number42
	global number52
	global number62
	global number72
	global number82
	global number92
	global secondBar0
	global secondBar1
	global secondBar2
	global secondBar3
	global secondBar4
	global secondBar5
	global sense
	minute = int(Time / 60)
	if minute < 10:
		minute = "0" + str(minute)
	else:
		minute = str(minute)
	if (int(Time / 60)) >= 1:  
		stringTime1 = Time - (60*int(Time / 60))
	else:
		stringTime1 = Time
	sense.clear()
	for y in range(10):
		if minute[0] == str(y):
                        if y == 0:
                                for k in number01:
                                        sense.set_pixel(k[0],k[1],75,0,130)
                        elif y == 1:
                                for k in number11:
                                        sense.set_pixel(k[0],k[1],0,0,255)
                        elif y == 2:
                                for k in number21:
                                        sense.set_pixel(k[0],k[1],0,255,255)
                        elif y == 3:
                                for k in number31:
                                        sense.set_pixel(k[0],k[1],0,255,127)
                        elif y == 4:
                                for k in number41:
                                        sense.set_pixel(k[0],k[1],0,128,0)
                        elif y == 5:
                                for k in number51:
                                        sense.set_pixel(k[0],k[1],124,252,0)
                        elif y == 6:
                                for k in number61:
                                        sense.set_pixel(k[0],k[1],255,255,0)
                        elif y == 7:
                                for k in number71:
                                        sense.set_pixel(k[0],k[1],255,165,0)
                        elif y == 8:
                                for k in number81:
                                        sense.set_pixel(k[0],k[1],250,128,114)
                        elif y == 9:
                                for k in number91:
                                        sense.set_pixel(k[0],k[1],255,0,0)
				
		if minute[1] == str(y):
                        if y == 0:
                                for k in number02:
                                        sense.set_pixel(k[0],k[1],255,0,0)
                        elif y == 1:
                                for k in number12:
                                        sense.set_pixel(k[0],k[1],250,128,114)
                        elif y == 2:
                                for k in number22:
                                        sense.set_pixel(k[0],k[1],255,165,0)
                        elif y == 3:
                                for k in number32:
                                        sense.set_pixel(k[0],k[1],255,255,0)
                        elif y == 4:
                                for k in number42:
                                        sense.set_pixel(k[0],k[1],124,252,0)
                        elif y == 5:
                                for k in number52:
                                        sense.set_pixel(k[0],k[1],0,128,0)
                        elif y == 6:
                                for k in number62:
                                        sense.set_pixel(k[0],k[1],0,255,127)
                        elif y == 7:
                                for k in number72:
                                        sense.set_pixel(k[0],k[1],0,255,255)
                        elif y == 8:
                                for k in number82:
                                        sense.set_pixel(k[0],k[1],0,0,255)
                        elif y == 9:
                                for k in number92:
                                        sense.set_pixel(k[0],k[1],75,0,130)
				
	forTenSeconds = int((stringTime1 / 10))
	for l in range(6):
                if forTenSeconds == l:
                        if l == 0:
                                for m in secondBar0:
                                        sense.set_pixel(m[0],m[1],0,0,0)
                        elif l == 1:
                                for m in secondBar1:
                                        sense.set_pixel(m[0],m[1],255,0,0)
                        elif l == 2:
                                for m in secondBar1:
                                        sense.set_pixel(m[0],m[1],255,0,0)
                                for m in secondBar2:
                                        sense.set_pixel(m[0],m[1],255,255,0)
                        elif l == 3:
                                for m in secondBar1:
                                        sense.set_pixel(m[0],m[1],255,0,0)
                                for m in secondBar2:
                                        sense.set_pixel(m[0],m[1],255,255,0)
                                for m in secondBar3:
                                        sense.set_pixel(m[0],m[1],0,255,0)
                        elif l == 4:
                                for m in secondBar1:
                                        sense.set_pixel(m[0],m[1],255,0,0)
                                for m in secondBar2:
                                        sense.set_pixel(m[0],m[1],255,255,0)
                                for m in secondBar3:
                                        sense.set_pixel(m[0],m[1],0,255,0)
                                for m in secondBar4:
                                        sense.set_pixel(m[0],m[1],0,255,255)
                        elif l == 5:
                                for m in secondBar1:
                                        sense.set_pixel(m[0],m[1],255,0,0)
                                for m in secondBar2:
                                        sense.set_pixel(m[0],m[1],255,255,0)
                                for m in secondBar3:
                                        sense.set_pixel(m[0],m[1],0,255,0)
                                for m in secondBar4:
                                        sense.set_pixel(m[0],m[1],0,255,255)
                                for m in secondBar5:
                                        sense.set_pixel(m[0],m[1],0,0,255)
"""
Function display is the main function of the display thread and is responsible for checking to see whether the help, time or name
screens should be shown on the sensehat display. It also checks to see whether any symbols need to be displayed on the screen.
"""
def display():
	global nowDisplaying
	global lock
	global lock1
	global lock2
	global hello
	global check2
	global leave
	global sense
	global check3
	global isPlay
	global playButton
	global pauseButton
	global check4
	global canPause
	global isNextTrack
	global lock4
	global check5
	global nextTrackButton
	global isPreviousTrack
	global lock5
	global check6
	global previousTrackButton
	global lock6
	global lock7
	global lock8
	global lock9
	global lock10
	global check7
	global check8
	global check9
	global check10
	global check11
	global check12
	global check13
	global whatSound1
	global whatSound2
	global whatSound3
	global whatSound4
	global noSoundButton
	global lowSoundButton
	global mediumSoundButton
	global highSoundButton
	global placeHolder
	global showName
	global middleTime
	global lock11
	global lock12
	global angle
	global checkAngle
	global check14
	global showHelp
	global lock13
	global infoButton
	global check15
	global check16
	global lock14
	global lock15
	global lockedButton
	global unlockedButton
	global canOrientation1
	global canOrientation2
	global backgroundColour
	global lock16
	global check17
	global check18
	global check19
	global lock17
	global lock18
	global checkScrollUp
	global checkScrollDown
	global scrollUpButton
	global scrollDownButton
	global lock19
	global check20
	global checkRewind
	global rewindButton
	global lock20
	global check21
	global checkFastForward
	global fastForwardButton
	loading()
	lock.acquire()
	check = nowDisplaying
	lock.release()
	showNumber(check)
	check2 = False
	hello = check
	while check2 == False:
		lock10.acquire()
		check11 = showName
		lock10.release()
		lock13.acquire()
		check14 = showHelp
		lock13.release()
		if check11 == True and check14 == False:
			lock12.acquire()
			if angle != checkAngle:
				sense.set_rotation(angle)
				checkAngle = angle
			lock12.release()
			lock4.acquire()
			check5 = isNextTrack
			lock4.release()
			if check5 == True:
				sense.set_pixels(nextTrackButton)
				time.sleep(0.5)
				lock4.acquire()
				isNextTrack = False
				lock4.release()
			lock5.acquire()
			check6 = isPreviousTrack
			lock5.release()
			if check6 == True:
				sense.set_pixels(previousTrackButton)
				time.sleep(0.5)
				lock5.acquire()
				isPreviousTrack = False
				lock5.release()
			lock.acquire()
			hello = nowDisplaying
			lock.release()
			if hello != check:
				showNumber(hello)
				check = hello
			placeholder = getSong(hello)
			for word in placeholder:
				lock12.acquire()
				if angle != checkAngle:
					sense.set_rotation(angle)
					checkAngle = angle
				lock12.release()
				lock16.acquire()
				check17 = backgroundColour
				lock16.release()
				sense.show_message(str(word), text_colour = check17, scroll_speed = 0.05)
				lock4.acquire()
				check5 = isNextTrack
				lock4.release()
				if check5 == True:
					sense.set_pixels(nextTrackButton)
					time.sleep(0.5)
					lock4.acquire()
					isNextTrack = False
					lock4.release()
				lock5.acquire()
				check6 = isPreviousTrack
				lock5.release()
				if check6 == True:
					sense.set_pixels(previousTrackButton)
					time.sleep(0.5)
					lock5.acquire()
					isPreviousTrack = False
					lock5.release()
				lock.acquire()
				hello = nowDisplaying
				lock.release()
				if hello != check:
					showNumber(hello)
					check = hello
					break
				lock2.acquire()
				check3 = isPlay
				lock2.release()
				if check3 == True:
					sense.set_pixels(playButton)
					time.sleep(0.5)
					lock2.acquire()
					isPlay = False
					lock2.release()
				lock3.acquire()
				check4 = canPause
				lock3.release()
				if check4 == True:
					sense.set_pixels(pauseButton)
					time.sleep(0.5)
					lock3.acquire()
					canPause = False
					lock3.release()
				lock6.acquire()
				check7 = whatSound1
				lock6.release()
				if check7 == True:
					sense.set_pixels(noSoundButton)
					time.sleep(0.5)
					lock6.acquire()
					whatSound1 = False
					lock6.release()
				lock7.acquire()
				check8 = whatSound2
				lock7.release()
				if check8 == True:
					sense.set_pixels(lowSoundButton)
					time.sleep(0.5)
					lock7.acquire()
					whatSound2 = False
					lock7.release()
				lock8.acquire()
				check9 = whatSound3
				lock8.release()
				if check9 == True:
					sense.set_pixels(mediumSoundButton)
					time.sleep(0.5)
					lock8.acquire()
					whatSound3 = False
					lock8.release()
				lock9.acquire()
				check10 = whatSound4
				lock9.release()
				if check10 == True:
					sense.set_pixels(highSoundButton)
					time.sleep(0.5)
					lock9.acquire()
					whatSound4 = False
					lock9.release()
				lock14.acquire()
				check15 = canOrientation1
				lock14.release()
				if check15 == True:
					sense.set_pixels(lockedButton)
					time.sleep(0.5)
					lock14.acquire()
					canOrientation1 = False
					lock14.release()
				lock15.acquire()
				check16 = canOrientation2
				lock15.release()
				if check16 == True:
					sense.set_pixels(unlockedButton)
					time.sleep(0.5)
					lock15.acquire()
					canOrientation2 = False
					lock15.release()
				lock10.acquire()
				check11 = showName
				lock10.release()
				if check11 == False:
					lock13.acquire()
					check14 = showHelp
					lock13.release()
					if check14 == True:
						sense.set_pixels(infoButton)
					else:
						lock11.acquire()
						check12 = middleTime
						lock11.release()
						setTime1(check12)
					break
				lock1.acquire()
				check2 = leave
				lock1.release()
				if check2 == True:
					break
		
		
		elif check14 == True and check11 == False:
			lock12.acquire()
			if angle != checkAngle:
				sense.set_rotation(angle)
				checkAngle = angle
			lock12.release()
			sense.set_pixels(infoButton)
			lock4.acquire()
			check5 = isNextTrack
			lock4.release()
			if check5 == True:
				sense.set_pixels(nextTrackButton)
				time.sleep(0.5)
				sense.show_message("Next Track Button", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock4.acquire()
				isNextTrack = False
				lock4.release()
			lock5.acquire()
			check6 = isPreviousTrack
			lock5.release()
			if check6 == True:
				sense.set_pixels(previousTrackButton)
				time.sleep(0.5)
				sense.show_message("Previous Track Button", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock5.acquire()
				isPreviousTrack = False
				lock5.release()
			lock2.acquire()
			check3 = isPlay
			lock2.release()
			if check3 == True:
				sense.set_pixels(playButton)
				time.sleep(0.5)
				sense.set_pixels(pauseButton)
				time.sleep(0.5)
				sense.show_message("Play/Pause Button", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock2.acquire()
				isPlay = False
				lock2.release()
			lock6.acquire()
			check7 = whatSound1
			lock6.release()
			if check7 == True:
				sense.set_pixels(noSoundButton)
				time.sleep(0.5)
				sense.show_message("Decrease Volume", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock6.acquire()
				whatSound1 = False
				lock6.release()
			lock9.acquire()
			check10 = whatSound4
			lock9.release()
			if check10 == True:
				sense.set_pixels(highSoundButton)
				time.sleep(0.5)
				sense.show_message("Increase Volume", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock9.acquire()
				whatSound4 = False
				lock9.release()
			lock14.acquire()
			check15 = canOrientation1
			lock14.release()
			if check15 == True:
				sense.set_pixels(lockedButton)
				time.sleep(0.5)
				sense.show_message("Orientation Lock", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock14.acquire()
				canOrientation1 = False
				lock14.release()
			lock15.acquire()
			check16 = canOrientation2
			lock15.release()
			if check16 == True:
				sense.set_pixels(unlockedButton)
				time.sleep(0.5)
				sense.show_message("Orientation Lock", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock15.acquire()
				canOrientation2 = False
				lock15.release()
			lock17.acquire()
			check18 = checkScrollUp
			lock17.release()
			if check18 == True:
				sense.set_pixels(scrollUpButton)
				time.sleep(0.5)
				sense.show_message("Scroll Up", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock17.acquire()
				checkScrollUp = False
				lock17.release()
			lock18.acquire()
			check19 = checkScrollDown
			lock18.release()
			if check19 == True:
				sense.set_pixels(scrollDownButton)
				time.sleep(0.5)
				sense.show_message("Scroll Down", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock18.acquire()
				checkScrollDown = False
				lock18.release()
			lock19.acquire()
			check20 = checkRewind
			lock19.release()
			if check20 == True:
				sense.set_pixels(rewindButton)
				time.sleep(0.5)
				sense.show_message("Rewind Button", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock19.acquire()
				checkRewind = False
				lock19.release()
			lock20.acquire()
			check21 = checkFastForward
			lock20.release()
			if check21 == True:
				sense.set_pixels(fastForwardButton)
				time.sleep(0.5)
				sense.show_message("FastForward Button", text_colour = [255,0,0], scroll_speed = 0.05)
				sense.set_pixels(infoButton)
				lock20.acquire()
				checkFastForward = False
				lock20.release()
			lock1.acquire()
			check2 = leave
			lock1.release()
			if check2 == True:
				break
		
		
			
		else:
		
			lock12.acquire()
			if angle != checkAngle:
				sense.set_rotation(angle)
				checkAngle = angle
			lock12.release()
			lock11.acquire()
			check12 = middleTime
			lock11.release()
			if int(check12/10) != int(check13/10):
				setTime1(check12)
				check13 = check12
			lock4.acquire()
			check5 = isNextTrack
			lock4.release()
			if check5 == True:
				sense.set_pixels(nextTrackButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock4.acquire()
				isNextTrack = False
				lock4.release()
			lock5.acquire()
			check6 = isPreviousTrack
			lock5.release()
			if check6 == True:
				sense.set_pixels(previousTrackButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock5.acquire()
				isPreviousTrack = False
				lock5.release()
			lock2.acquire()
			check3 = isPlay
			lock2.release()
			if check3 == True:
				sense.set_pixels(playButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock2.acquire()
				isPlay = False
				lock2.release()
			lock3.acquire()
			check4 = canPause
			lock3.release()
			if check4 == True:
				sense.set_pixels(pauseButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock3.acquire()
				canPause = False
				lock3.release()
			lock6.acquire()
			check7 = whatSound1
			lock6.release()
			if check7 == True:
				sense.set_pixels(noSoundButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock6.acquire()
				whatSound1 = False
				lock6.release()
			lock7.acquire()
			check8 = whatSound2
			lock7.release()
			if check8 == True:
				sense.set_pixels(lowSoundButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock7.acquire()
				whatSound2 = False
				lock7.release()
			lock8.acquire()
			check9 = whatSound3
			lock8.release()
			if check9 == True:
				sense.set_pixels(mediumSoundButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock8.acquire()
				whatSound3 = False
				lock8.release()
			lock9.acquire()
			check10 = whatSound4
			lock9.release()
			if check10 == True:
				sense.set_pixels(highSoundButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock9.acquire()
				whatSound4 = False
				lock9.release()
			lock14.acquire()
			check15 = canOrientation1
			lock14.release()
			if check15 == True:
				sense.set_pixels(lockedButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock14.acquire()
				canOrientation1 = False
				lock14.release()
			lock15.acquire()
			check16 = canOrientation2
			lock15.release()
			if check16 == True:
				sense.set_pixels(unlockedButton)
				time.sleep(0.5)
				lock11.acquire()
				check12 = middleTime
				lock11.release()
				setTime1(check12)
				lock15.acquire()
				canOrientation2 = False
				lock15.release()
			lock1.acquire()
			check2 = leave
			lock1.release()
			if check2 == True:
				break
			
	print("The Display has Closed")
	sense.clear()

		
thread = threading.Thread(target = display,) #Creates thread object which will run the display function
thread.start() #Starts the thread object running
###############################################################################################################################

##################################################### Functions for Main Thread ###############################################
"""
Function scroll detects whether the up(which is left to the senshat) and down(which is right for the sensehat) joystick actions have occured and then changes nowDisplaying accordingly so
that the display changes to the currently selected song. 
"""
def scroll(event):
	global List
	global lock
	global nowDisplaying
	global lock13
	global helpCheck1
	global showHelp
	global lock17
	global checkScrollUp
	global lock18
	global checkScrollDown
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_LEFT:
                if helpCheck1 == False:
                        lock.acquire()
                        if nowDisplaying > 0:
                                nowDisplaying -= 1
                        elif nowDisplaying == 0:
                                nowDisplaying = len(List) - 1
                        lock.release()
	elif event.key == p.K_RIGHT:
                if helpCheck1 == False:
                        lock.acquire()
                        if nowDisplaying < len(List) - 1:
                                nowDisplaying += 1
                        elif nowDisplaying == len(List) - 1:
                                nowDisplaying = 0
                        lock.release()
        if event.key == p.K_LEFT and helpCheck1 == True:
                lock17.acquire()
                checkScrollUp = True
                lock17.release()
        elif event.key == p.K_RIGHT and helpCheck1 == True:
                lock18.acquire()
                checkScrollDown = True
                lock18.release()
"""
Function sendKey is used to send the correct input key to the omxplayer subprocess. Letters are encoded with utf-8 and the arrow keys are sent as codes
"""
def sendKey(key):
	global music
	if key == "\x1B[C" or key == "\x1B[D":
		music.stdin.write(key)
		music.stdin.flush()
	else:
		music.stdin.write(key.encode('utf-8'))
		music.stdin.flush()
"""
Function setVolume is used to set the volume of the new omxplayer subprocess to the current volume level set by the user
"""
def setVolume(volume):
        for i in range(volume):
		sendKey("-")
		time.sleep(0.1)
"""
Function nextTrack is used to check whether the right(which is up for the sensehat) joystick action has occured and then
changes the track to the next song in the list 
"""
def nextTrack(event, override):
	global middleTime
	global current
	global volume
	global lock4
	global isNextTrack
	global music
	global lock11
	global showHelp
	global lock13
	global helpCheck1
	global newVar5
	global lock
	global nowDisplaying
	global start
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_UP or override == True:
                if helpCheck1 == False and start == False:
                        if current < (len(List) - 1):
                                sendKey("q")
                                music = subprocess.Popen(["omxplayer", List[current + 1], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                                setVolume(volume)
                                current += 1
                                newVar5 = current
                                lock.acquire()
                                nowDisplaying = newVar5
                                lock.release()
                        else:
                                current = 0
                                sendKey("q")
                                music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                                setVolume(volume)
                                newVar5 = current
                                lock.acquire()
                                nowDisplaying = newVar5
                                lock.release()
                        lock11.acquire()
                        middleTime = 0
                        lock11.release()
                        lock4.acquire()
                        isNextTrack = True
                        lock4.release()
                        increase = True
	if event.key == p.K_UP and helpCheck1 == True:
		lock4.acquire()
		isNextTrack = True
		lock4.release()
		
"""
Function previousTrack is used to detect whether the left(which is down for the sensehat) joystick action has occured and
if so changes the song to the previous song in the list
"""
def previousTrack(event, override):
	global middleTime
	global current
	global volume
	global lock5
	global isPreviousTrack
	global music
	global lock11
	global showHelp
	global lock13
	global helpCheck1
	global nowDisplaying
	global lock
	global newVar5
	global start
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_DOWN or override == True:
                if helpCheck1 == False and start == False:
                        if current == 0:
                                current = (len(List) - 1)
                                sendKey("q")
                                music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                                setVolume(volume)
                                newVar5 = current
                                lock.acquire()
                                nowDisplaying = newVar5
                                lock.release()
                        else:
                                sendKey("q")
                                music = subprocess.Popen(["omxplayer", List[current - 1], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                                setVolume(volume)
                                current -= 1
                                newVar5 = current
                                lock.acquire()
                                nowDisplaying = newVar5
                                lock.release()
                        lock11.acquire()
                        middleTime = 0
                        lock11.release()
                        lock5.acquire()
                        isPreviousTrack = True
                        lock5.release()
                        increase = True
	if event.key == p.K_DOWN and helpCheck1 == True:
		lock5.acquire()
		isPreviousTrack = True
		lock5.release()
"""
Function info is used to detect whether the left button has been either pressed quickly or held down for over one second.
If pressed quicly, this will allow the time of the song to be displayed on the display of the sense hat.
If held down, this will allow the help menu to be displayed on the sense hat display, which will tell you what the buttons do when you press them.
Buttons and joystick will not affect anything while in help mode and will just tell you their function. They will work again once out of help mode.
"""
def info(event):
	global showName
	global showHelp
	global lock10
	global lock13
	if event.key == p.K_l:
		time.sleep(1)
		for event2 in p.event.get():
			if event2.type == p.KEYUP and event2.key == p.K_l:
				lock10.acquire()
				if showName == True:
					showName = False
				elif showName == False:
					showName = True
				lock10.release()
				lock13.acquire()
				showHelp = False
				lock13.release()
				break
		else:
			lock13.acquire()
			showHelp = True
			lock13.release()
			lock10.acquire()
			showName = False
			lock10.release()
"""
Function playPause is used to play and pause the song. If the song is playing, by pressing the right button, the song will pause and vica-versa by sending input to omxplayer.
If the currently selected song is different from that which is actually playing then by pressing the right button, the curently selected song will start playing
"""
def playPause(event):
	global songPlaying
	global List
	global current
	global isPause
	global start
	global lock2
	global isPlay
	global lock3
	global canPause
	global music
	global volume
	global middleTime
	global lock11
	global increase
	global newVar
	global lock13
	global helpCheck1
	global showHelp
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_r and helpCheck1 == False:
		lock.acquire()
		newVar = nowDisplaying
		lock.release()
		if songPlaying == True and isPause == False and start == False and newVar == current:
			sendKey("p")
			lock3.acquire()
			canPause = True
			lock3.release()
			isPause = True
			increase = False
			songPlaying = False
		elif songPlaying == False and isPause == True and newVar == current and start == False:
			sendKey("p")
			lock2.acquire()
			isPlay = True
			lock2.release()
			isPause = False
			increase = True
			songPlaying = True
		elif isPause == False and newVar != current and start == False:
			current = newVar
			sendKey("q")
			music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			setVolume(volume)
			lock2.acquire()
			isPlay = True
			lock2.release()
			lock11.acquire()
			middleTime = 0
			lock11.release()
			increase = True
			songPlaying = True
		elif isPause == True and newVar != current and start == False:
			current = newVar
			sendKey("q")
			music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			setVolume(volume)
			lock2.acquire()
			isPlay = True
			lock2.release()
			lock11.acquire()
			middleTime = 0
			lock11.release()
			isPause = False
			increase = True
			songPlaying = True
		elif isPause == False and start == True and songPlaying == False:
			if newVar != current or newVar == current:
                                current = newVar
                                music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                                lock2.acquire()
                                isPlay = True
                                lock2.release()
                                start = False
                                increase = True
                                songPlaying = True
	elif event.key == p.K_r and helpCheck1 == True:
		lock2.acquire()
		isPlay = True
		lock2.release()
"""
Function decreaseVolume is used to decrease the volume by sending input to omxplayer. This works when the A button is pressed.
"""
def decreaseVolume(event):
	global volume
	global lock6
	global lock7
	global lock8
	global lock9
	global whatSound1
	global whatSound2
	global whatSound3
	global whatSound4
	global showHelp
	global lock13
	global helpCheck1
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_a and volume <= 24 and helpCheck1 == False:
		volume += 1
		sendKey("-")
		if volume == 25:
			lock6.acquire()
			whatSound1 = True
			lock6.release()
		elif volume < 25 and volume > 17:
			lock7.acquire()
			whatSound2 = True
			lock7.release()
		elif volume <= 17 and volume > 9:
			lock8.acquire()
			whatSound3 = True
			lock8.release()
		elif volume <= 9 and volume >= 0:
			lock9.acquire()
			whatSound4 = True
			lock9.release()
	elif event.key == p.K_a and helpCheck1 == True:
		lock6.acquire()
		whatSound1 = True
		lock6.release()

"""
Function increaseVolume is used to increae the volume by sending input to omxplayer when the B button is pressed
"""
def increaseVolume(event):
	global volume
	global lock6
	global lock7
	global lock8
	global lock9
	global whatSound1
	global whatSound2
	global whatSound3
	global whatSound4
	global showHelp
	global lock13
	global helpCheck1
	lock13.acquire()
	helpCheck1 = showHelp
	lock13.release()
	if event.key == p.K_b and volume >= 1 and helpCheck1 == False:
		volume -= 1
		sendKey("+")
		if volume == 25:
			lock6.acquire()
			whatSound1 = True
			lock6.release()
		elif volume < 25 and volume > 17:
			lock7.acquire()
			whatSound2 = True
			lock7.release()
		elif volume <= 17 and volume > 9:
			lock8.acquire()
			whatSound3 = True
			lock8.release()
		elif volume <= 9 and volume >= 0:
			lock9.acquire()
			whatSound4 = True
			lock9.release()
	elif event.key == p.K_b and helpCheck1 == True:
		lock9.acquire()
		whatSound4 = True
		lock9.release()
"""
Function rewindSong is used to move the song back 30 seconds when the down button is pressed. If the song is less than 30 seconds in play time, then
the song is restarted.
"""
def rewindSong(event):
	global middleTime
	global lock11
	global music
	global volume
	global current
	global List
	global showHelp
	global checkHelp1
	global lock13
	global lock19
	global checkRewind
	lock13.acquire()
	checkHelp1 = showHelp
	lock13.release()
	if songPlaying == True and middleTime > 30 and checkHelp1 == False:  
		if event.key == p.K_d:
			lock11.acquire()                                
			middleTime -= 30
			lock11.release()
			sendKey("\x1B[D")                                                   
	elif songPlaying == True and middleTime <= 30 and checkHelp1 == False:
		if event.key == p.K_d:
			lock11.acquire()
			middleTime = 0
			lock11.release()
			sendKey("q")
			music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			setVolume(volume)
	elif event.key == p.K_d and checkHelp1 == True:
		lock19.acquire()
		checkRewind = True
		lock19.release()
"""
Function fastforwardSong is used to move the song 30 seconds forward when the up button is pressed. If the song finishes when doing this,
then the next song is played.
"""
def fastforwardSong(event):
	global middleTime
	global lock11
	global current
	global newVar4
	global nowDisplaying
	global volume
	global checkHelp1
	global showHelp
	global checkFastForward
	global lock20
	global lock13
	lock13.acquire()
	checkHelp1 = showHelp
	lock13.release()
	if songPlaying == True and checkHelp1 == False:
		if event.key == p.K_u:
                        try:
                                lock11.acquire()
                                middleTime += 30
                                lock11.release()
                                sendKey("\x1B[C")
                        except:
                                pass
        elif checkHelp1 == True and event.key == p.K_u:
                lock20.acquire()
                checkFastForward = True
                lock20.release()
"""
Function orientationLock is used to either lock or unlock the ability for the screen to change orientation when the raspberry pi spins around.
This is done by pressing the joystick button quickly. If the joystick button is held down for more than two seconds then the MP3 player will shut down
closing both the dislay thread and main control loop safely
"""
def orientationLock(event):
	global isOrientation
	global canOrientation1
	global canOrientation2
	global lock14
	global lock15
	global lock1
	global leave
	if event.key == p.K_RETURN:
                time.sleep(2)
                for event3 in p.event.get():
                        if event3.type == p.KEYUP and event3.key == p.K_RETURN:                
                                if isOrientation == True:
                                        isOrientation = False
                                        lock14.acquire()
                                        canOrientation1 = True
                                        lock14.release()
                                elif isOrientation == False:
                                        isOrientation = True
                                        lock15.acquire()
                                        canOrientation2 = True
                                        lock15.release()
                                break
                else:
                        lock1.acquire()
                        leave = True
                        lock1.release()
                
"""
Function checkSongFinished is used to see whether the currently playing song has finished. If it has then the next song in the list will be played
"""
def checkSongFinished():
	global music
	global volume
	global lock
	global current
	global nowDisplaying
	global newVar2
	global lock11
	global middleTime
	global List
	try:
		if music.poll() is not None:
			if current < (len(List) - 1):
				current += 1
				newVar2 = current
				lock.acquire()
				nowDisplaying = newVar2
				lock.release()
			else:
				current = 0
				newVar2 = current
				lock.acquire()
				nowDisplaying = newVar2
				lock.release()
			music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			lock11.acquire()
			middleTime = 0
			lock11.release()
			setVolume(volume)
	except:
		print("Next Song Could not be Played")
"""
Function checkShake takes the accelerometer data for all the x,y,z axis. If the MP3 player is shaken purposely then the
song will shuffle to a random song in the list of songs. This songs will not be the same song, thanks to the while loop.
There is a cooldown of 2 seconds to make sure the song is shuffled once with each shake
"""
def checkShake():
	global xAxis
	global yAxis
	global zAxis
	global overTime
	global shakeTime
	global isShake
	global randomNumber
	global List
	global music
	global current
	global newVar3
	global nowDisplaying
	global middleTime
	global lock11
	global lock
	global volume
	global showHelp
	global lock13
	global checkHelp1
	lock13.acquire()
	checkHelp1 = showHelp
	lock13.release()
	xAxis, yAxis, zAxis = sense.get_accelerometer_raw().values()
	if isShake == False:
		shakeTime += time.time() - overTime
		if shakeTime >= 2:
			isShake = True
			shakeTime = 0
	elif isShake == True and checkHelp1 == False:    
		xAxis = abs(xAxis)
		yAxis = abs(yAxis)
		zAxis = abs(zAxis)
		if xAxis > 1.4 or yAxis > 1.4 or zAxis > 1.4:
			randomNumber = random.randint(0,(len(List)-1))
			while randomNumber == current:
				randomNumber = random.randint(0,(len(List)-1))
			sendKey("q")
			current = randomNumber
			music = subprocess.Popen(["omxplayer", List[current], "-o", "local", "-I"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			newVar3 = current
			lock.acquire()
			nowDisplaying = newVar3
			lock.release()
			lock11.acquire()
			middleTime = 0
			lock11.release()
			setVolume(volume)
			isShake = False
"""
Function checkTemperature is used to get the temperature of the surroundings and then according to the
temperature, change the colour of the display text of the song name. This is usually more red due to the heat from the raspberry pi itself.
"""
def checkTemperature():
	global temperature
	global lock16
	global backgroundColour
	temperature = sense.get_temperature()
	temperature = round(temperature, 1)
	if temperature > 26.7:
		lock16.acquire()
		backgroundColour = [255,0,0]
		lock16.release()
	elif temperature > 25.3 and temperature <= 26.7:
		lock16.acquire()
		backgroundColour = [250,128,114]
		lock16.release()
	elif temperature > 23.9 and temperature <= 25.3:
		lock16.acquire()
		backgroundColour = [255,165,0]
		lock16.release()
	elif temperature > 22.5 and temperature <= 23.9:
		lock16.acquire()
		backgroundColour = [255,255,0]
		lock16.release()
	elif temperature > 21.1 and temeprature <= 22.5:
		lock16.acquire()
		backgroundColour = [0,128,0]
		lock16.release()
	elif temperature > 19.7 and temperature <= 21.1:
		lock16.acquire()
		backgroundColour = [0,255,127]
		lock16.release()
	elif temperature > 18.3 and temperature <= 19.7:
		lock16.acquire()
		backgroundColour = [0,255,255]
		lock16.release()
	else:
		lock16.acquire()
		backgroundColour = [0,0,255]
		lock16.release()
			
#################################################################################################################

############################################### While Loop of Main Thread #######################################
"""
This is the main control loop and contains the code which checks the angle of rotation of the raspberry pi
, calls the above functions, contains a 0.005 seconds time delay which stops the display thread from going very slowly
and also contains the code which updates the middleTime variable as to the current time the song has played for.
"""
while True:
	overTime = time.time()
	
	checkTemperature()
	
	pitch, yaw, roll = sense.get_orientation_degrees().values()
	if isOrientation == True:
		if yaw >= 90 and yaw < 180:
			lock12.acquire()
			angle = 180
			lock12.release()
		elif yaw >= 180 and yaw < 270:
			lock12.acquire()
			angle = 90
			lock12.release()
		elif yaw >= 270 and yaw < 360:
			lock12.acquire()
			angle = 0
			lock12.release()
		else:
			lock12.acquire()
			angle = 270
			lock12.release()
			
	checkShake()
	  
	lock1.acquire()
	if leave == True:
                break
	lock1.release()
	
	for event in p.event.get():
                if event.type == p.KEYDOWN:
                        scroll(event)
                        nextTrack(event, False)
                        previousTrack(event, False)
                        info(event)
                        playPause(event)
                        decreaseVolume(event)
                        increaseVolume(event)
                        rewindSong(event)       
                        fastforwardSong(event)
                        orientationLock(event)
			
	time.sleep(0.005)
	overTime = (time.time() - overTime)
	if increase == True:
		lock11.acquire()
		middleTime += overTime
		lock11.release()
	if start == False:
		checkSongFinished()
#################################################################################################################

################################################ Exit and Shutting Down of the Pygame Modules ###################
"""
This code is run once the control loop has been exited. It shuts down the pygame display, and then waits for the display thread to close.
There is a five second timeout on this command incase the display thread does not stop as expected.
It then closes omxplayer down, if omxplayer was initiated.
The print statements are sent to the terminal to tell the user if they are using monitor that the program has ended.
The display will clear when the program has ended.
"""
p.display.quit()
thread.join(5.0)
try:
	sendKey("q")
	print("Control Manager has Closed Down")
except:
	print("Song Did Not Start Playing")
	print("Control Manager has Closed Down")
#################################################################################################################
		
