import pygame
import random

def player_controller(screen, x, y):

    player_image = pygame.image.load('space-invaders.png')
    screen.blit(player_image, (x, y))
    

def enemy(screen, x, y):

    enemy_image = pygame.image.load('ufo.png')
    screen.blit(enemy_image, (x, y))
    

def fire_bullet(screen, x, y):  
    
    global bullet_state
    bullet_image = pygame.image.load('paintball.png')
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))


def game_over(screen):
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (190, 250))




def main():

#Initialize pygame 
    pygame.init()
    pygame.display.set_caption("Galaxy Raiders")
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution))
    background = pygame.image.load('spaceBackground.jpg')

#player
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0
    player_hit_box = pygame.Rect(playerX, playerY,  playerX + 64, playerY - 64)

#enemy
    enemyX = random.randint(0,800)
    enemyY = random.randint(50,150)
    enemyX_change = 0.3 
    enemyY_change = 40
    enemy_hit_box = pygame.Rect(enemyX, enemyY, enemyX + 64, enemyY - 64)

#bullet
    global bullet_state
    bulletY = 380
    bulletY_change = 10
    bulletX_change = 0
    bullet_state = "ready"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #if keystroke is pressed, check if left or right and move player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = .3
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    #boundaries for player and enemies
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        if enemyX <= 0:
            enemyX_change = 0.2
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -0.2
            enemyY += enemyY_change

    #bullet movement
        if bulletY <= 0:
            bulletY = 380
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

    #collision and game over
        collide = pygame.Rect.colliderect(player_hit_box, enemy_hit_box)
        """
        if collide:
            return True
        else:
            return False
        if collide == True:
            game_over(screen)
        """

    #render
        black = pygame.Color(0,0,0)
        screen.fill (black)
        screen.blit(background, (0,0))
        playerX += playerX_change
        enemyX += enemyX_change
        player_controller(screen, playerX, playerY)
        enemy(screen, enemyX, enemyY)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()