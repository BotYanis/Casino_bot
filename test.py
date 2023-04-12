import sqlite3

conn = sqlite3.connect('bebra.db', check_same_thread=False)
cursor = conn.cursor()

for i in cursor.execute('SELECT user_id FROM users').fetchall():

    demo_list = [i[0], 0, 0, 0]
    print(i[0])
    cursor.execute("INSERT INTO demo VALUES (?, ?, ?, ?) ;", demo_list)
    conn.commit()