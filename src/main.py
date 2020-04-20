import pygame, json
import sys
from os import path
from settings import *
from pygame import locals as const
from game import Game
from dungeon import Dungeon
from tilemap import *
from sprites import *

class Main(object):
    """docstring for Main."""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
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
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.camera = Camera(16 * 16 * 5, 16 * 16 * 5)
        self.d = Dungeon(self)
        self.d.new(5)
        self.player = self.d.player()

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
        self.sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BLACK)
        for sprite in self.sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_F1:
                    self.sprites = pygame.sprite.Group()
                    self.walls = pygame.sprite.Group()
                    self.floors = pygame.sprite.Group()
                    self.camera = Camera(16 * 16 * 5, 16 * 16 * 5)
                    self.d = Dungeon(self)
                    self.d.new(5)
                    self.player = self.d.player()
                if event.key == pygame.K_LEFT:
                    self.player.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.player.move(1, 0)
                if event.key == pygame.K_UP:
                    self.player.move(0, -1)
                if event.key == pygame.K_DOWN:
                    self.player.move(0, 1)
            if event.type == pygame.MOUSEBUTTONUP:
                pass

m = Main()
#while True:
m.new()
m.run()
