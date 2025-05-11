from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from widgets.sidebar import Sidebar

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()

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

    def add_new_task(self, instance):
        # TODO: Implement new task creation
        pass

    def load_tasks(self):
        # TODO: Load tasks from database
        pass 