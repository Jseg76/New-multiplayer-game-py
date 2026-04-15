import pygame
import time as t
from math import sin, cos, atan2
#

class Block:
    def __init__(self, x, y, width, height, color):
        self.x, self.y = x, y
        self.w, self.h = width, height
        self.top, self.bottom = y, y + height
        self.left, self.right = x, x + width
        self.c = color

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))

class Projectile:
    def __init__(self, x, y, mouseX, mouseY, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.lifetime = 1
        self.velX = self.speed * sin(atan2(mouseX - self.x, mouseY - self.y))
        self.velY = self.speed * cos(atan2(mouseX - self.x, mouseY - self.y))

    def draw(self, win):
        pygame.draw.circle(win, (130, 130, 130), (self.x, self.y), 5)
        if -10 > self.x > win.get_width()+10 or -10 > self.y > win.get_height()+10:
            print('e')

    def checkCollide(self, groups):
        for item in groups:
            if item.left < self.x < item.right and item.top < self.y < item.bottom:
                self.lifetime = 0

    def update(self):
        self.x += self.velX
        self.y += self.velY
        if not 0 < self.x < 800 or not 0 < self.y < 600:
            self.lifetime = 0

class Player:
    def __init__(self, x, y, width, height, color):
        self.x, self.y = x, y
        self.w, self.h = width, height
        self.top, self.bottom = y, y + height
        self.left, self.right = x, x + width
        self.c = color
        self.health = 100
        self.maxHealth = 100
        self.healthBar = (self.x, self.y + 30, 40, 10)
        self.shealthBarBorder = (self.x, self.y + 32, 44, 14)
        self.velX, self.velY = 0, 0
        self.jumping = False
        self.friction = .3
        self.maxVel = 30
        self.projectiles = []
        self.shootable = True

    def shoot(self, mouseX, mouseY):
        if self.shootable:
            self.shootable = False
            self.projectiles.append(Projectile(self.x+self.w/2, self.y+self.h/2, mouseX, mouseY, 15))
            t.sleep(1)
            self.shootable = True

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
            self.jump(21)
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

    def check_collision_bottom(self, objects):
        for obj in objects:
            if obj.bottom == self.top and self.left + self.w > obj.left and self.right - self.w < obj.right:
                return True
        return False

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(win, (0, 0, 0), self.shealthBarBorder)
        pygame.draw.rect(win, (0, 255, 50), self.healthBar)

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
                self.jumping = True
            else:
                self.jumping = False
                self.velY = 0
        for i in range(-self.velY):
            if not self.check_collision_bottom(group):
                self.y -= 1
                self.top, self.bottom = self.y, self.y + self.h
            else:
                self.velY = 0

        self.healthBar = (self.x - 7.5, self.y - 18, 40 / (self.maxHealth / self.health), 6)
        self.shealthBarBorder = (self.x - 10.5, self.y - 21, 46, 12)