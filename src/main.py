import pygame, json, sys
from os import path
from settings import *
from pygame import locals as const
from game.game import Game
from menus.mainMenu import MainMenu

class Main(object):
    """docstring for Main."""

    def __init__(self, args):
        if 'test' in args:
            self.test = True
            print("Test Mode:\n")
            return
        else:
            self.test = False
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
        self.change = ''
        self.tasks = []
        self.tasks.append(['mainMenu', True, MainMenu(self, self.screen)])
        self.tasks.append(['game', False, None])

    def getTask(self, id):
        for task in self.tasks:
            if task[0] == id:
                return task

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0
            if self.change != '':
                self.getTask(self.change)[1] = not task[1]
                self.change = ''
            for task in self.tasks:
                if task[1]:
                    self.events(task[2])
                    if self.change != '':
                        task[1] = not task[1]
                    self.update(task[2])
                    self.draw(task[2])

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self, task):
        task.update()

    def draw(self, task):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BLACK)
        task.draw()
        pygame.display.flip()

    def events(self, task):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            task.events(event)

m = Main(sys.argv)
if not m.test:
    m.new()
    m.run()
