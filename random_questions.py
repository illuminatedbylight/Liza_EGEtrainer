import sqlite3
from random import randint


def random_questions():
    questions = list()
    types = {
        "word": 0,
        "numbers": 0,
        "multi": 0
    }

    with sqlite3.connect('questions.db') as conn:
        cursor = conn.cursor()
        cursor.execute('select id from questions order by 1 desc limit 1')
        max_id = cursor.fetchone()[0]

        while len(questions) != 6:
            rand_num = randint(1, max_id)
            cursor.execute(f'select * from questions where id = {rand_num}')
            data = cursor.fetchone()

            flag_add_quest = True
            for quest in questions:
                if data[0] in quest:
                    flag_add_quest = False

            if flag_add_quest and types[data[2]] < 2:
                questions.append([data[0], data[1], data[2]])
                types[data[2]] += 1

    return questions
