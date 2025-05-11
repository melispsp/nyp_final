from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class TaskDetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()

    def setup_ui(self):
        # Ana layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Geri butonu
        back_btn = Button(
            text='← Geri',
            size_hint_y=None,
            height=50,
            background_color=(0.3, 0.6, 0.9, 1)
        )
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        # Görev başlığı
        self.task_title = Label(
            text='Görev Detayları',
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.task_title)
        
        # Görev detayları
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Örnek görev detayları
        task_details = [
            ('Durum', 'Devam Ediyor'),
            ('Takım', 'A Takımı'),
            ('Atanan Kişi', 'Ahmet Yılmaz'),
            ('Başlangıç Tarihi', '01.01.2024'),
            ('Bitiş Tarihi', '15.01.2024'),
            ('Açıklama', 'Bu görev web sitesinin tasarımını içermektedir. '
                        'Kullanıcı arayüzü ve kullanıcı deneyimi iyileştirmeleri yapılacaktır.')
        ]
        
        for label, value in task_details:
            detail_box = BoxLayout(orientation='vertical', size_hint_y=None, height=60)
            detail_box.add_widget(Label(
                text=label,
                size_hint_y=None,
                height=30,
                bold=True
            ))
            detail_box.add_widget(Label(
                text=value,
                size_hint_y=None,
                height=30
            ))
            content.add_widget(detail_box)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        # Alt butonlar
        buttons_box = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        edit_btn = Button(
            text='Düzenle',
            background_color=(0.2, 0.8, 0.2, 1)
        )
        buttons_box.add_widget(edit_btn)
        
        delete_btn = Button(
            text='Sil',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        buttons_box.add_widget(delete_btn)
        
        layout.add_widget(buttons_box)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def load_task(self, task_data):
        # Görev verilerini yükle
        self.task_title.text = task_data.get('title', 'Görev Detayları')
        # TODO: Diğer görev detaylarını yükle 