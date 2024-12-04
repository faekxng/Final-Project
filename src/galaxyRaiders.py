import pygame
import random

def player_controller(screen, playerX, playerY):

    player_image = pygame.image.load('space-invaders.png')
    screen.blit(player_image, (playerX, playerY))
    player_hit_box = Rect(playerX + 64, playerY - 64)


def enemy(screen, enemyX, enemyY):

    enemy_image = pygame.image.load('ufo.png')
    screen.blit(enemy_image, (enemyX, enemyY))
    enemy_hit_box = Rect(enemyX + 64, enemyY - 64)


def fire_bullet(screen, playerX, playerY):  
    
    global bullet_state
    bullet_image = pygame.image.load('paintball.png')
    bullet_state = "fire"
    screen.blit(bullet_image, (playerX + 16, playerY + 10))

def game_over():
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
    player_hit_box = Rect(playerX + 64, playerY - 64)
#enemy
    enemyX = random.randint(0,800)
    enemyY = random.randint(50,150)
    enemyX_change = 0.3 
    enemyY_change = 40
    enemy_hit_box = Rect(enemyX + 64, enemyY - 64)
#bullet
    bulletY = 480
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
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(screen, playerX, playerY)
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
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
    #collision and game over
        collide = pygame.Rect.colliderect(player_hit_box, enemy_hit_box)
        if collide:
            gameOver = True
            return gameOver
        if gameOver = True:
            game_over()
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