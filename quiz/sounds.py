import pygame

def playSound(filename):
	pygame.mixer.music.load(filename)
	#pygame.time.wait(delay)
	pygame.mixer.music.play(-1)

def stopSound():
	pygame.mixer.music.stop()
