import pygame
import os, sys


imageX=pygame.image.load(os.path.join('images','x.png'))
imageO=pygame.image.load(os.path.join('images',"0.png"))

class Grid:
    def __init__(self):
        self.gridline= [((0,200),(600,200)),
                        ((0,400),(600,400)),
                        ((200,0),(200,600)),
                        ((400,0),(400,600))]

        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]


        self.switch_player = True

        search_dirs=[(0,-1), (-1,1), (-1,0),(-1,1),(1,1),(0,1),(1,1),(1,0),(1,-1)]





    def draw(self,surface):
        for section in self.gridline:
            pygame.draw.line(surface,(200,200,200),section[0],section[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x,y) == 1:
                    surface.blit(imageX, (x*200,y*200))
                elif self.get_cell_value(x,y) == 2:
                    surface.blit(imageO, (x*200, y*200))





    def get_cell_value(self,x,y):
        return self.grid[y][x]

    def set_cell_value(self,x,y,value):
        self.grid[y][x] = value



    def get_mouse(self,x,y,player):
        if self.get_cell_value(x,y) == 0:
            self.switch_player = True
            if player == "X":
                self.set_cell_value(x,y,1)
            if player == "O":
                self.set_cell_value(x,y,2)
        else:
            self.switch_player = False


    def sort(self):
        grid = self.grid
        s













    def print_grid(self):
        for row in self.grid:
            print(row)
