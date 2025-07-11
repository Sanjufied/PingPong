import random
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
        self.player1 = pygame.rect.FRect(30 , 100 , 30 , 90)
        self.player2 = pygame.rect.FRect(1920 - 30 - 30 , 100 , 30 , 90)
        self.box = pygame.rect.FRect(1920/2 , 1080/2 , 20 , 20)
        self.flow = random.choice((-1 ,1))
        self.direction = pygame.Vector2(self.flow,1)
        self.difficutly = 0.4
    
    def run(self):
        change_difficulty = pygame.event.custom_type()
        pygame.time.set_timer(change_difficulty , 10000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT : sys.exit()
                if event.type == change_difficulty : self.difficutly += 0.1
            
            dt = self.clock.tick()
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen , "#da16af" , self.player1)
            pygame.draw.rect(self.screen , "#da16af" , self.player2)
            pygame.draw.rect(self.screen , "#da16af" , self.box)

            pygame.display.flip()
            self._inputs(dt)
            self._box_movement(dt)


    def _inputs(self , dt):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_w]:
            self.player1.y -= 1 * dt 

        if keypressed[pygame.K_s]:
            self.player1.y += 1 * dt

        if keypressed[pygame.K_UP]:
            self.player2.y -= 1 * dt

        if keypressed[pygame.K_DOWN]:
            self.player2.y += 1 * dt

    def _box_movement(self ,dt):
        # Check collision with paddles and reverse horizontal direction
        if self.box.colliderect(self.player2) or self.box.colliderect(self.player1):
            self.direction.x *= -1
        
        # Bounce off top and bottom
        if self.box.bottom > 1080:
            self.direction.y *= -1
        if self.box.top < 0:
            self.direction.y *= -1

        self.box.center += self.direction * dt * self.difficutly
        # Reset if out of bounds
        if self.box.left > 1920 or self.box.right < 0:
            self.box.center = pygame.Vector2(1920/2 , 1080 /2)
            self.direction = pygame.Vector2(random.choice((-1,1)), 1)
        
            

            


        
    
    
    
    
    
if __name__ == '__main__':
    Player = main()
    Player.run()
    
    pygame.quit()