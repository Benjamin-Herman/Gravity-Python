import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, r, color, mass, velx = 0, vely = 0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.mass = mass
        self.velocityx = velx
        self.velocityy = vely
        self.accelerationx = 0
        self.accelerationy = 0

    def draw(self, screen):
        self.velocityx += self.accelerationx
        self.velocityy += self.accelerationy
        self.x += self.velocityx
        self.y += self.velocityy
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r)

def update(circles):
    G = 0.4
    for c in circles:
        c.accelerationx = 0
        c.accelerationy = 0

    for i in range(len(circles)):
        for j in range(i+1, len(circles)):
            a = circles[i]
            b = circles[j]
            dx = b.x - a.x
            dy = b.y - a.y
            dist = math.sqrt(dx*dx + dy*dy) + 0.001
            force = G * a.mass * b.mass / (dist * dist)
            ax = force * dx / dist
            ay = force * dy / dist
            a.accelerationx += ax / a.mass
            a.accelerationy += ay / a.mass
            b.accelerationx -= ax / b.mass
            b.accelerationy -= ay / b.mass

circles = []
c1 = Circle(WIDTH//2, HEIGHT//2, 60, (255,120,120), 500, 0, 0)
c2 = Circle(200, 150, 40, (120,255,120), 10, 2.5, -1)
c3 = Circle(600, 450, 50, (120,120,255), 5, -2.5, 2)
circles.append(c1)
circles.append(c2)
circles.append(c3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update(circles)
    screen.fill((30, 30, 40))

    for c in circles:
        c.draw(screen)

    pygame.display.flip()
    clock.tick(60)
