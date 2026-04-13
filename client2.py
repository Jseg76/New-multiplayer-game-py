#variables are camelCase
#functions are under_score
#please and thank you
#

import pygame
import pickle
import socket as s
from player import Player, Block

WIDTH = 800; HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('192.168.68.74', 8000))

running = True; clock = pygame.time.Clock()

players = []
player = Player(100, 100, 30, 30, (0,0,255))

testBlock = Block(400, 400, 50, 100, (0,0,0))
floor = Block(0, 500, 800, 100, (153, 142, 104))
blocks = [floor,
          testBlock,]

while running:
    print(player.jumping)
    try:
        client.send(pickle.dumps(player))
        players = pickle.loads(client.recv(2048))
    except:
        ...
    for block in blocks:
        block.draw(win)

    player.update()
    for p in players:
        try:
            p.draw(win)
        except:
            ...

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
    win.fill((255,255,255))
pygame.quit()