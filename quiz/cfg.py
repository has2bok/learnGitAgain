import pygame
from pygame.locals import FULLSCREEN
#pygame.init()

textQuestionMax=84
picQuestionMax=42
soundQuestionMax=24
testQuestion=0		#for testing certain question set it's file number here or else =0
testType=0			#for testing different subjects 1= picture questions, 2=text questions,  3= sound questions
bigButtonControl=True	#input big button controller true/false
keyboardControl=True

black=pygame.Color('black')
red=pygame.Color('red')
#blue=(100,100,200)
blue=pygame.Color('blue')
green=pygame.Color('green')
yellow=(250, 200, 50)	#pygame.Color('yellow')
white=pygame.Color('white')
gray=pygame.Color(100,100,100)

class PlayerClass:
	def __init__(self, name, colour, controller, banner):
		self.name=name
		self.score=0
		self.colour=colour
		self.controller=controller
		self.banner=banner
		self.excluded=False
		self.gamex=0
		self.gamey=0

class QuestionClass:
	def __init__(self, type, options, answer, filename, question, option1, option2, option3, option4):
		self.type=type
		self.options=options
		self.answer=answer
		self.filename=filename
		self.question=question
		self.option1=option1
		self.option2=option2
		self.option3=option3
		self.option4=option4
		self.waitForAnswer=0

screeninfo = pygame.display.Info()
screenwidth=screeninfo.current_w
screenheight=screeninfo.current_h
screen=pygame.display.set_mode((screenwidth, screenheight))	#, FULLSCREEN)

#divide screen into rows and columns
screenrows=int(screenheight/10)
screencolumns=int(screenwidth/8)

pictureScaleHeight=int(screenrows*4)
pictureScaleWidth=int(screencolumns*4)



background=pygame.image.load("graphics/quizzes1.jpg")
background=pygame.transform.scale(background,(screenwidth, screenheight))
p1Banner=pygame.image.load("graphics/p1banner.jpg")
p1Banner=pygame.transform.scale(p1Banner, (screencolumns*1,screenrows*1))
p2Banner=pygame.image.load("graphics/p2banner.jpg")
p2Banner=pygame.transform.scale(p2Banner, (screencolumns*1, screenrows*1))
p3Banner=pygame.image.load("graphics/p3banner.jpg")
p3Banner=pygame.transform.scale(p3Banner, (screencolumns*1, screenrows*1))
p4Banner=pygame.image.load("graphics/p4banner.jpg")
p4Banner=pygame.transform.scale(p4Banner, (screencolumns*1, screenrows*1))
banner=pygame.image.load("graphics/quizbanner2.png")
banner=pygame.transform.scale(banner, (screenwidth, screenrows*2))
correctAnswer=pygame.image.load("graphics/correct.jpg")
correctAnswer=pygame.transform.scale(correctAnswer, (screencolumns*3, screenrows*3))
wrongAnswer=pygame.image.load("graphics/wrong.jpg")
wrongAnswer=pygame.transform.scale(wrongAnswer, (screencolumns*3, screenrows*3))
timeout=pygame.image.load("graphics/outoftime.jpg")
timeout=pygame.transform.scale(timeout, (screencolumns*3, screenrows*3))
pointer=pygame.image.load("graphics/pointer.png")
picPointer=pygame.image.load("graphics/picpointer.png")
timer0=pygame.image.load("graphics/clock0.png")
timer0=pygame.transform.scale(timer0, (screencolumns*4, screenrows*4))
timer1=pygame.image.load("graphics/clock1.png")
timer1=pygame.transform.scale(timer1, (screencolumns*4, screenrows*4))
timer2=pygame.image.load("graphics/clock2.png")
timer2=pygame.transform.scale(timer2, (screencolumns*4, screenrows*4))
timer3=pygame.image.load("graphics/clock3.png")
timer3=pygame.transform.scale(timer3, (screencolumns*4, screenrows*4))
timer4=pygame.image.load("graphics/clock4.png")
timer4=pygame.transform.scale(timer4, (screencolumns*4, screenrows*4))
timers=[timer0, timer1, timer2, timer3, timer4]
excludeBanner=pygame.image.load("graphics/exclude.png")
excludeBanner=pygame.transform.scale(excludeBanner, (screencolumns*1, screenrows*1))
questionfont = pygame.font.SysFont('Comic Sans MS', 70)
optionfont= pygame.font.SysFont('Comic Sans MS', 70, True)
scoreFont=pygame.font.SysFont('Comic Sans MS', 90, True)


player1=PlayerClass("Player 1", green, 0, p1Banner)	#name,  colour, controller number, banner surface
player2=PlayerClass("Player 2", red, 1, p2Banner)
player3=PlayerClass("Player 3", blue, 2, p3Banner)
player4=PlayerClass("Player 4", yellow, 3, p4Banner)
players=[player1, player2, player3, player4]
