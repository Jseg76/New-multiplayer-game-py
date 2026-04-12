#variables are camelCase
#functions are under_score
#please and thank you

import pygame
import pickle
import socket as s
from player import Player

WIDTH = 800; HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('192.168.68.74', 8000))

running = True; clock = pygame.time.Clock()

players = []
player = Player(100, 100, 30, 30, (255,0,255))

while running:
    try:
        client.send(pickle.dumps(player))
        players = pickle.loads(client.recv(2048))
    except:
        print("Failed")

    player.move()
    for p in players:
            p.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
    win.fill((255,255,255))
pygame.quit()
