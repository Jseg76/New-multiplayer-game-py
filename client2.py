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
client.connect(('127.0.0.1', 8000))

running = True; clock = pygame.time.Clock()

players = []
player = Player(637, 100, 30, 30, (255,0,0))

centralBlock = Block(350, 380, 100, 120, (0,0,0))
topLeftPlatform = Block(100, 260, 100, 20, (0, 0, 0))
bottomLeftPlatform = Block(100, 400, 100, 20, (0, 0, 0))
topRightPlatform = Block(600, 260, 100, 20, (0, 0, 0))
bottomRightPlatform = Block(600, 400, 100, 20, (0, 0, 0))
floor = Block(0, 500, 800, 100, (153, 142, 104))
blocks = [floor,
          centralBlock,
          bottomLeftPlatform,
          topLeftPlatform,
          bottomRightPlatform,
          topRightPlatform,]

while running:
    print(player.jumping)
    try:
        client.send(pickle.dumps(player))
        players = pickle.loads(client.recv(2048))
    except:
        ...
    for block in blocks:
        block.draw(win)

    player.update(blocks)
    for p in players:
        try:
            p.draw(win)
        except:
            ...

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            elif event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()
    clock.tick(60)
    win.fill((255,255,255))
pygame.quit()