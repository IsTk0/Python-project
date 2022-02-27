import pygame
import sys

pygame.init()
pygame.display.set_caption('[AS]')

speed = [2,2]
size = width, height = 1000,800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
logo = pygame.image.load("AS.png")
rect = logo.get_rect()
fps = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if rect.left < 0:
        speed[0] = -speed[0]
    if rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0:
        speed[1] = -speed[1]
    if rect.bottom > height:
        speed[1] = -speed[1]
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((200,200,200))
    screen.blit(logo, rect)
    pygame.display.update()
    clock.tick(fps)