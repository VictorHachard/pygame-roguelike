import pygame, sys, math, random
from settings import *
from pygame import locals as const

class Dungeon(object):
    """docstring for Dungeon."""

    def __init__(self):
        super(Dungeon, self).__init__()
        self.tiles = []
