from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from screens import InScreen, GameScreen


class NSApp(MDApp):
    manager = ScreenManager(transition=NoTransition())
    screens = list()

    def build(self):
        self.title = 'УГАДАЙ ЧИСЛО'
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Yellow'
        self.theme_cls.theme_style = 'Dark'
        self.kvs_loader()
        config = self.config
        self.screens.append(InScreen(name='in_scr'))
        self.screens.append(GameScreen(name='game_scr'))
        for scr in self.screens:
            self.manager.add_widget(scr)
        self.manager.current = 'in_scr'
        return self.manager

    def kvs_loader(self):
        Builder.load_file('screens/inscreen.kv')
        Builder.load_file('screens/gamescreen.kv')

    def build_config(self, config):
        config.setdefaults('Game Settings', {
            'min number': 0,
        })

    def on_stop(self):
        print(self.screens[1].number)
        print(self.screens[1].players_attempts)


if __name__ == '__main__':
    NSApp().run()