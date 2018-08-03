import pygame
from pygame.locals import *
from pygame import joystick, event
#from pygame import QUIT, JOYAXISMOTION, JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN


pygame.init()
pygame.joystick.init()

for i in range(pygame.joystick.get_count()):
	pygame.joystick.Joystick(i).init()
	
done=False	
while not done:
	e=event.wait()
	if e.type == QUIT:
		done = True
	elif e.type == KEYDOWN:
		if e.key == K_ESCAPE:
			done=True
	if e.type == JOYBUTTONUP:   print ("Joystick # " + str(e.joy) + " button " + str(e.button) + " up")
	if e.type == JOYBUTTONDOWN: print ("Joystick # " + str(e.joy) + " button " + str(e.button) + " down")
	player=e.joy
	button=e.button
	print("Player " + str(player) +" pressed button " + str(button))

