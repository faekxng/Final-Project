import pygame


def player_controller(screen):
        player_image = pygame.image.load('space-invaders.png')
        playerX = 370
        playerY = 480
        playerX_change = 0
        playerY_change = 0
        screen.blit(player_image, (playerX, playerY))

#if keystroke is pressed, check if left or right
def button_pressed(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
        playerX += playerX_change
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        playerX += playerX_change



def main():
    #Initialize pygame 
    pygame.init()
    pygame.display.set_caption("Galaxy Raiders")
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0,0,0)
        screen.fill (black)
        player_controller(screen)
        button_pressed(event)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()