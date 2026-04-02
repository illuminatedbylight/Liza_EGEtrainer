from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(Label(size_hint=(1, 0.10)))

        center_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.15),
            spacing=5
        )


        lines = [
            'Я – твой',
            'карманный',
            'тренер для',
            'ЕГЭ',
            'ПО РУССКОМУ',
            'ЯЗЫКУ'
        ]


        for line in lines:
            label = Label(
                text=line,
                font_size='30sp',
                bold=True,
                color=(0.88, 0.38, 0.47, 1),
                font_name='Roboto',
                halign='center',
                valign='middle'
            )
            center_layout.add_widget(label)

        main_layout.add_widget(center_layout)


        bottom_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.15),
            padding=[0, 0, 0, 20]
        )


        hint = Label(
            text='Нажми для продолжения',
            font_size='20sp',
            color=(0.88, 0.38, 0.47, 0.8),
            halign='center',
            valign='bottom'
        )

        bottom_layout.add_widget(hint)
        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)

    def on_touch_down(self, touch):
        self.manager.current = 'variant'
        return True