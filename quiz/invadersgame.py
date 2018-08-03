import pygame
import random
from pygame.locals import *
from pygame import event

pygame.init()
random.seed()

import cfg

WHITE=pygame.Color('white')
BLACK=pygame.Color('black')
screen_width = 800
screen_height = 600
gamescreen = pygame.display.set_mode([screen_width, screen_height])



class Sprites(pygame.sprite.Sprite):
	def __init__(self, image, width, height):
	# Call the parent class (Sprite) constructor
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image = pygame.transform.scale(self.image, (width, height))
		# Set our transparent color
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

class Rockets(pygame.sprite.Sprite):
	def __init__(self, image, whoFired, x, y, width, height):
	# Call the parent class (Sprite) constructor
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image = pygame.transform.scale(self.image, (width, height))
		# Set our transparent color
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.player=whoFired

def getPlayer(e):

	#pygame.event.clear()
	player=0
	#pygame.time.set_timer(pygame.USEREVENT, delay)  #setup timer of x seconds for someone to click their big answer button
	done=False

	#while not done:
	#e=pygame.event.get()
	#e=event.wait()
	#if e.type==USEREVENT:
	#	pygame.time.set_timer(pygame.USEREVENT, 0)      #turn off user timer
	#	done = True
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
							player=f+1              #might be needed to make sure correct player is passed
							done=True

	return player


gamebg=pygame.image.load("graphics/starrysky.jpg")
gamebg=pygame.transform.scale(gamebg,(screen_width, screen_height))
explosion=pygame.image.load("graphics/explosion.png")
explosion=pygame.transform.scale(explosion, (64,64))

enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
rocket_list= pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


p1=Sprites("graphics/invaderp1.jpg", 32, 32)
player_list.add(p1)
all_sprites_list.add(p1)
p2=Sprites("graphics/invaderp2.jpg", 32, 32)
player_list.add(p2)
all_sprites_list.add(p2)
p3=Sprites("graphics/invaderp3.jpg", 32, 32)
player_list.add(p3)
all_sprites_list.add(p3)
p4=Sprites("graphics/invaderp4.jpg", 32, 32)
player_list.add(p4)
all_sprites_list.add(p4)
enemy=Sprites("graphics/invader.jpg", 32, 32)
enemy_list.add(enemy)
all_sprites_list.add(enemy)
#rocket=Sprites("graphics/rocket.jpg", 32, 32)



playerRockets=[0, 0, 0, 0]
maxRockets=2

spacing=int(screen_width/5)
x=spacing
y=screen_height-40

randomx=[0,0,0,0]	#shuffle the players x coords 

counter=0
for f in range(len(randomx)):	#player_list:
 	randomx[counter]=x
 	x+=spacing
 	counter+=1
random.shuffle(randomx)

counter=0
for f in player_list:
	f.rect.x=randomx[counter]
	f.rect.y=y
	cfg.players[counter].gamex=randomx[counter]
	cfg.players[counter].gamey=y
	counter+=1

x=0
y=0

clock = pygame.time.Clock()

done = False
while not done:

	clock.tick(30)
	player=0

	hit_list = pygame.sprite.spritecollide(enemy, rocket_list, False)
	for f in hit_list:
		player=f.player
		cfg.players[player-1].score+=50
		print("player hit = " + str(cfg.players[player-1].name))
		done=True
		gamescreen.blit(explosion, (enemy.rect.x, enemy.rect.y))
		pygame.display.flip
	#move the spaceship across the top of screen
	x+=10
	if (x+32>screen_width):
		x=0
#		y+=10
		if (y+32>screen_height):
			y=0
			x=0
	enemy.rect.x = x
	enemy.rect.y = y

	#update rockets going up the screen
	for r in rocket_list:
		r.rect.y-=10
		if r.rect.y<0:
			playerRockets[r.player-1]-=1
			r.kill()



	gamescreen.blit(gamebg,(0,0))
	all_sprites_list.update()
	#gamescreen.fill(BLACK)
	all_sprites_list.draw(gamescreen)
	pygame.display.flip()





	for e in pygame.event.get():
		if e.type == QUIT:
			done = True
			pygame.quit()
		elif e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				done=True
			else:
				player=getPlayer(e)
		elif e.type==JOYBUTTONDOWN:
				player=getPlayer(e)

	if (player>0 and playerRockets[player-1]<maxRockets):
		rocket=Rockets("graphics/rocket.jpg", player, cfg.players[player-1].gamex, cfg.players[player-1].gamey, 32, 32)
		#rocket=Rockets("graphics/rocket.jpg", player, player*spacing, screen_height-80, 32, 32)
		#rocket.rect.x=player*spacing
		#rocket.rect.y=screen_height-80
		rocket_list.add(rocket)
		all_sprites_list.add(rocket)
		playerRockets[player-1]+=1

	print("player = " + str(player))



pygame.quit()
