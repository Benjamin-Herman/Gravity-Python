import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, r, color, mass):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.mass = mass
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

c1 = Circle(WIDTH//2, HEIGHT//2, 60, (255,120,120), 1)
c2 = Circle(200, 150, 40, (120,255,120), 1)
c3 = Circle(600, 450, 50, (120,120,255), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 40))

    c1.draw(screen)
    c2.draw(screen)
    c3.draw(screen)

    pygame.display.flip()
