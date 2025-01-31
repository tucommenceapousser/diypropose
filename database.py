import sqlite3

def init_db():
    conn = sqlite3.connect("data/diy.db")
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS tutoriels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT UNIQUE,
        description TEXT,
        materiel TEXT,
        etapes TEXT,
        conseils TEXT,
        video_url TEXT,
        pdf_url TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS favoris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT UNIQUE
    )
    ''')

    conn.commit()
    conn.close()

init_db()
