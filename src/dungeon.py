import pygame, sys, math, random, copy
from settings import *
from pygame import locals as const
from sprites import *

class Dungeon(object):
    """docstring for Dungeon."""

    def __init__(self, main):
        super(Dungeon, self).__init__()
        self.dungeon = []
        self.main = main

    def getDungeon(self):
        return self.dungeon

    def player(self):
        return Player(self.main, ((self.dungeonSize) // 2) * TILESIZE + 1, ((self.dungeonSize) // 2) * TILESIZE + 1)

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
                    if j -1 < 0 or not self.dungeon[j -1][i]: #top
                        for n in range(6, 10):
                            dungeon[0][n] = 2
                    if j +1 >= dungeonSize or not self.dungeon[j +1][i]: #down
                        for n in range(6, 10):
                            dungeon[TILESIZE -1][n] = 2
                    if i -1 < 0 or not self.dungeon[j][i -1]: #left
                        for n in range(6, 10):
                            dungeon[n][0] = 2
                    if i +1 >= dungeonSize or not self.dungeon[j][i +1]: #right
                        for n in range(6, 10):
                            dungeon[n][TILESIZE -1] = 2
        #change int to object
        offseti, offsetj = 0, 0
        for jd in range(self.dungeonSize):
            for id in range(self.dungeonSize):
                dungeon = self.dungeon[jd][id]
                if dungeon:
                    dungeon = dungeon[0]
                    for j in range(TILESIZE):
                        for i in range(TILESIZE):
                            if dungeon[j][i] == 1 or dungeon[j][i] == 2:
                                dungeon[j][i] = Wall(self.main, i + offseti, j + offsetj)
                            elif dungeon[j][i] == 0:
                                dungeon[j][i] = Floor(self.main, i + offseti, j + offsetj)
                offseti += TILESIZE
            offsetj += TILESIZE
            offseti = 0

    def event(self, mouse):
        return
        pos = mouse.get_pos()
        if self.dungeon:
            offseti, offsetj = 0, 0
            for jd in range(self.dungeonSize):
                for id in range(self.dungeonSize):
                    dungeon = self.dungeon[jd][id]
                    if dungeon:
                        dungeon = dungeon[0]
                        ti, tj = 0, 0
                        for j in range(TILESIZE):
                            for i in range(TILESIZE):
                                if pos[0] < ti + offseti + TILESIZE and pos[0] + TILESIZE > ti + offseti and pos[1] < tj + offsetj + TILESIZE and pos[1] + TILESIZE > tj + offsetj:
                                    dungeon[j][i] = 1
                                    print(dungeon)
                                    return
                                ti += TILESIZE
                            tj += TILESIZE
                            ti = 0
                    offseti += TILESIZE * TILESIZE
                offsetj += TILESIZE * TILESIZE
                offseti = 0


    def render(self, screen):
        if self.dungeon:
            offseti, offsetj = 0, 0
            for jd in range(self.dungeonSize):
                for id in range(self.dungeonSize):
                    dungeon = self.dungeon[jd][id]
                    if dungeon:
                        dungeon = dungeon[0]
                        ti, tj = 0, 0
                        for j in range(TILESIZE):
                            for i in range(TILESIZE):
                                if dungeon[j][i] == 1:
                                    pygame.draw.rect(screen, DARKGREY, (ti + offseti, tj + offsetj, TILESIZE, TILESIZE))
                                elif dungeon[j][i] == 2:
                                    pygame.draw.rect(screen, BLUE, (ti + offseti, tj + offsetj, TILESIZE, TILESIZE))
                                elif dungeon[j][i] == 0:
                                    pygame.draw.rect(screen, WHITE, (ti + offseti, tj + offsetj, TILESIZE, TILESIZE))
                                ti += TILESIZE
                            tj += TILESIZE
                            ti = 0
                    offseti += TILESIZE * TILESIZE
                offsetj += TILESIZE * TILESIZE
                offseti = 0
