from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex

class TaskItem(BoxLayout):
    def __init__(self, task_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = 120
        self.padding = 10
        self.spacing = 5
        self.task_data = task_data
        
        # Arka plan rengi
        with self.canvas.before:
            Color(0.18, 0.18, 0.18, 1)  # Koyu gri
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_rect, size=self._update_rect)
        self.setup_ui()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def setup_ui(self):
        # Görev başlığı
        title = Label(
            text=self.task_data['title'],
            size_hint_y=None,
            height=30,
            font_size='16sp',
            bold=True,
            color=(1, 1, 1, 1)  # Beyaz
        )
        self.add_widget(title)
        
        # Görev süresi
        duration = Label(
            text=f"Süre: {self.task_data['duration']}",
            size_hint_y=None,
            height=25,
            font_size='14sp',
            color=(0.75, 0.75, 0.75, 1)  # Açık gri
        )
        self.add_widget(duration)
        
        # Takım bilgisi
        team = Label(
            text=f"Takım: {self.task_data['team']}",
            size_hint_y=None,
            height=25,
            font_size='14sp',
            color=(0.75, 0.75, 0.75, 1)  # Açık gri
        )
        self.add_widget(team)
        
        # Durum etiketi
        status = Label(
            text=f"Durum: {self.task_data['status']}",
            size_hint_y=None,
            height=25,
            font_size='14sp',
            color=(0, 0.72, 0.76, 1)  # Turkuaz
        )
        self.add_widget(status)