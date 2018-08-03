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


question=QuestionClass

#check picture files first
soundMax=24
pictureMax=37

testQuestion=1

while (testQuestion<=pictureMax):
	questionFilename="picture/picture"
	questionFilename+=str(testQuestion)+".txt"
	print("Testing question " + questionFilename)
	F=open("questions/"+questionFilename)
	question.type=F.readline().strip()
	question.type=question.type.lower()		#convert to lower case for comparisons
	question.options=int(F.readline().strip())
	question.answer=int(F.readline().strip())
	#if questionType==1:		####################if if picture type is picture get pic filename
	questionFile="questions/picture/pics/"+F.readline().strip()
	#if questionType==3:
	#	question.filename="questions/sound/sounds/"+F.readline().strip()
	question.question=F.readline().strip()
	question.option1=F.readline().strip()
	question.option2=F.readline().strip()
	question.option3=F.readline().strip()
	question.option4=F.readline().strip()
	F.close()
	print("Question " + questionFilename + " OK")
	print("Opening file " + questionFile)
	F=open(questionFile)
	testQuestion+=1


#check sound files now

testQuestion=1

while (testQuestion<=soundMax):
	questionFilename="sound/sound"
	questionFilename+=str(testQuestion)+".txt"
	print("Testing question " + questionFilename)
	F=open("questions/"+questionFilename)
	question.type=F.readline().strip()
	question.type=question.type.lower()		#convert to lower case for comparisons
	question.options=int(F.readline().strip())
	question.answer=int(F.readline().strip())
	#if questionType==1:		####################if if picture type is picture get pic filename
	questionFile="questions/sound/sounds/"+F.readline().strip()
	#if questionType==3:
	#	question.filename="questions/sound/sounds/"+F.readline().strip()
	question.question=F.readline().strip()
	question.option1=F.readline().strip()
	question.option2=F.readline().strip()
	question.option3=F.readline().strip()
	question.option4=F.readline().strip()
	F.close()
	print("Question " + questionFilename + " OK")
	print("Opening file " + questionFile)
	F=open(questionFile)
	testQuestion+=1

print("All picture and sound files correspond")
