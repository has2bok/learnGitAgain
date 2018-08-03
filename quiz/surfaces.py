import pygame
import cfg



def blit_text(surface, text, pos, font, bgcolour, txtcolour):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, txtcolour, bgcolour)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    return surface

def createQuestionSurface(question, width, height):
	surface=pygame.Surface((width, height))
	pygame.Surface.fill(surface, cfg.white)
	questionSurface=blit_text(surface, question.question, (0, 0), cfg.questionfont, cfg.white, cfg.black)
	#questionSurface=questionfont.render(question.question, False, (black), (white))
	return questionSurface

def createOptionsSurface(text, colour):
	optionSurface=cfg.optionfont.render(text, False, colour, cfg.gray)
	return optionSurface

#display correct or wrong image 
def createAnswerSurface(response):
    if response<0:      #wrong answer,  response = negative option
        cfg.screen.blit(cfg.wrongAnswer, (cfg.screencolumns*5, cfg.screenrows*5))
    elif response>0:  #correct answer, response = positive option
        cfg.screen.blit(cfg.correctAnswer,(cfg.screencolumns*5, cfg.screenrows*5))
    elif response==0:  #no answer/out of time
        cfg.screen.blit(cfg.timeout,(cfg.screencolumns*5, cfg.screenrows*5))
    # if answer==True:
    #     cfg.screen.blit(cfg.correctAnswer,(cfg.screencolumns*5, cfg.screenrows*5))
    # else:
    #     cfg.screen.blit(cfg.wrongAnswer, (cfg.screencolumns*5, cfg.screenrows*5))
    pygame.display.flip()

def displayBackground():
    cfg.screen.blit(cfg.player1.banner,(0,0))
    cfg.screen.blit(cfg.player2.banner,(cfg.screencolumns*2,0))
    cfg.screen.blit(cfg.player3.banner,(cfg.screencolumns*4,0))
    cfg.screen.blit(cfg.player4.banner,(cfg.screencolumns*6,0))

    blit_text(cfg.screen, str(cfg.player1.score), (cfg.screencolumns*1,0), cfg.scoreFont, cfg.white, cfg.player1.colour )
    blit_text(cfg.screen, str(cfg.player2.score), (cfg.screencolumns*3,0), cfg.scoreFont, cfg.white, cfg.player2.colour )
    blit_text(cfg.screen, str(cfg.player3.score), (cfg.screencolumns*5,0), cfg.scoreFont, cfg.white, cfg.player3.colour )
    blit_text(cfg.screen, str(cfg.player4.score), (cfg.screencolumns*7,0), cfg.scoreFont, cfg.white, cfg.player4.colour )

    #print excl;uded banner across players banner
    for f in range(0, len(cfg.players)):
        if cfg.players[f].excluded==True:
            cfg.screen.blit(cfg.excludeBanner, (cfg.screencolumns*(f*2), 0))


                    #1=question, 2,3,4,5 = options
def displayQuestion(surface1, surface2, surface3, surface4, surface5):
    cfg.screen.blit(cfg.background,(0,0))
    cfg.screen.blit(cfg.banner,(0,0))
    displayBackground()
    cfg.screen.blit(surface1,(0,cfg.screenrows*2))  #question surface
    #blit_text(screen, question.question, (0, screenrows*2), questionfont, pygame.Color('black'))
    cfg.screen.blit(surface2,(cfg.screencolumns*2, cfg.screenrows*5))   #option 1 surface
    cfg.screen.blit(surface3,(cfg.screencolumns*2, cfg.screenrows*6))   #option 2 surface
    cfg.screen.blit(surface4,(cfg.screencolumns*2, cfg.screenrows*7))   #option 3 surface
    cfg.screen.blit(surface5,(cfg.screencolumns*2, cfg.screenrows*8))   #option 4 surface
    pygame.display.flip()

                            #1=question, 2=picture, 3, 4, 5, 6 = options
def displayPictureQuestion(surface1, surface2, surface3, surface4, surface5, surface6):
    cfg.screen.blit(cfg.background,(0,0))
    cfg.screen.blit(cfg.banner,(0,0))
    displayBackground()
    cfg.screen.blit(surface1,(0,cfg.screenrows*2))  #question surface
    #blit_text(screen, question.question, (0, screenrows*2), questionfont, pygame.Color('black'))
    cfg.screen.blit(surface2,(cfg.screencolumns*4, cfg.screenrows*5))  #picture surface
    cfg.screen.blit(surface3,(cfg.screencolumns*0, cfg.screenrows*5))   #option 1 surface
    cfg.screen.blit(surface4,(cfg.screencolumns*0, cfg.screenrows*6))   #option 2 surface
    cfg.screen.blit(surface5,(cfg.screencolumns*0, cfg.screenrows*7))   #option 3 surface
    cfg.screen.blit(surface6,(cfg.screencolumns*0, cfg.screenrows*8))   #option 4 surface
    pygame.display.flip()

#show pointer to option the player chose
def optionPointer(type, response): 
    base=3
    multiplier=base+response
    if type=="text":
        cfg.screen.blit(cfg.pointer, (cfg.screencolumns*0, cfg.screenrows*multiplier))
    if type=="sound":
        cfg.screen.blit(cfg.pointer, (cfg.screencolumns*0, cfg.screenrows*multiplier))
    if type=="picture":
        cfg.screen.blit(cfg.picPointer, (cfg.screencolumns*2, cfg.screenrows*multiplier))
    pygame.display.flip()

#show banner of player answering question
def displayPlayingBanner(player):
    banner=cfg.players[player-1].banner
    banner=pygame.transform.scale(banner, (cfg.screenwidth, cfg.screenrows*2))
    cfg.screen.blit(banner, (cfg.screencolumns*0,cfg.screencolumns*0))
    pygame.display.flip()

def displayCountdown(count):
    cfg.screen.blit(cfg.timers[count], (cfg.screencolumns*4, cfg.screenrows*2))
    pygame.display.flip()
