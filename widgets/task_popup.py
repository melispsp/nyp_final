from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from utils.colors import get_color, COLORS

class TaskPopup(Popup):
    def __init__(self, teams, on_save_callback, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Yeni Görev Ekle'
        self.size_hint = (0.9, 0.7)
        self.background = ''
        self.background_color = get_color('surface')
        self.title_color = get_color('text')
        self.title_size = '20sp'
        self.title_align = 'center'
        self.teams = teams
        self.on_save_callback = on_save_callback  # Kaydetme işlemi için callback
        self.setup_ui()

    def setup_ui(self):
        # Ana layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Form alanları
        form = GridLayout(cols=1, spacing=10, size_hint_y=None, height=300)
        
        # Takım seçimi
        team_label = Label(
            text='Takım:',
            size_hint_y=None,
            height=30,
            color=get_color('text'),
            halign='left'
        )
        form.add_widget(team_label)
        
        self.team_spinner = Spinner(
            text='Takım Seçin',
            values=[team['name'] for team in self.teams],
            size_hint_y=None,
            height=40,
            background_color=get_color('secondary'),
            color=get_color('text'),
            background_normal=''
        )
        form.add_widget(self.team_spinner)
        
        # Görev adı
        title_label = Label(
            text='Görev Adı:',
            size_hint_y=None,
            height=30,
            color=get_color('text'),
            halign='left'
        )
        form.add_widget(title_label)
        
        self.title_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            background_color=get_color('secondary'),
            foreground_color=get_color('text'),
            cursor_color=get_color('text'),
            padding=[10, 10, 10, 10]
        )
        form.add_widget(self.title_input)
        
        # Görev açıklaması
        desc_label = Label(
            text='Görev Açıklaması:',
            size_hint_y=None,
            height=30,
            color=get_color('text'),
            halign='left'
        )
        form.add_widget(desc_label)
        
        self.desc_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=100,
            background_color=get_color('secondary'),
            foreground_color=get_color('text'),
            cursor_color=get_color('text'),
            padding=[10, 10, 10, 10]
        )
        form.add_widget(self.desc_input)
        
        # Görev süresi
        duration_label = Label(
            text='Görev Süresi:',
            size_hint_y=None,
            height=30,
            color=get_color('text'),
            halign='left'
        )
        form.add_widget(duration_label)
        
        self.duration_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            background_color=get_color('secondary'),
            foreground_color=get_color('text'),
            cursor_color=get_color('text'),
            padding=[10, 10, 10, 10],
            hint_text='Örn: 2 hafta, 5 gün'
        )
        form.add_widget(self.duration_input)
        
        layout.add_widget(form)
        
        # Butonlar
        buttons = BoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint_y=None,
            height=50
        )
        
        cancel_btn = Button(
            text='İptal',
            background_color=get_color('error'),
            color=get_color('text'),
            background_normal=''
        )
        cancel_btn.bind(on_press=self.dismiss)
        
        save_btn = Button(
            text='Kaydet',
            background_color=get_color('success'),
            color=get_color('text'),
            background_normal=''
        )
        save_btn.bind(on_press=self.save_task)
        
        buttons.add_widget(cancel_btn)
        buttons.add_widget(save_btn)
        layout.add_widget(buttons)
        
        self.content = layout

    def save_task(self, instance):
        # Görev verilerini al
        task_data = {
            'team': self.team_spinner.text,
            'title': self.title_input.text,
            'description': self.desc_input.text,
            'duration': self.duration_input.text,
            'status': 'Planlandı'  # Varsayılan durum
        }
        
        # Callback fonksiyonunu çağır
        if self.on_save_callback:
            self.on_save_callback(task_data)
        
        # Popup'ı kapat
        self.dismiss() 