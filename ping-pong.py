import pygame
H = 500
W = 500
Game = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((W,H))

while Game:
    event_list = pygame.event.get()
    for event in event_list: 
        if event.type == pygame.QUIT: 
            Game = False
    pygame.display.update() 
    clock.tick(30)