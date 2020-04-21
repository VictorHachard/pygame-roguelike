import pygame, sys, math, random
from settings import *
from pygame import locals as const
from menu import Menu
from game import Game

class MainMenu(object):
    """docstring for MainMenu."""

    def __init__(self, main, screen):
        self.main = main
        self.screen = screen
        self.new()

    def new(self):
        self.mainMenu = Menu(self.screen, 3).addText('roro', 60).addButton('Play', 'p').addButton('Quit', 'q')

    def update(self):
        pass

    def draw(self):
        self.mainMenu.render()

    def events(self, event):
        res = self.mainMenu.update(event)
        if res == 'p':
            self.main.getTask('game')[2] = Game(self.main, self.screen)
            self.main.change = 'game'
        elif res == 'q':
            self.main.running = False
