import pygame
from pygame.locals import *

pygame.init()

#import input
from input import *
from questions import *
import questions
import surfaces
#from surfaces import *
import cfg
#from cfg import *
from sounds import *


pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
	pygame.joystick.Joystick(i).init()

#setup text
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
#questionfont = pygame.font.SysFont('Comic Sans MS', 50)
#create surface for question


done = False
while not done:

    player=0

    askQuestion()
    #question.options=4
    #question.question="This is the question" 
    

    player=getPlayer(question.waitForAnswer*1000)   #wait x secs for someone to hit their answer button
    #clear all excluded player flags
    for f in cfg.players:
        f.excluded=False
    
    if player==0:
        createAnswerSurface(0)  #out of time
        pygame.mixer.music.load("sounds/gasp1.mp3")
        pygame.mixer.music.play()
    if player>0:
        displayPlayingBanner(player)    #show banner of player answering question

        response=getResponse(player, question.answer)
        surfaces.createAnswerSurface(response)

        if response!=0:
            surfaces.optionPointer(question.type, abs(response)) #show pointer to option player chose
        if response>0:
            cfg.players[player-1].score+=10
            pygame.mixer.music.load("sounds/correct1.mp3")
            pygame.mixer.music.play()
        if response<0:
            cfg.players[player-1].excluded=True     #wrong answer so player is excluded from answering next question
            pygame.mixer.music.load("sounds/wrong1.mp3")
            pygame.mixer.music.play()
        if response==0:
            cfg.players[player-1].excluded=True     #out of time so excluded from next question    
            pygame.mixer.music.load("sounds/gasp1.mp3")
            pygame.mixer.music.play()
        for f in cfg.players:
            print (f.name, "  Score : ", f.score )
            #print (question.filename)
            #print (players[f].name) , "Score : " + i.score)

    pygame.time.wait(5000)
    stopSound()
    pygame.time.wait(2000)      #probably not necessary, but next question might have sound too1
    #done = False
    #while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done=True
 

pygame.quit()
