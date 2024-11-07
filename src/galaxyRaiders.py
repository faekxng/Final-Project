import pygame


def player_controller(screen):
        player_image = pygame.image.load('space-invaders.png')
        playerX = 370
        playerY = 480
        screen.blit(player_image, (playerX, playerY))

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
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()