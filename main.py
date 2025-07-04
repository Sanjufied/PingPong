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

    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT : sys.exit()
            self.screen.fill((0,0,0))

        
    
    
    
    
    
if __name__ == '__main__':
    Player = main()
    Player.run()
    
    pygame.quit()