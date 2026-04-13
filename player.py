import pygame

class Block:
    def __init__(self, x, y, width, height, color):
        self.x, self.y = x, y
        self.w, self.h = width, height
        self.top, self.bottom = y, y + height
        self.left, self.right = x, x + width
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
            self.velY = -strength

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
            self.velY += 2

    def check_collision_top(self, objects):
        for obj in objects:
            if obj.y == self.bottom and self.left + self.w > obj.left and self.right - self.w < obj.right:
                    return True
        return False

    def check_collision_right(self, objects):
        for obj in objects:
            if obj.left == self.right and self.top + self.h > obj.top and self.bottom - self.h < obj.bottom:
                    return True
        return False

    def check_collision_left(self, objects):
        for obj in objects:
            if obj.right == self.left and self.top + self.h > obj.top and self.bottom - self.h < obj.bottom:
                return True
        return False

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))

    def update(self, group):
        self.move_x()
        for i in range(int(round(self.velX))):
            if not self.check_collision_right(group):
                self.x += 1
                self.left, self.right = self.x, self.x + self.w
        for i in range(int(round(-self.velX))):
            if not self.check_collision_left(group):
                self.x -= 1
                self.left, self.right = self.x, self.x + self.w
        self.velX = self.velX * self.friction

        self.move_y()
        for i in range(self.velY):
            if not self.check_collision_top(group):
                self.y += 1
                self.top, self.bottom = self.y, self.y + self.h
            else:
                self.jumping = False
                self.velY = 0
        for i in range(-self.velY):
            self.y -= 1
            self.top, self.bottom = self.y, self.y + self.h