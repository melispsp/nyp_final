from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from utils.colors import get_color, COLORS

class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = 0.3
        self.padding = 10
        self.spacing = 5
        
        # Arka plan rengi
        with self.canvas.before:
            Color(*get_color('surface'))
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_rect, size=self._update_rect)
        self.setup_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def setup_ui(self):
        # Başlık
        header = Button(
            text='Takımlar',
            size_hint_y=None,
            height=50,
            background_color=get_color('primary'),
            color=get_color('text'),
            bold=True,
            background_normal=''
        )
        self.add_widget(header)
        
        # Takım listesi
        scroll = ScrollView(
            bar_width=10,
            bar_color=get_color('primary'),
            bar_inactive_color=get_color('secondary'),
            effect_cls='ScrollEffect'
        )
        self.team_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.team_list.bind(minimum_height=self.team_list.setter('height'))
        
        # Örnek takımları ekle
        teams = [
            {'name': 'A Takımı', 'id': 1},
            {'name': 'B Takımı', 'id': 2}
        ]
        
        for team in teams:
            btn = Button(
                text=team['name'],
                size_hint_y=None,
                height=40,
                background_color=get_color('secondary'),
                color=get_color('text'),
                background_normal='',
                bold=True
            )
            btn.bind(on_press=lambda x, t=team: self.on_team_click(t))
            self.team_list.add_widget(btn)
        
        scroll.add_widget(self.team_list)
        self.add_widget(scroll)

    def on_team_click(self, team):
        # Takım detay sayfasına git
        app = self.get_root_window().children[0].children[0]
        team_screen = app.manager.get_screen('team')
        team_screen.current_team = team['name']  # Takım adını sakla
        app.manager.current = 'team' 