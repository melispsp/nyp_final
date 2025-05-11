from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from screens.main_screen import MainScreen
from screens.team_screen import TeamScreen
from screens.profile_screen import ProfileScreen
from screens.task_detail_screen import TaskDetailScreen

class TaskManagerApp(App):
    def build(self):
        # Test için pencere boyutunu ayarla
        Window.size = (400, 700)
        
        # Ekran yöneticisini oluştur
        sm = ScreenManager()
        
        # Ekranları ekle
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(TeamScreen(name='team'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(TaskDetailScreen(name='task_detail'))
        
        return sm

if __name__ == '__main__':
    TaskManagerApp().run()
