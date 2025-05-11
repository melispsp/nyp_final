from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class ProfileScreen(Screen):
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
        
        # Profil başlığı
        layout.add_widget(Label(
            text='Profil',
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=50
        ))
        
        # Profil fotoğrafı (örnek)
        profile_image = Image(
            source='default_profile.png',  # Varsayılan bir resim ekleyin
            size_hint=(None, None),
            size=(150, 150),
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(profile_image)
        
        # Kullanıcı bilgileri
        info_box = BoxLayout(orientation='vertical', spacing=10)
        
        # Örnek kullanıcı bilgileri
        user_info = [
            ('Ad Soyad', 'Ahmet Yılmaz'),
            ('E-posta', 'ahmet@example.com'),
            ('Takım', 'A Takımı'),
            ('Rol', 'Takım Lideri')
        ]
        
        for label, value in user_info:
            info_box.add_widget(Label(
                text=f'{label}: {value}',
                size_hint_y=None,
                height=40,
                halign='left'
            ))
        
        layout.add_widget(info_box)
        
        # Butonlar
        buttons_box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=120)
        
        change_pass_btn = Button(
            text='Şifre Değiştir',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        buttons_box.add_widget(change_pass_btn)
        
        logout_btn = Button(
            text='Çıkış Yap',
            size_hint_y=None,
            height=50,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        buttons_box.add_widget(logout_btn)
        
        layout.add_widget(buttons_box)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'