import pygame 

pygame.init()

game_screen = pygame.display.set_mode(600, 600)

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == False:
            game_running = False
