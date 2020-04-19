import pygame, sys, math, random, copy
from settings import *
from pygame import locals as const

class Player(pygame.sprite.Sprite):
    """docstring for Player."""

    def __init__(self, main, x, y):
        self.groups = main.sprites
        self.main = main
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.main.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def move(self, dx = 0, dy = 0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
    """docstring for Wall."""

    def __init__(self, main, x, y):
        self.groups = main.sprites, main.walls
        self.main = main
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Floor(pygame.sprite.Sprite):
    """docstring for Floor."""

    def __init__(self, main, x, y):
        self.groups = main.sprites, main.floors
        self.main = main
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
