#functions for questions
import pygame
from random import randint
import random
from surfaces import *
#import surfaces
import cfg
from sounds import *
random.seed()

pictureWait=10
textWait=10
soundWait=30

question=cfg.QuestionClass

#get a new question
def getQuestion():
	questionType=randint(1,cfg.picQuestionMax+cfg.textQuestionMax+cfg.soundQuestionMax)	############type : 1 = picture question, 2 = text question,  3 = sound question
	if cfg.testType==1:			###for testing different subjects
		questionType=cfg.testType
	if cfg.testType==2:
		questionType=cfg.testType+cfg.picQuestionMax
	if cfg.testType==3:
		questionType=cfg.testType+cfg.picQuestionMax+cfg.textQuestionMax	
	if (questionType>=1 and questionType<=cfg.picQuestionMax):
		questionNumber=randint(1, cfg.picQuestionMax)
		filename="picture/picture"	#+str(questionNumber)+".txt"	##get picture question
		question.waitForAnswer=pictureWait
		questionType=1
	if (questionType>cfg.picQuestionMax and questionType<=(cfg.picQuestionMax+cfg.textQuestionMax)):
		questionNumber=randint(1, cfg.textQuestionMax)
		filename="text/text"	#+str(questionNumber)+".txt"			##get text question
		question.waitForAnswer=textWait
		questionType=2
	if (questionType>(cfg.picQuestionMax+cfg.textQuestionMax)):
		questionNumber=randint(1, cfg.soundQuestionMax)
		filename="sound/sound"
		question.waitForAnswer=soundWait
		questionType=3
	if cfg.testQuestion>0:					#for testing specific questions
		questionNumber=cfg.testQuestion
	print("Type = " + str(questionType) + "  Number = " + str(questionNumber))
	filename+=str(questionNumber)+".txt"
	F=open("questions/"+filename)
	question.type=F.readline().strip()
	question.type=question.type.lower()		#convert to lower case for comparisons
	question.options=int(F.readline().strip())
	question.answer=int(F.readline().strip())
	if questionType==1:		####################if if picture type is picture get pic filename
		question.filename="questions/picture/pics/"+F.readline().strip()
	if questionType==3:
		question.filename="questions/sound/sounds/"+F.readline().strip()
	question.question=F.readline().strip()
	question.option1=F.readline().strip()
	question.option2=F.readline().strip()
	question.option3=F.readline().strip()
	question.option4=F.readline().strip()
	F.close()

def askQuestion():
	getQuestion()
	questionSurface=createQuestionSurface(question, cfg.screenwidth, cfg.screenrows*3)
	if question.type=="picture":
		pictureSurface=pygame.image.load(question.filename)
		pictureSurface=pygame.transform.scale(pictureSurface, (cfg.pictureScaleWidth, cfg.pictureScaleHeight))
	option1Surface=createOptionsSurface(question.option1, cfg.green)
	option2Surface=createOptionsSurface(question.option2, cfg.red)
	option3Surface=createOptionsSurface(question.option3, cfg.blue)
	option4Surface=createOptionsSurface(question.option4, cfg.yellow)
	if question.type=="picture":
		displayPictureQuestion(questionSurface, pictureSurface, option1Surface, option2Surface, option3Surface, option4Surface)
	else:
		displayQuestion(questionSurface, option1Surface, option2Surface, option3Surface, option4Surface)
	if question.type=="sound":
		playSound(question.filename)





	

