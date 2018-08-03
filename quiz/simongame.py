import pygame
import random


from pygame.locals import *
from pygame import event

pygame.init()
random.seed()

screen_width = 800
screen_height = 600
gamescreen = pygame.display.set_mode([screen_width, screen_height])

import cfg
import surfaces
from surfaces import *

button=random.randint(1,4)
if button==1:
	buttonText="GREEN"
	buttonColour=cfg.red
elif button==2:
	buttonText="RED"
	buttonColour=cfg.yellow
elif button==3:
	buttonText="BLUE"
	buttonColour=cfg.red
elif button==4:
	buttonText="YELLOW"
	buttonColour=cfg.blue



text="Press your small"
#def blit_text(surface, text, pos, font, bgcolour, txtcolour):
blit_text(gamescreen, text, (100,100), cfg.questionfont, cfg.black, cfg.white)
blit_text(gamescreen, buttonText, (200,200), cfg.questionfont, cfg.black, buttonColour)
blit_text(gamescreen, "button", (200,300), cfg.questionfont, cfg.black, cfg.white)
pygame.display.flip()

button-=1	#to make it equal to wee buttopn on controller
e=event.wait()
if e.type==JOYBUTTONDOWN:
	if e.button!=6:		#dont accept big button
#		if e.joy==cfg.players[player-1].controller:       #check for correct player controller ignore other controllers
		if (e.button)==button:
			done=True
			#print("correct = "+str(correct)+" button = "+str(e.button))
			#return correct
			cfg.players[e.joy].score+=10
			text=cfg.players[e.joy].name
			blit_text(gamescreen, text, (200, 400), cfg.questionfont, cfg.black, cfg.white)
		else:
			print("correct = "+str(correct)+"-button = "+str((-(e.button+1))))
			#return ((e.button+1)*-1)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done=True

pygame.quit()