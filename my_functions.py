import sqlite3

def create_DB():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo (todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       status INTEGER NOT NULL)''')
    
    # reset the auto-increment counter after clearing all records
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='todo'")
    conn.commit()
    conn.close()

def viewDB():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo')
    rows= cursor.fetchall()
    return rows

def insertDB(title):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todo (title, status) VALUES(?, ?)", (title, 0))
    conn.commit()
    conn.close()

def updateTask(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE todo SET status =1 WHERE todo_id=? ", (id,))
    conn.commit()
    conn.close()

def deleteTask(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo WHERE todo_id=?", (id,))
    cursor.execute("SELECT todo_id FROM todo")
    rows = cursor.fetchall()
    for i, row in enumerate(rows, start=1):
        cursor.execute("UPDATE todo SET todo_id=? WHERE todo_id=?", (i, row[0]))
    
    conn.commit()
    conn.close()


def clear():
    conn = sqlite3.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE todo SET todo_id = NULL")
    conn.commit()
    conn.close()


def clear_all():
    conn = sqlite3.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE from todo")
    conn.commit()

    #re-assign IDs starting from 1
    cursor.execute("SELECT todo_id FROM todo")
    clear()
    conn.commit()
    conn.close()