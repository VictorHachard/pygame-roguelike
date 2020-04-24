import pygame, sys, math, random
from settings import *
from pygame import locals as const
from game.dungeon import Dungeon
from gameGraphicElements.tilemap import *
from gameGraphicElements.sprites import *

class Game(object):
    """docstring for Game."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        self.sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.camera = Camera(16 * 16 * 5, 16 * 16 * 5)
        self.d = Dungeon(self)
        self.d.new(5)
        self.player = self.d.getPlayer()

    def update(self):
        self.sprites.update()
        self.camera.update(self.player)

    def draw(self):
        for sprite in self.sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.new()
            if event.key == pygame.K_LEFT:
                self.player.move(-1, 0)
            if event.key == pygame.K_RIGHT:
                self.player.move(1, 0)
            if event.key == pygame.K_UP:
                self.player.move(0, -1)
            if event.key == pygame.K_DOWN:
                self.player.move(0, 1)
