from os import environ

import pygame as pg
from pygame.locals import *

from Const import *
from Map import Map
from MenuManager import MenuManager
from Sound import Sound

#Lớp core

class Core(object):
    # Lớp init dùng để thiết lập môi trường, âm thanh, thiết lập các cấu hình cho cửa sổ trò chơi.
    def __init__(self):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Super Mario Bros')
        pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.oWorld = Map('1-1')
        self.oSound = Sound()
        self.oMM = MenuManager(self)

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False

#Vòng lặp xử lý đầu vào
    def main_loop(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

#Xử lý đầu vào trong trò chơi
    def input(self):
        if self.get_mm().currentGameState == 'Game':
            self.input_player()
        else:
            self.input_menu()

#Xử lý các sự kiện trong trò chơi
    def input_player(self):
        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.keyR = True
                elif e.key == K_LEFT:
                    self.keyL = True
                elif e.key == K_DOWN:
                    self.keyD = True
                elif e.key == K_UP:
                    self.keyU = True
                elif e.key == K_LSHIFT:
                    self.keyShift = True

            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.keyR = False
                elif e.key == K_LEFT:
                    self.keyL = False
                elif e.key == K_DOWN:
                    self.keyD = False
                elif e.key == K_UP:
                    self.keyU = False
                elif e.key == K_LSHIFT:
                    self.keyShift = False

#xử lý các phím trong trò chơi
    def input_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.get_mm().start_loading()

#Cập nhật trạng thái của trò chơi
    def update(self):
        self.get_mm().update(self)

#Vẽ lại màn hình trò chơi
    def render(self):
        self.get_mm().render(self)

#Bản đồ
    def get_map(self):
        return self.oWorld

#Menu
    def get_mm(self):
        return self.oMM

#Âm thanh
    def get_sound(self):
        return self.oSound
