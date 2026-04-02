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
        Window.clearcolor = (1, 0.94, 0.8, 1)

        sm = ScreenManager()

        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='variant'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(ResultsScreen(name='results'))

        return sm


if __name__ == '__main__':
    EGEApp().run()
