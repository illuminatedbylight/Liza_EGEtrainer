import sqlite3


with sqlite3.connect('questions.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('''
    #     CREATE TABLE questions (
    #     id INTEGER PRIMARY KEY,
    #     question TEXT,
    #     type TEXT
    #     )
    # ''')
    # cursor.execute('''
    #     CREATE TABLE answers (
    #     question_id INTEGER REFERENCES questions(id),
    #     answer TEXT,
    #     correcting INT
    #     )
    # ''')
    # cursor.execute('''
    #     INSERT INTO questions
    #     VALUES (1, "Ты покакал?", "word")
    # ''')
    cursor.execute('''
        INSERT INTO answers
        VALUES (1, "Да", 1)
    ''')
