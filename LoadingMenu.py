import pygame as pg

from Const import *
from Text import Text

#Class đại diện cho Menu loading game
class LoadingMenu(object):
    def __init__(self, core):
        self.iTime = pg.time.get_ticks()
        self.loadingType = True
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        self.text = Text('WORLD ' + core.oWorld.get_name(), 32, (WINDOW_W / 2, WINDOW_H / 2))

#Cập nhật trạng thái của menu tải dựa trên thời gian trôi qua. 
    def update(self, core):
        if pg.time.get_ticks() >= self.iTime + (5250 if not self.loadingType else 2500):
            if self.loadingType:
                core.oMM.currentGameState = 'Game'
                core.get_sound().play('overworld', 999999, 0.5)
                core.get_map().in_event = False
            else:
                core.oMM.currentGameState = 'MainMenu'
                self.set_text_and_type('WORLD ' + core.oWorld.get_name(), True)
                core.get_map().reset(True)

#Đặt lại văn bản và loại của menu tải
    def set_text_and_type(self, text, type):
        self.text = Text(text, 32, (WINDOW_W / 2, WINDOW_H / 2))
        self.loadingType = type

#Vẽ menu tải lên màn hình bằng cách sử dụng các hình ảnh và văn bản được thiết lập trước đó.
    def render(self, core):
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

#Cập nhật thời gian bắt đầu của menu tải, thường được gọi khi cần đặt lại thời gian đếm ngược.
    def update_time(self):
        self.iTime = pg.time.get_ticks()
