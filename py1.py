import pygame

pygame.init() #initializing pygame

gameDisplay=pygame.display.set_mode((800,600))

pygame.display.set_caption('Slytherin')

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
gameExit=False
while not gameExit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True;
        #print(event)
    gameDisplay.fill(white)
   # pygame.draw.rect(gameDisplay,black,[400,300,10,100])
   # gameDisplay.fill(red,rect=[0,0,50,50])

pygame.display.update()


pygame.quit() #uninitialize pygame
quit() #Exits pygame
