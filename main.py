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
            
            dt = self.clock.tick()
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen , "#da16af" , self.player1)
            pygame.draw.rect(self.screen , "#da16af" , self.player2)
            pygame.draw.rect(self.screen , "#da16af" , self.box)

            pygame.display.flip()
            self._inputs(dt)


    def _inputs(self , dt):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_w]:
            self.player1.y -= 2 * dt 

        if keypressed[pygame.K_s]:
            self.player1.y += 2 * dt

        if keypressed[pygame.K_UP]:
            self.player2.y -= 2 * dt

        if keypressed[pygame.K_DOWN]:
            self.player2.y += 2 * dt

            


        
    
    
    
    
    
if __name__ == '__main__':
    Player = main()
    Player.run()
    
    pygame.quit()