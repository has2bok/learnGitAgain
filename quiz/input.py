import pygame
from pygame import joystick, event
from pygame.locals import *
from surfaces import *

#pygame.joystick.init()

#take correct option number, check for input and return positive option for correct answer,  negative option chosen for incorrect answer
#or return zero for out of time
def getResponse(player, correct):       #retrun the option number if correct answer or -1 if wrong
	countdown=0
	pygame.event.clear()
	pygame.time.set_timer(pygame.USEREVENT, 1000)   #give x seconds for an answer or return zero
	done=False
	while not done:
		displayCountdown(countdown)
		e=event.wait()
		#for event in pygame.event.get():
		if e.type == USEREVENT:
			countdown+=1
			if countdown==5:
				pygame.time.set_timer(pygame.USEREVENT, 0)      #turn off user timer
				done = True
				return 0
		if cfg.keyboardControl==True:
			if e.type == KEYDOWN:
				if e.key == K_1:
					done=True
					if correct==1:
						return correct
					else:
						return -1
				elif e.key==K_2:
					done=True
					if correct==2:
						return correct
					else:
						return -2
				elif e.key==K_3:
					done=True
					if correct==3:
						return correct
					else:
						return -3
				elif e.key==K_4:
					done=True
					if correct==4:
						return correct
					else:
						return -4
		if cfg.bigButtonControl==True:
			if e.type==JOYBUTTONDOWN:
				if e.button!=6:		#dont accept big button
					if e.joy==cfg.players[player-1].controller:       #check for correct player controller ignore other controllers
						if (e.button+1)==correct:
							done=True
							print("correct = "+str(correct)+" button = "+str(e.button))
							return correct
						else:
							print("correct = "+str(correct)+"-button = "+str((-(e.button+1))))
							return ((e.button+1)*-1)

##########for testing players take first key as player number ie. a=player1, b=player2, c=player3
def getPlayer(delay):

	pygame.event.clear()
	player=0
	pygame.time.set_timer(pygame.USEREVENT, delay)  #setup timer of x seconds for someone to click their big answer button
	done=False

	while not done:
		e=event.wait()
		if e.type==USEREVENT:
			pygame.time.set_timer(pygame.USEREVENT, 0)      #turn off user timer
			done = True
		if cfg.keyboardControl==True:
			if e.type == KEYDOWN:
				if e.key==K_1:
					if cfg.player1.excluded==False:
						player=1
						done=True
				elif e.key==K_2:
					if cfg.player2.excluded==False:
						player=2
						done=True
				elif e.key==K_3:
					if cfg.player3.excluded==False:
						player=3
						done=True
				elif e.key==K_4:
					if cfg.player4.excluded==False:
						player=4
						done=True
		if cfg.bigButtonControl==True:
			if e.type == JOYBUTTONDOWN:
				print("joy button down dtected")
				if e.button == 6:       #big button on controller
					for f in range(len(cfg.players)):                       #cycle through players to find who pressed their big button
						if e.joy==cfg.players[f].controller:
							if cfg.players[f].excluded==False:
								player=f+1	#might be needed to make sure correct player is passed
								done=True

		# for event in pygame.event.get():
		#       if event.type == USEREVENT:
		#               pygame.time.set_timer(pygame.USEREVENT, 0)      #turn off user timer
		#               done = True
		#       elif event.type == KEYDOWN:
		#               if event.key==K_a:
		#                       if cfg.player1.excluded==False:
		#                               player=1
		#                               done=True
		#               if event.key==K_b:
		#                       if cfg.player2.excluded==False:
		#                               player=2
		#                               done=True
		#               if event.key==K_c:
		#                       if cfg.player3.excluded==False:
		#                               player=3
		#                               done=True
	return player

