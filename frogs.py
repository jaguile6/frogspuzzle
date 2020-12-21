import pygame
import sys
from pygame.locals import *

orange=220,130,40

pygame.init()
screen = pygame.display.set_mode((1400,320))
clock = pygame.time.Clock()
screen.fill(orange)

frog = pygame.image.load("images/frog1.png")
frogrect = frog.get_rect()
frogrect.top=140
frogt = pygame.image.load("images/frog4.png")
frogtrect = frogt.get_rect()
frogtrect.top=140

level = 3
total=level * 2 + 1
center = level + 1

positions = []

for i in range(level): #Per aconseguir una llista tipus [R][R][R][R][ ][L][L][L][L]
    positions.append("R")
positions.append(" ")
for i in range(level): 
    positions.append("L")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if(event.pos[1]>100 and event.pos[1]<220):
                position = int((event.pos[0]-20)/120)
                if(position<total and position>=0):
                    #mover la rana que hay en position
                    if(positions[position]=="L"):
                        if(positions[position-1]==" "):
                            positions[position]=" "
                            positions[position-1]="L"
                        elif(positions[position-2]==" "):
                            positions[position]=" "
                            positions[position-2]="L"
                    if(positions[position]=="R"):
                        if(positions[position+1]==" "):
                            positions[position]=" "
                            positions[position+1]="R"
                        elif(positions[position+2]==" "):
                            positions[position]=" "
                            positions[position+2]="R"  
            
            #Mover la rana si se puede
        
    screen.fill(orange)
    for i in range(total):
        pygame.draw.rect(screen, (90,90,90), [i*120+20, 100, 120, 120], 2)
        if(positions[i]=="R"):
            frogrect.left=i*120+40
            screen.blit(frog, frogrect)
        if(positions[i]=="L"):
            frogtrect.left=i*120+40
            screen.blit(frogt, frogtrect)
    pygame.display.flip()
    clock.tick(60)
        
        