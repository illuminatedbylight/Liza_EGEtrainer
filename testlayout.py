from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

from random_questions import random_questions

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_question = 1
        self.total_questions = 6
        self.questions = [quest for quest in random_questions()]
        self.create_screen()

    def create_screen(self):
        main_layout = FloatLayout()

        self.upper = Label(
            text=f'Задание №{self.current_question} ({self.current_question}/{self.total_questions})',
            font_size='20sp',
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            pos_hint={'top': 1},
            halign='center'
        )

        self.middle = BoxLayout(
            orientation='vertical',
            size_hint=(0.9, 0.7),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            spacing=20,
            padding=[0, 20, 0, 0]
        )

        navigation = BoxLayout(
            size_hint=(0.9, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            spacing=20
        )

        button_back = Button(
            text='Назад',
            font_size='18sp',
            bold=True,
            background_color=(0.85, 0.92, 0.78, 1),
            color=(0.35, 0.45, 0.3, 1),
            background_normal=''
        )
        button_back.bind(on_press=self.go_back)


        button_next = Button(
            text='Далее',
            font_size='18sp',
            bold=True,
            background_color=(0.95, 0.75, 0.8, 1),
            color=(0.35, 0.45, 0.3, 1),
            background_normal=''
        )
        button_next.bind(on_press=self.go_next)

        navigation.add_widget(button_back)
        navigation.add_widget(button_next)

        main_layout.add_widget(self.upper)
        main_layout.add_widget(self.middle)
        main_layout.add_widget(navigation)

        self.add_widget(main_layout)

        self.show_question()


    def show_question(self):
        self.middle.clear_widgets()
        self.upper.text = f'Задание №{self.current_question} ({self.current_question}/{self.total_questions})'

        if self.questions[self.current_question - 1][2] == "multi":
            self.show_checkbox_question()
        elif self.questions[self.current_question - 1][2] == "numbers":
            self.show_digits_question()
        elif self.questions[self.current_question - 1][2] == "word":
            self.show_word_question()

    #выбор нескольких ответов
    def show_checkbox_question(self):
        helping = Label(
            text='Вопрос с выбором нескольких ответов\n(отметь нужные варианты)',
            font_size='10sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )
        self.middle.add_widget(helping)

        question = Label(
            text=self.questions[self.current_question - 1][1],
            font_size='18sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )

        self.middle.add_widget(question)

        answers_box = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.7),
            spacing=10
        )

        for i in range(5):
            checkbox = ToggleButton(
                text=f'Вариант ответа {i + 1}',
                group=None,
                size_hint=(0.9, None),
                height=50,
                pos_hint={'center_x': 0.5},
                background_color=(1, 1, 1, 1),
                color=(0.4, 0.4, 0.4, 1),
                background_normal=''
            )
            answers_box.add_widget(checkbox)

        self.middle.add_widget(answers_box)

    def show_digits_question(self):
        question_label = Label(
            text='Вопрос с вводом цифр\n(введите цифры \nв порядке возрастания\nбез пробелов)',
            font_size='18sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )
        self.middle.add_widget(question_label)

        question = Label(
            text=self.questions[self.current_question - 1][1],
            font_size='18sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )

        self.middle.add_widget(question)

        self.middle.add_widget(Label(size_hint=(1, 0.2)))

        digits_input = TextInput(
            hint_text='Например: 123',
            multiline=False,
            size_hint=(0.8, 0.15),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            foreground_color=(0.4, 0.4, 0.4, 1),
            background_color=(1, 1, 1, 1),
            padding=[10, 10]
        )
        self.middle.add_widget(digits_input)

    def show_word_question(self):
        question_label = Label(
            text='Вопрос с вводом слова\n(введите слово)',
            font_size='18sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )
        self.middle.add_widget(question_label)

        question = Label(
            text=self.questions[self.current_question - 1][1],
            font_size='18sp',
            color=(0.88, 0.38, 0.47, 1),
            size_hint=(1, 0.3),
            halign='center',
            valign='top'
        )

        self.middle.add_widget(question)

        self.middle.add_widget(Label(size_hint=(1, 0.2)))

        word_input = TextInput(
            hint_text='Введите слово',
            multiline=False,
            size_hint=(0.8, 0.15),
            pos_hint={'center_x': 0.5},
            font_size='16sp',
            foreground_color=(0.4, 0.4, 0.4, 1),
            background_color=(1, 1, 1, 1),
            padding=[10, 10]
        )
        self.middle.add_widget(word_input)

    def go_next(self, instance):

        if self.current_question < self.total_questions:
            self.current_question += 1
            self.show_question()
        else:
            print("Тест завершён! Переходим к результатам...")
            self.manager.current = 'results'

    def go_back(self, instance):

        if self.current_question > 1:
            self.current_question -= 1
            self.show_question()
