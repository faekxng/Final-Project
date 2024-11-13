import pygame


def player_controller(screen, playerX, playerY):
        player_image = pygame.image.load('space-invaders.png')
        screen.blit(player_image, (playerX, playerY))



def main():
    #Initialize pygame 
    pygame.init()
    pygame.display.set_caption("Galaxy Raiders")
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution))
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    #if keystroke is pressed, check if left or right and move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
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
        playerX += playerX_change
        player_controller(screen, playerX, playerY)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()