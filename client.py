#variables are camelCase
#functions are under_score
#please and thank you

import pygame
import pickle
import socket as s
from player import Player, Block

WIDTH = 800; HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

pygame.init()

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('10.218.144.50', 8000))

running = True; clock = pygame.time.Clock()

players = []
player = Player(137, 100, 25, 25, (255,0,0))

centralBlock = Block(350, 410, 100, 90, (0,0,0))
topLeftPlatform = Block(100, 275, 80, 20, (0, 0, 0))
middleLeftPlatform = Block(200, 350, 80, 20, (0, 0, 0))
bottomLeftPlatform = Block(100, 425, 80, 20, (0, 0, 0))
topRightPlatform = Block(620, 275, 80, 20, (0, 0, 0))
middleRightPlatform = Block(520, 350, 80, 20, (0, 0, 0))
bottomRightPlatform = Block(620, 425, 80, 20, (0, 0, 0))
floor = Block(0, 500, 800, 100, (153, 142, 104))
blocks = [floor,
          centralBlock,
          bottomLeftPlatform,
          middleLeftPlatform,
          topLeftPlatform,
          bottomRightPlatform,
          middleRightPlatform,
          topRightPlatform,
          ]

while running:
    try:
        client.send(pickle.dumps(player))
        players = pickle.loads(client.recv(2048))
    except:
        ...
    for block in blocks:
        block.draw(win)
    mouseX, mouseY = pygame.mouse.get_pos()

    player.update(blocks)
    for p in players:
        try:
            p.draw(win)
            for proj in p.projectiles:
                proj.draw(win)
        except:
            ...
    for proj in player.projectiles:
        proj.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.shoot(mouseX, mouseY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            elif event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    clock.tick(60)
    win.fill((255,255,255))
pygame.quit()