import sys
import os
# Projenin kök dizinini Python path'ine ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from utils.colors import get_color, COLORS
from screens.main_screen import MainScreen
from screens.team_screen import TeamScreen
from screens.profile_screen import ProfileScreen
from screens.task_detail_screen import TaskDetailScreen

class TaskManagerApp(App):
    def build(self):
        # Pencere boyutu ve arka plan rengi
        Window.size = (400, 700)
        Window.clearcolor = get_color('background')
        
        # Ekran yöneticisi - FadeTransition ile yumuşak geçiş
        sm = ScreenManager(transition=FadeTransition(duration=0.2))
        
        # Ekranları ekle
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(TeamScreen(name='team'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(TaskDetailScreen(name='task_detail'))
        
        return sm

if __name__ == '__main__':
    TaskManagerApp().run()
