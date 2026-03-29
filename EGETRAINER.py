import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from openinglayout import FirstScreen
from variantlayout import SecondScreen
from testlayout import TestScreen
from resultslayout import ResultsScreen


class EGEApp(App):
    def build(self):

        Window.size = (360, 640)
        Window.clearcolor = (1.0, 0.93, 0.75, 1)

        sm = ScreenManager()

        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='variant'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(ResultsScreen(name='results'))

        with open('answers.json', 'w', encoding='utf-8') as f:
            json.dump({'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}}, f, ensure_ascii=False, indent=4)

        return sm


if __name__ == '__main__':
    EGEApp().run()
