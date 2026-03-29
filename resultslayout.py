import json, sqlite3
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = FloatLayout()

        self.upper = Label(
            text=f'Жми кнопку',
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

        self.navigation = BoxLayout(
            size_hint=(0.9, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            spacing=20
        )

        button_next = Button(
            text='Показать результаты',
            font_size='18sp',
            bold=True,
            background_color=(0.95, 0.75, 0.8, 1),
            color=(0.35, 0.45, 0.3, 1),
            background_normal=''
        )
        button_next.bind(on_press=self.show_results)

        self.navigation.add_widget(button_next)

        main_layout.add_widget(self.upper)
        main_layout.add_widget(self.middle)
        main_layout.add_widget(self.navigation)

        self.add_widget(main_layout)

    def show_results(self, instance):

        count_right_ans = 0
        errors_ans = []

        with open('answers.json', 'r', encoding='utf-8') as f:
            answers = json.load(f)

        for ans in answers:

            with sqlite3.connect('questions.db') as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                    select answer
                    from answers
                    where question_id = {list(answers[ans].keys())[0]}
                    and correcting = 1
                ''')
                list_right_answers = [i[0] for i in cursor.fetchall()]

            if len(list_right_answers) == 1:
                if answers[ans][list(answers[ans].keys())[0]] == list_right_answers[0]:
                    count_right_ans += 1
                else:
                    errors_ans.append([ans, answers[ans][list(answers[ans].keys())[0]], list_right_answers[0]])
            else:

                count_right_multi_ans = 0
                for multi_ans in answers[ans][list(answers[ans].keys())[0]]:
                    if multi_ans in list_right_answers:
                        count_right_multi_ans += 1
                if count_right_multi_ans == len(list_right_answers):
                    count_right_ans += 1
                else:
                    errors_ans.append([ans,
                                       ', '.join(answers[ans][list(answers[ans].keys())[0]]),
                                       ', '.join(list_right_answers)]
                                      )

        self.upper.text = f'{count_right_ans} / 6'
        for err in errors_ans:
            res = Label(
                text=f'Номер: {err[0]} / Ваш ответ: {err[1]} / Верный ответ: {err[2]}',
                font_size='18sp',
                color=(0.88, 0.38, 0.47, 1),
                size_hint=(1, 0.3),
                halign='center',
                valign='top'
            )
            self.middle.add_widget(res)
        self.navigation.clear_widgets()
