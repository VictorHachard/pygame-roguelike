import pygame, json
import sys
from os import path
from settings import *
from pygame import locals as const
from game import Game
from dungeon import Dungeon

class Main(object):
    """docstring for Main."""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        imgage_folder = path.join(game_folder, 'imgage')
        sound_folder = path.join(game_folder, 'sound')
        music_folder = path.join(game_folder, 'music')
        # Load a ton of stuff
        with open('maps.json') as f:
            data = json.load(f)
        m = 0
        for map in data:
            MAPS.append([])
            n = 0
            for j in range(TILESIZE):
                MAPS[m].append([])
                for i in range(TILESIZE):
                    MAPS[m][j].append(data.get(str(map))[n])
                    n += 1
            m += 1

    def new(self):
        self.draw_debug = False
        self.paused = False

        # self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        if self.draw_debug:
            pass

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug


m = Main()
while True:
    m.new()
    m.run()
