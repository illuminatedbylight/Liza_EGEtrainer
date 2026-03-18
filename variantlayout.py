from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_simple_layout()

    def create_simple_layout(self):
        layout = FloatLayout()

        title = Label(
            text='Давай создадим\nтренировочный вариант\nтестовой части!',
            font_size='28sp',
            bold=True,
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'top': 0.80},
            halign='center'
        )

        arrow = Label(
            text='↓',
            font_size='35sp',
            color=(0.88, 0.38, 0.47, 0.7),
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            font_name='Arial',
        )


        self.button = Button(
            text='подобрать вариант!',
            font_size='22sp',
            bold=True,
            size_hint=(0.7, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.40},
            background_color=(0.7, 0.82, 0.62, 1),
            color=(0.35, 0.45, 0.3, 1),
            background_normal=''
        )

        self.button.bind(on_press=self.generate_variant)


        hint = Label(
            text='10 случайных заданий\nиз базы ЕГЭ',
            font_size='16sp',
            color=(0.88, 0.38, 0.47, 0.8),
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            halign='center'
        )


        layout.add_widget(title)
        layout.add_widget(arrow)
        layout.add_widget(self.button)
        layout.add_widget(hint)


        self.add_widget(layout)

    def generate_variant(self, instance):
        print("Генерируем вариант...")
        self.manager.current = 'test'


