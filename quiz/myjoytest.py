import pygame

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print ("Initialised Joystick : ", joystick.get_name())
print ("Press ESC to stop")

screen = pygame.display.set_mode((800,600))

# get count of joysticks=1, axes=27, buttons=19 for DualShock 3

joystick_count = pygame.joystick.get_count()
print("joystick_count")
print(joystick_count)
print("--------------")

numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)
print("--------------")

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 24)

WHITE=(255,255,255)
textsurface=[]
loopQuit = False
while loopQuit == False:

        e=event.wait()
        if e.type == QUIT:
            loopQuit = True
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                loopQuit=True
        if e.type==JOYBUTTONDOWN:
                print("Joystick #" + e.joy + "Button " + e.button + " down")
        if e.type==JOYBUTTONUP:
                print("Joystick #" + e.joy + "Button " + e.button + " up")
        # textCount=0
        # for f in range(0,joystick_count):
        #         text="Joystick number " + str(joystick_count)
        #         textsurface[textCount] = myfont.render(text , False, WHITE)
        #         textCount+=1
        # # test joystick axes
        #         for i in range(0,4):
        #                 pygame.event.pump()
        #                 axis = joystick.get_axis(i)
        #                 print("Axis " + str(i) + " = " + str(axis))
        #                 text="Axis " + str(i) + " = " + str(axis)
        #                 textsurface[textCount] = myfont.render(text , False, WHITE)
        #                 textCount+=1
        #         print("--------------")

        # # test controller buttons
        #         for i in range(0,numbuttons):
        #                 pygame.event.pump()
        #                 button = joystick.get_button(i)
        #                 print("Button " + str(i) + " = " + str(button))
        #                 text="Button " + str(i) + " = " + str(button)
        #                 textsurface[textCount] = myfont.render(text , False, WHITE)
        #                 textCount+=1
        #         print("--------------")
        
        # for i in range (0, len(textsurface)):
        #         screen.blit(textsurface[i],(0,10*i))
        # pygame.display.update()

# quit if escape pressed
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                loopQuit = True

        #pygame.display.update()

pygame.quit()