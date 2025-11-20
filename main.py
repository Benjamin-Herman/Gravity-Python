import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


G = 0.1      
DT = 0.1     


class Circle:
    def __init__(self, x, y, r, color, mass, velx=0, vely=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.mass = mass

        self.vx = velx
        self.vy = vely

        self.ax = 0
        self.ay = 0

    def apply_accel(self):
        """Update velocity & position."""
        self.vx += self.ax * DT
        self.vy += self.ay * DT

        self.x += self.vx * DT
        self.y += self.vy * DT

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r)


        ACCEL_SCALE = 2  

        ax = self.ax * ACCEL_SCALE
        ay = self.ay * ACCEL_SCALE

        start = (int(self.x), int(self.y))
        end = (int(self.x + ax), int(self.y + ay))

        pygame.draw.line(screen, (255, 255, 255), start, end, 2)

        angle = math.atan2(ay, ax)
        ah = 8  
        left = (int(end[0] - ah * math.cos(angle - 0.4)),
                int(end[1] - ah * math.sin(angle - 0.4)))
        right = (int(end[0] - ah * math.cos(angle + 0.4)),
                 int(end[1] - ah * math.sin(angle + 0.4)))

        pygame.draw.polygon(screen, (255, 255, 255), [end, left, right])

        mag = math.sqrt(self.ax * self.ax + self.ay * self.ay)
        text = font.render(f"{mag:.2f}", True, (255, 255, 255))
        screen.blit(text, (self.x + self.r + 5, self.y - self.r - 5))


def update_gravity(circles):
    """Computes gravitational acceleration between all circles."""

    for c in circles:
        c.ax = 0
        c.ay = 0

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            a = circles[i]
            b = circles[j]

            dx = b.x - a.x
            dy = b.y - a.y
            dist = math.sqrt(dx*dx + dy*dy) + 0.001

            F = G * a.mass * b.mass / (dist * dist)

            ux = dx / dist
            uy = dy / dist

            a.ax += (F * ux) / a.mass
            a.ay += (F * uy) / a.mass

            b.ax -= (F * ux) / b.mass
            b.ay -= (F * uy) / b.mass


font = pygame.font.SysFont("consolas", 15)

circles = []

sun = Circle(WIDTH//2, HEIGHT//2, 30, (255, 255, 120), 9000000, 0, 0)
planet1 = Circle(WIDTH//2 + 200, HEIGHT//2, 12, (120, 255, 120), 15, 0, 65)
planet2 = Circle(WIDTH//2 - 300, HEIGHT//2, 10, (120, 120, 255), 8, 0, -52)
planet3 = Circle(WIDTH//2, HEIGHT//2 + 250, 12, (255, 120, 120), 10, -70, 0)

circles += [sun, planet1, planet2, planet3]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((20, 20, 30))

    update_gravity(circles)

    for c in circles:
        c.apply_accel()
        c.draw(screen)

    pygame.display.flip()
    clock.tick(60)
