from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens import InScreen, GameScreen


class NSApp(MDApp):
    manager = ScreenManager(transition=NoTransition())
    screens = list()

    def build(self):
        self.title = 'УГАДАЙ ЧИСЛО'
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Amber'
        self.theme_cls.theme_style = 'Dark'
        self.kvs_loader()
        self.screens.append(InScreen(name='in_scr'))
        self.screens.append(GameScreen(name='game_scr'))
        for scr in self.screens:
            self.manager.add_widget(scr)
        self.manager.current = 'in_scr'
        return self.manager

    def kvs_loader(self):
        Builder.load_file('screens/inscreen.kv')
        Builder.load_file('screens/gamescreen.kv')


if __name__ == '__main__':
    NSApp().run()