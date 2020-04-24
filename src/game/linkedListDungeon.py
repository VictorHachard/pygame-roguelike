import pygame, sys, math, random
from settings import *
from pygame import locals as const

class Node(object):
    """docstring for Node."""

    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None
        self.left = None
        self.right = None

class Dungeon(object):
    """docstring for Dungeon."""

    def __init__(self):
        self.head = None

    def addHead(self, new):
        self.head = new

    def getHead(self):
        return self.head

    def add(self, old, new, direction):
        if direction == 'up':
            old.up = new
            new.down = old
        elif direction == 'down':
            old.down = new
            new.up = old
        elif direction == 'left':
            old.left = new
            new.right = old
        elif direction == 'right':
            old.right = new
            new.left = old

    def print(self):
        node = self.data
        prev = None
        if node.right != None:
            node = node.right
            prev = node.left
        elif node.down != None:
            node = node.down
            prev = node.up
        elif node.left != None:
            node = node.left
            prev = node.right
        elif node.up != None:
            node = node.up
            prev = node.down
        else

d = Dungeon().addHead(Node(Bonjour))
d.add(d.getHead(), Node(Salut), 'left')
d.add(d.getHead(), Node(Salut), 'left')
