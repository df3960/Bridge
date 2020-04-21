import pygame,sys
from grid import Grid


window = (600,600)
surface = pygame.display.set_mode(window)
pygame.display.set_caption('TTT')
red = [255,0,0]
grid = Grid()


running = True
player = "X"


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0]//200,pos[1]//200, player)
                if grid.switch_player:
                    if player == "X":
                        player ="O"
                    else:
                        player = "X"

                #grid.print_grid()
                grid.sort()









    surface.fill(red)
    grid.draw(surface)
    pygame.display.flip()
