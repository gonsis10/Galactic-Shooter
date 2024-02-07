import pygame
import math
from config import WIDTH, HEIGHT
from classes import Player, Crosshair

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

CROSSHAIR = pygame.sprite.GroupSingle(Crosshair())
PLAYER = pygame.sprite.GroupSingle(Player((400, 300)))
BULLETS = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            BULLETS.add(PLAYER.sprite.shoot())

    screen.fill("black")

    BULLETS.update()
    PLAYER.update()
    CROSSHAIR.update()

    BULLETS.draw(screen)
    PLAYER.draw(screen)
    CROSSHAIR.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
