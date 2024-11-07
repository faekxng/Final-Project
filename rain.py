import random
import pygame
import math


class Particle():

    def __init__(self, pos = (0,0), size = 15, life = 1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(random.randrange(0,256),random.randrange(0,256), random.randrange(0,256))
        self.alpha = 255
        self.life = life
        self.age = 0
        self.surface = self.update_surface()
        self.dead = False

    def update_surface(self):
        surf = pygame.Surface((self.size * 0.8, self.size * 0.8))
        surf.fill(self.color)
        return surf

    def update (self, dt):
        self.age += dt
        self.alpha = 255 * (math.sin(math.radians(self.age))+1)/2
        if self.age > self.life:
            self.dead = True
            self.apha = 255 * (1- (self.age/self.life))

    def draw(self, surface):
        surface.blit(self.surface, self.pos)
        

class ParticleTrail():
    
    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles = []

    def update(self, dt):
        particle = Particle(self.pos, size = self.size, life = self.life)
        self.particles.insert(0, particle)
        self._update_particles(dt)
        self._update_pos()

    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def _update_pos(self):
        x,y = self.pos
        y += self.size
        self.pos = (x,y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

class Rain():

    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.particle_size = 15
        self._birth_rate = 1
        self.trails = []

    def _birth_new_trails(self):
        for count in range (self._birth_rate):
            screen_width = self.screen_res[0]
            x = random.randrange(0, screen_width, self.particle_size)
            pos = (x,0)
            life = random.randrange(500,800)
            trail = ParticleTrail(pos, self.particle_size, life)
            self.trails.insert(0, trail)
    
    def update(self, dt):
        self._birth_new_trails()
        self.update_trails(dt)

    def update_trails(self, dt):
        for idx, trail in enumerate(self.trails):
            trail.update(dt)
            if self._trail_is_offscreen(trail):
                del self.trails[idx]

    def _trail_is_offscreen(self, trail):
        tail_is_offscreen = trail.particles[-1].pos[1] > self.screen_res[1]
        return tail_is_offscreen

    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)

def mouseClickedDraw(screen):
    mouse_pos = pygame.mouse.get_pos()
    color = pygame.Color(random.randrange(0,256),random.randrange(0,256), random.randrange(0,256))
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(screen, color, mouse_pos, 20)
        



def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode((resolution), pygame.FULLSCREEN)
    rain = Rain(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        rain.draw(screen)
        mouseClickedDraw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()
        
if __name__ == "__main__":
    main()