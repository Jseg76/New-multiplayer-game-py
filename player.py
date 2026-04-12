import pygame

class Player:
    def __init__(self, x, y, w, h, c):
        self.x, self.y = x, y
        self.width, self.height = w, h
        self.color = c

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    # def update(self, win):
    #     self.draw(win)