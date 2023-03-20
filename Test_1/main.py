import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
)

position_y = 250
position_x = 250

created = True

def createRects():
    global created
    if created == True:
        x1 = random.randint(0, 800)  
        y1 = random.randint(0, 640)  
        x2 = random.randint(0, 800)
        y2 = random.randint(0, 640)
        
        pygame.draw.rect(screen, (0, 255, 0), rect=(x1, y1, 60, 160)) 
        pygame.draw.rect(screen, (0, 255, 0), rect=(x2, y2, 60, 160))     
        created = False



pygame.init()

time = pygame.time.get_ticks()

events = pygame.event.get()
screen = pygame.display.set_mode([1200, 500])

screenWidth = screen.get_width()

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                position_y += 45
                print(position_y)
            if event.key == K_UP:
                position_y -= 45
                print(position_y)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    if time > 0.1:
        position_x += 0.3

    if position_y < 205 or position_y > 295:
        position_y = 250

    createRects()
    
    pygame.draw.circle(screen, (0, 0, 255), (position_x, position_y), 15)

    pygame.display.flip()

pygame.quit()
