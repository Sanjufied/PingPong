import sys

import pygame
import OpenGL.GL as gl
import numpy as np

class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((1920 , 1080))
        pygame.display.set_caption("PingPong")
        self.clock = pygame.time.Clock()
        self.player1 = pygame.rect.Rect(30 , 100 , 30 , 90)
        self.player2 = pygame.rect.Rect(1920 - 30 - 30 , 100 , 30 , 90)
        self.box = pygame.rect.Rect(1920/2 , 1080/2 , 20 , 20)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT : sys.exit()
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen , "#da16af" , self.player1)
            pygame.draw.rect(self.screen , "#da16af" , self.player2)
            pygame.draw.rect(self.screen , "#da16af" , self.box)

            pygame.display.flip()
            dt = self.clock.tick()
            


        
    
    
    
    
    
if __name__ == '__main__':
    Player = main()
    Player.run()
    
    pygame.quit()