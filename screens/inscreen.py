from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog


class InScreen(MDScreen):
    first_name = None
    second_name = None
    state = False

    def settings_dlg(self):
    	# Function to make settings dialog, like different ranges to play
	    pass

    def check(self):
        app = MDApp.get_running_app()
        if self.first_name and self.second_name:
            if self.first_name != self.second_name:
                self.ids.play_btn.disabled = False
                self.ids.info_lbl.text_color = app.theme_cls.accent_dark
                self.ids.info_lbl.text = 'Играть!'
                self.state = True
        elif self.first_name == '' or self.second_name == '':
            self.ids.play_btn.disabled = True
            self.ids.info_lbl.text = 'Пожалуйста, введите имена игроков!'
            self.state = False
        if self.first_name == self.second_name:
            self.ids.play_btn.disabled = True
            self.ids.info_lbl.text = '[color=#fa2132]Имена игроков должны отличаться![/color]'
            self.state = False

    def go_on(self):
        if self.state:
            anim = Animation(size_hint=(5, 5), opacity=0)
            anim.bind(on_progress=self.animator, on_complete=self.anim_finisher)
            anim.start(self.ids.intro_lay)

    def animator(self, *args):
        self.ids.intro_lay.center = Window.center

    def anim_finisher(self, *args):
        self.manager.current = 'game_scr'