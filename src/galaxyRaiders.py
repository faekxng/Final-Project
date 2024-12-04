import pygame
import random

def player_controller(screen, x, y):

    player_image = pygame.image.load('space-invaders.png')
    screen.blit(player_image, (x, y))
    

def enemy(screen, x, y, i):

    screen.blit(enemy_image[i], (x, y))
    

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
    black = pygame.Color(0,0,0)
    screen.fill (black)

#player
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0
    player_hit_box = pygame.Rect(playerX, playerY,  playerX + 64, playerY - 64)

#enemy
    enemy_image = []
    enemyX = []
    enemyY = []
    enemyX_change = [] 
    enemyY_change = []
    enemy_hit_box = []
    num_of_enemies = 6

    for i in range(num_of_enemies):
        enemy_image.append(pygame.image.load('ufo.png')) 
        enemyX.append(random.randint(0,735)) 
        enemyY.append(random.randint(50,150)) 
        enemyX_change.append(0.5) 
        enemyY_change.append(40) 
        enemy_hit_box.append(pygame.Rect(enemyX, enemyY, enemyX + 64, enemyY - 64)) 

#bullet
    global bullet_state
    bulletX = 0
    bulletY = 480
    bulletY_change = .5
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
                    fire_bullet(screen, bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        screen.blit(background, (0,0))

    #boundaries for player and enemies
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        for i in range(num_of_enemies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.2
                enemyY[i] += enemyY_change[i]
            bullet_hit_box = pygame.Rect(bulletX, bulletY, bulletX + 32, bulletY - 32)
            if bullet_hit_box.colliderect(enemy_hit_box[i]):
                bulletY = 480
                bullet_state = "ready"
                enemyX[i] = random.randint(0,735)
                enemyY[i] = random.randint(50,150)

            enemy(screen, enemyX[i], enemyY[i], i)

        
    #bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(screen, bulletX, bulletY)
            bulletY -= bulletY_change

    #collision and game over


        if enemy_hit_box.colliderect(player_hit_box):
            return True

        if enemy_hit_box.colliderect(player_hit_box) = True:
            game_over(screen)

    #render
        playerX += playerX_change
        player_controller(screen, playerX, playerY)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()