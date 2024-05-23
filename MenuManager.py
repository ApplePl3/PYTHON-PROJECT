import pygame as pg

from LoadingMenu import LoadingMenu
from MainMenu import MainMenu


class MenuManager(object):
    """

    Lớp đó cho phép dễ dàng xử lý trạng thái trò chơi. Tùy thuộc vào tình hình, nó cập nhật và vẽ những cái khác nhau.

    """
    def __init__(self, core):

        self.currentGameState = 'MainMenu'

        self.oMainMenu = MainMenu()
        self.oLoadingMenu = LoadingMenu(core)

    def update(self, core):
        if self.currentGameState == 'MainMenu':
            pass

        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.update(core)

        elif self.currentGameState == 'Game':
            core.get_map().update(core)

    def render(self, core):
        if self.currentGameState == 'MainMenu':
            core.get_map().render_map(core)
            self.oMainMenu.render(core)

        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.render(core)

        elif self.currentGameState == 'Game':
            core.get_map().render(core)
            core.get_map().get_ui().render(core)

        pg.display.update()

    def start_loading(self):
            # bắt đầu load level
            self.currentGameState = 'Loading'
            self.oLoadingMenu.update_time()
