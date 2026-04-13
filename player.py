import pygame
# #

class Block:
    def __init__(self, x, y, width, height, color):
        self.x, self.y = x, y
        self.w, self.h = width, height
        self.c = color

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))

class Player:
    def __init__(self, x, y, width, height, color):
        self.x, self.y = x, y
        self.w, self.h = width, height
        self.top, self.bottom = y, y + height
        self.left, self.right = x, x + width
        self.c = color
        self.velX, self.velY = 0, 0
        self.jumping = False
        self.friction = 0.9
        self.maxVel = 30

    def jump(self, strength):
        if not self.jumping:
            self.jumping = True
            self.velY -= strength

    def move_x(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.velX = -5
        if keys[pygame.K_d]:
            self.velX = 5

    def move_y(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.jump(25)
        if abs(self.velY) <= self.maxVel:
            self.velY += .5

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))

    def update(self):
        self.move_x()
        self.x += self.velX
        self.velX = self.velX * self.friction
        self.move_y()
        self.y += self.velY