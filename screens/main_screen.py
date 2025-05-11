import os
import sys
# Projenin kök dizinini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from widgets.sidebar import Sidebar
from widgets.task_item import TaskItem
from widgets.task_popup import TaskPopup
from utils.colors import get_color, COLORS

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tasks = []  # Görevleri tutacak liste
        self.setup_ui()
        self.load_sample_tasks()  # Örnek görevleri yükle

    def setup_ui(self):
        # Main layout
        layout = BoxLayout(orientation='horizontal')
        
        # Add sidebar
        self.sidebar = Sidebar()
        layout.add_widget(self.sidebar)
        
        # Main content area
        content = BoxLayout(orientation='vertical')
        
        # Header
        header = BoxLayout(size_hint_y=None, height=50)
        header.add_widget(Label(text='Tasks', font_size=20))
        profile_btn = Button(text='Profile', size_hint_x=None, width=100)
        profile_btn.bind(on_press=self.go_to_profile)
        header.add_widget(profile_btn)
        content.add_widget(header)
        
        # Task list
        scroll = ScrollView()
        self.task_list = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        scroll.add_widget(self.task_list)
        content.add_widget(scroll)
        
        # Add new task button
        add_btn = Button(text='Add New Task', size_hint_y=None, height=50)
        add_btn.bind(on_press=self.add_new_task)
        content.add_widget(add_btn)
        
        layout.add_widget(content)
        self.add_widget(layout)

    def go_to_profile(self, instance):
        self.manager.current = 'profile'

    def load_sample_tasks(self):
        # Örnek görevler
        self.tasks = [
            {
                'title': 'Web Sitesi Tasarımı',
                'duration': '2 hafta',
                'team': 'A Takımı',
                'status': 'Devam Ediyor',
                'description': 'Web sitesinin tasarımı ve kullanıcı arayüzü iyileştirmeleri'
            },
            {
                'title': 'Veritabanı Güncelleme',
                'duration': '3 gün',
                'team': 'A Takımı',
                'status': 'Tamamlandı',
                'description': 'Veritabanı şemasının güncellenmesi ve optimizasyonu'
            },
            {
                'title': 'Mobil Uygulama Testi',
                'duration': '1 hafta',
                'team': 'B Takımı',
                'status': 'Beklemede',
                'description': 'Mobil uygulamanın kapsamlı testi ve hata raporlaması'
            }
        ]
        self.update_task_list()

    def update_task_list(self):
        # Görev listesini temizle
        self.task_list.clear_widgets()
        
        # Görevleri listele
        for task in self.tasks:
            task_item = TaskItem(task_data=task)
            self.task_list.add_widget(task_item)

    def add_new_task(self, instance):
        # Örnek takım listesi
        teams = [
            {'name': 'A Takımı', 'id': 1},
            {'name': 'B Takımı', 'id': 2}
        ]
        
        # Görev ekleme popup'ını göster
        popup = TaskPopup(
            teams=teams,
            on_save_callback=self.save_new_task
        )
        popup.open()

    def save_new_task(self, task_data):
        # Yeni görevi listeye ekle
        self.tasks.append(task_data)
        # Görev listesini güncelle
        self.update_task_list() 