import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="task_manager.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                photo_path TEXT
            )
        ''')

        # Create teams table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')

        # Create team_members table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS team_members (
                team_id INTEGER,
                user_id INTEGER,
                role TEXT,
                FOREIGN KEY (team_id) REFERENCES teams (id),
                FOREIGN KEY (user_id) REFERENCES users (id),
                PRIMARY KEY (team_id, user_id)
            )
        ''')

        # Create tasks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                short_description TEXT,
                full_description TEXT,
                due_date TEXT,
                status TEXT,
                team_id INTEGER,
                assigned_to INTEGER,
                created_by INTEGER,
                created_at TEXT,
                FOREIGN KEY (team_id) REFERENCES teams (id),
                FOREIGN KEY (assigned_to) REFERENCES users (id),
                FOREIGN KEY (created_by) REFERENCES users (id)
            )
        ''')

        conn.commit()
        conn.close()

    def get_connection(self):
        return sqlite3.connect(self.db_name)