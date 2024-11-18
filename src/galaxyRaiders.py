import pygame
import random

def player_controller(screen, playerX, playerY):
        player_image = pygame.image.load('space-invaders.png')
        screen.blit(player_image, (playerX, playerY))

def enemy(screen, enemyX, enemyY):
    enemy_image = pygame.image.load('ufo.png')
    screen.blit(enemy_image, (enemyX, enemyY))

"""       
class Enemy():

    def __init__(self, enemyX = 370, enemyY = 50, enemyX_change = 0, enemyY_change = 0):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change 
        self.enemyY_change = enemyY_change
    
    def draw_enemy(self, enemyX, enemyY):
        self.image = pygame.image.load('ufo.png')
        screen.blit(self.image, (enemyX, enemyY))
"""


def main():
    #Initialize pygame 
    pygame.init()
    pygame.display.set_caption("Galaxy Raiders")
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution))
    background = pygame.image.load('spaceBackground.jpg')
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0
    enemyX = random.randint(0,800)
    enemyY = random.randint(50,150)
    enemyX_change = 0
    enemyY_change = 0
    #enemy_called = Enemy()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #if keystroke is pressed, check if left or right and move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.5
            if event.key == pygame.K_RIGHT:
                playerX_change = .5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
    #render
        black = pygame.Color(0,0,0)
        screen.fill (black)
        screen.blit(background, (0,0))
        playerX += playerX_change
        player_controller(screen, playerX, playerY)
        enemy(screen, enemyX, enemyY)
        #enemy_called()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()