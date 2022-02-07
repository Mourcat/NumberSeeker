from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from random import randrange


class GameScreen(MDScreen):
    number = None
    first_player = StringProperty()
    second_player = StringProperty()
    attempt = NumericProperty(1)
    players_attempts = list()

    lbl = None
    attempts_labels = list()

    attempt_dict = {
        1: 'Первая',
        2: 'Вторая',
        3: 'Третья',
        4: 'Четвертая',
        5: 'Пятая',
    }

    def list_refresher(self):
        self.ids.attempts_list.add_widget(MDLabel(
            text=f'{self.first_player}  {self.second_player}',
            halign='center',
            font_style='Button',
            size_hint_y=None,
            height=dp(30),
        ))

    def anim_next_player(self):
        anim = Animation(opacity=0)
        anim.start(self.ids.game_card)
        anim.bind(on_complete=self.next_player)

    def next_player(self, *args):
        if int(self.players_attempts[-1]) == self.number:
            self.ids.result_lbl.opacity = 1
        self.ids.num_inp.text = ''
        if len(self.players_attempts) % 2 == 1:
            Animation(opacity=1).start(self.ids.game_card)
            self.ids.info_lbl.text = f'ИГРОК {self.second_player.upper()} УГАДЫВАЕТ ЧИСЛО.'
            self.attempts_labels.append(MDLabel(
                text=f'{self.players_attempts[-1]}       ',
                halign='center',
                font_style='Button',
                size_hint_y=None,
                height=dp(30),
            ))
            self.ids.attempts_list.add_widget(self.attempts_labels[-1])

        else:
            self.ids.info_lbl.text = f'ИГРОК {self.first_player.upper()} УГАДЫВАЕТ ЧИСЛО.'
            if self.attempt < 5:
                self.attempt += 1
                self.attempts_labels[-1].text=f'{self.players_attempts[-2]}  {self.players_attempts[-1]}'
                self.ids.attempt_lbl.text = f'{self.attempt_dict[self.attempt].upper()} ПОПЫТКА'
                self.animator()
            else:
                print('Иди нахуй')

    def check_enter(self):
        if self.ids.num_inp.text.isdigit():
            num = int(self.ids.num_inp.text)
            if num in range(0, 100):
                self.ids.try_btn.disabled = False
            else:
                self.ids.try_btn.disabled = True
        if self.ids.num_inp.text == '':
            self.ids.try_btn.disabled = True

    def on_enter(self, *args):
        app = MDApp.get_running_app()
        self.number = randrange(0, 100)
        self.ids.result_lbl.text = str(self.number)
        self.first_player = app.screens[0].first_name
        self.second_player = app.screens[0].second_name
        self.animator()
        self.list_refresher()

    def animator(self):
        anim = Animation(opacity=1)
        anim.bind(on_complete=self.finish_enter_anim)
        anim.start(self.ids.game_lay)

    def finish_enter_anim(self, *args):
        app = MDApp.get_running_app()
        self.lbl = MDLabel(
            text=f'{self.attempt_dict[self.attempt].upper()} ПОПЫТКА',
            halign='center',
            font_style='H5',
            opacity=0,
            size_hint=(None, None),
            size=(dp(150), dp(100)),
            pos_hint={'right': 0, 'center_y': .5},
            theme_text_color='Custom',
            text_color=app.theme_cls.accent_color,
        )
        self.add_widget(self.lbl)
        anim = Animation(opacity=1, d=1.5)
        anim &= Animation(pos_hint={'right': .1}, d=3)
        anim.bind(on_complete=self.schedule_clear)
        anim.start(self.lbl)

    def schedule_clear(self, *args):
        Clock.schedule_once(self.remove_after, 2)

    def remove_after(self, dt):
        self.remove_widget(self.lbl)
        self.ids.info_lbl.text = f'ИГРОК {self.first_player.upper()} УГАДЫВАЕТ ЧИСЛО.'
        Animation(opacity=1).start(self.ids.game_card)