from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Результаты теста', font_size=30))