import pygame
import sys

# ----- INIT CODE - THE WINDOW ------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#---- Circle pos, size, colour ------
x = WIDTH // 2
y = HEIGHT // 2
r = 60
color = (255, 120, 120)

while True:
    for event in pygame.event.get():
        #get input to quit and any others
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill the screen to reset
    screen.fill((30, 30, 40))
    #draw circle
    pygame.draw.circle(screen, color, (x, y), r)

    pygame.display.flip()
