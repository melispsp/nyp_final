from kivy.uix.screenmanager import Screen # type: ignore
from kivy.uix.boxlayout import BoxLayout# type: ignore
from kivy.uix.gridlayout import GridLayout# type: ignore
from kivy.uix.scrollview import ScrollView# type: ignore
from kivy.uix.label import Label# type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.graphics import Color, Rectangle # type: ignore

class TeamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        self.load_team_data()  # Örnek takım verilerini yükle

    def setup_ui(self):
        # Ana layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Başlık ve geri butonu
        header = BoxLayout(size_hint_y=None, height=50)
        
        back_btn = Button(
            text='← Geri',
            size_hint_x=None,
            width=100,
            background_color=(0.3, 0.6, 0.9, 1)
        )
        back_btn.bind(on_press=self.go_back)
        header.add_widget(back_btn)
        
        self.team_title = Label(
            text='Takım Detayları',
            font_size=24,
            bold=True,
            size_hint_x=0.7
        )
        header.add_widget(self.team_title)
        
        layout.add_widget(header)
        
        # Takım bilgileri
        info_box = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
        info_box.padding = 10
        
        with info_box.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.info_rect = Rectangle(pos=info_box.pos, size=info_box.size)
        info_box.bind(pos=self._update_info_rect, size=self._update_info_rect)
        
        self.team_info = Label(
            text='',
            size_hint_y=None,
            height=100,
            halign='left',
            valign='top',
            text_size=(info_box.width, None)
        )
        info_box.add_widget(self.team_info)
        
        layout.add_widget(info_box)
        
        # Takım üyeleri başlığı
        members_header = Label(
            text='Takım Üyeleri',
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(members_header)
        
        # Takım üyeleri listesi
        scroll = ScrollView()
        self.members_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.members_list.bind(minimum_height=self.members_list.setter('height'))
        scroll.add_widget(self.members_list)
        layout.add_widget(scroll)
        
        # Aktif görevler başlığı
        tasks_header = Label(
            text='Aktif Görevler',
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(tasks_header)
        
        # Aktif görevler listesi
        tasks_scroll = ScrollView()
        self.tasks_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.tasks_list.bind(minimum_height=self.tasks_list.setter('height'))
        tasks_scroll.add_widget(self.tasks_list)
        layout.add_widget(tasks_scroll)
        
        self.add_widget(layout)

    def _update_info_rect(self, instance, value):
        self.info_rect.pos = instance.pos
        self.info_rect.size = instance.size

    def load_team_data(self):
        # Örnek takım verileri
        team_data = {
            'A Takımı': {
                'description': 'Web Geliştirme Ekibi\nOluşturulma: 01.01.2024\nProje: E-Ticaret Platformu',
                'members': [
                    {'name': 'Ahmet Yılmaz', 'role': 'Takım Lideri'},
                    {'name': 'Ayşe Demir', 'role': 'Frontend Geliştirici'},
                    {'name': 'Mehmet Kaya', 'role': 'Backend Geliştirici'},
                    {'name': 'Zeynep Şahin', 'role': 'UI/UX Tasarımcı'}
                ],
                'active_tasks': [
                    {'title': 'Web Sitesi Tasarımı', 'status': 'Devam Ediyor'},
                    {'title': 'Veritabanı Güncelleme', 'status': 'Tamamlandı'},
                    {'title': 'Kullanıcı Arayüzü İyileştirme', 'status': 'Planlandı'}
                ]
            },
            'B Takımı': {
                'description': 'Mobil Uygulama Ekibi\nOluşturulma: 15.01.2024\nProje: Mobil Uygulama Geliştirme',
                'members': [
                    {'name': 'Ali Öztürk', 'role': 'Takım Lideri'},
                    {'name': 'Fatma Yıldız', 'role': 'Mobil Geliştirici'},
                    {'name': 'Can Korkmaz', 'role': 'Test Mühendisi'},
                    {'name': 'Elif Aydın', 'role': 'UI Tasarımcı'}
                ],
                'active_tasks': [
                    {'title': 'Mobil Uygulama Testi', 'status': 'Beklemede'},
                    {'title': 'API Entegrasyonu', 'status': 'Devam Ediyor'}
                ]
            }
        }
        
        self.team_data = team_data

    def on_enter(self):
        # Takım adını al ve verileri göster
        current_team = getattr(self, 'current_team', 'A Takımı')
        self.team_title.text = current_team
        self.show_team_details(current_team)

    def show_team_details(self, team_name):
        if team_name in self.team_data:
            team = self.team_data[team_name]
            
            # Takım bilgilerini göster
            self.team_info.text = team['description']
            
            # Takım üyelerini göster
            self.members_list.clear_widgets()
            for member in team['members']:
                member_box = BoxLayout(size_hint_y=None, height=50)
                with member_box.canvas.before:
                    Color(0.95, 0.95, 0.95, 1)
                    Rectangle(pos=member_box.pos, size=member_box.size)
                
                name_label = Label(
                    text=member['name'],
                    size_hint_x=0.7,
                    halign='left',
                    valign='middle'
                )
                role_label = Label(
                    text=member['role'],
                    size_hint_x=0.3,
                    halign='right',
                    valign='middle'
                )
                
                member_box.add_widget(name_label)
                member_box.add_widget(role_label)
                self.members_list.add_widget(member_box)
            
            # Aktif görevleri göster
            self.tasks_list.clear_widgets()
            for task in team['active_tasks']:
                task_box = BoxLayout(size_hint_y=None, height=40)
                with task_box.canvas.before:
                    Color(0.95, 0.95, 0.95, 1)
                    Rectangle(pos=task_box.pos, size=task_box.size)
                
                title_label = Label(
                    text=task['title'],
                    size_hint_x=0.7,
                    halign='left',
                    valign='middle'
                )
                status_label = Label(
                    text=task['status'],
                    size_hint_x=0.3,
                    halign='right',
                    valign='middle'
                )
                
                task_box.add_widget(title_label)
                task_box.add_widget(status_label)
                self.tasks_list.add_widget(task_box)

    def go_back(self, instance):
        self.manager.current = 'main' 