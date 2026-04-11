import pygame
import pickle
import socket as s

pygame.init()

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('192.168.68.75', 8000))

WIDTH = 800; HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

running = True; clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, w, h, c):
        self.x, self.y = x, y
        self.width, self.height = w, h
        self.color = c

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

player = Player(100, 100, 30, 30, (255,0,0))

while running:
    player.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
    win.fill((255,255,255))
pygame.quit()
