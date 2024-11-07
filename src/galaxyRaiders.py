import pygame


class PlayerController():
    def __init__(self, pos = (370, 480)):
        self.img = pygame.image.load('space-invaders.png')
        self.pos = pos

    def player():
        screen.blit(self.img, pos)



def main():
    #Initialize pygame 
    pygame.init()
    pygame.display.set_caption("Galaxy Raiders")
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution))
    running = True
    while running:
        black = pygame.Color(0,0,0)
        screen.fill (black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        PlayerController()
        pygame.display.update()


if __name__ == "__main__":
    main()