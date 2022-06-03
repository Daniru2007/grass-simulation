import pygame
import sys
from engine import Entity
pygame.init()

WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Grass Simulation')

clock = pygame.time.Clock()

player = Entity(10, 10, 16, 16, "player")
player.load_animations("animations/player.json")
player.set_action("idle")

tiles = []
for i in range(30):
    tiles.append(["1", pygame.Rect(i * 16, 250, 16, 16)])
running = True
while running:
    player.gravity += 0.2
    if player.gravity > 2:
        player.gravity = 2



    player.air_time += 1
    player.movement = [0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.air_time < 6:
                    player.gravity = -3
            if event.key == pygame.K_RIGHT:
                player.right = True
            if event.key == pygame.K_LEFT:
                player.left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.right = False
            if event.key == pygame.K_LEFT:
                player.left = False
    player.movement[1] = player.gravity
    screen.fill((0, 0, 0))
    if player.right:
        player.movement[0] = 3
    if player.left:
        player.movement[0] = -3
    for tile in tiles:
        screen.blit(pygame.image.load("imgs/ground.png"), tile[1])

    collisions = player.move(tiles)
    if collisions["bottom"]:
        player.gravity = 0
        player.air_time = 0
    player.display(screen, [0, 0])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
sys.exit()
