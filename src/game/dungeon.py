import pygame, sys, math, random, copy
from settings import *
from pygame import locals as const
from gameGraphicElements.sprites import *

class Dungeon(object):
    """docstring for Dungeon."""

    def __init__(self, game):
        super(Dungeon, self).__init__()
        self.dungeon = []
        self.game = game

    def getDungeon(self):
        return self.dungeon

    def getPlayer(self):
        return self.player

    def newPlayer(self):
        dungeon = self.dungeon[self.dungeonSize // 2][self.dungeonSize // 2][0]
        for j in range(TILESIZE):
            for i in range(TILESIZE):
                for case in dungeon[j][i]:
                    if isinstance(case, Floor):
                        self.player = Player(self.game, ((self.dungeonSize) // 2) * TILESIZE + i, ((self.dungeonSize) // 2) * TILESIZE + j)
                        return

    def new(self, dungeonSize):
        #print("\n-------------------")
        #print("dungeonSize " + str(dungeonSize))
        self.dungeon.clear()
        self.dungeonSize = dungeonSize
        adjacent = []
        adjacent.append(((self.dungeonSize) // 2, (self.dungeonSize) // 2))
        #print("adjacent " + str(adjacent))
        for j in range(self.dungeonSize):
            self.dungeon.append([])
            for i in range(self.dungeonSize):
                self.dungeon[j].append([])
        dungeonSizeItr = self.dungeonSize
        #print("dungeon " + str(self.dungeon))
        while dungeonSizeItr >= 0:
            #print(adjacent)
            index = random.randint(0, len(adjacent)-1)
            point = adjacent[index]
            del adjacent[index]
            if point[0] -1 >= 0 and not self.dungeon[point[0] -1][point[1]]:
                adjacent.append((point[0] -1, point[1]))
            if point[0] +1 < dungeonSize and not self.dungeon[point[0] +1][point[1]]:
                adjacent.append((point[0] +1, point[1]))
            if point[1] -1 >= 0 and not self.dungeon[point[0]][point[1] -1]:
                adjacent.append((point[0], point[1] -1))
            if point[1] +1 < dungeonSize and not self.dungeon[point[0]][point[1] +1]:
                adjacent.append((point[0], point[1] +1))
            self.dungeon[point[0]][point[1]].append(copy.deepcopy(random.choice(MAPS)))
            #print(point)
            #print(self.dungeon[point[0]][point[1]])
            dungeonSizeItr -= 1
        for j in range(self.dungeonSize):
            for i in range(self.dungeonSize):
                if self.dungeon[j][i]:
                    dungeon = self.dungeon[j][i][0]
                    if j -1 < 0 or not self.dungeon[j - 1][i]: #top
                        for n in range(6, 10):
                            dungeon[0][n].remove(0)
                            dungeon[0][n].append(2)
                    if j +1 >= dungeonSize or not self.dungeon[j + 1][i]: #down
                        for n in range(6, 10):
                            dungeon[TILESIZE -1][n].remove(0)
                            dungeon[TILESIZE -1][n].append(2)
                    if i -1 < 0 or not self.dungeon[j][i - 1]: #left
                        for n in range(6, 10):
                            dungeon[n][0].remove(0)
                            dungeon[n][0].append(2)
                    if i +1 >= dungeonSize or not self.dungeon[j][i + 1]: #right
                        for n in range(6, 10):
                            dungeon[n][TILESIZE -1].remove(0)
                            dungeon[n][TILESIZE -1].append(2)
        #change int to object
        offseti, offsetj = 0, 0
        for jd in range(self.dungeonSize):
            for id in range(self.dungeonSize):
                dungeon = self.dungeon[jd][id]
                if dungeon:
                    dungeon = dungeon[0]
                    for j in range(TILESIZE):
                        for i in range(TILESIZE):
                            tmp = []
                            for case in dungeon[j][i]:
                                if case == 1 or case == 2:
                                    tmp.append(Wall(self.game, i + offseti, j + offsetj))
                                elif case == 0:
                                    tmp.append(Floor(self.game, i + offseti, j + offsetj))
                                elif case == 3:
                                    tmp.append(Enemy(self.game, i + offseti, j + offsetj))
                            dungeon[j][i].clear()
                            dungeon[j][i] = tmp
                offseti += TILESIZE
            offsetj += TILESIZE
            offseti = 0
        self.newPlayer()
