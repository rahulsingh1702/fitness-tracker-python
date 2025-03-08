import sqlite3

conn = sqlite3.connect('database/fitness_tracker.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS fitness_data (
                user_id INTEGER,
                steps INTEGER,
                calories INTEGER,
                water_intake REAL,
                workouts INTEGER,
                date TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT)''')

conn.commit()
conn.close()
print("✅ Database setup complete! fitness_tracker.db created.")