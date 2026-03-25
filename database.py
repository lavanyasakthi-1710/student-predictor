import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    
    # Check if empty
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        seed_data(conn)
    
    conn.close()
    print("Database initialized and connected.")

def seed_data(conn):
    print("Seeding sample data...")
    password_hash = generate_password_hash('password123')
    
    users = [
        ('Alice Johnson', 'alice@student.com', password_hash, 'student'),
        ('Bob Smith', 'bob@student.com', password_hash, 'student'),
        ('Charlie Brown', 'charlie@student.com', password_hash, 'student')
    ]
    cur = conn.cursor()
    cur.executemany("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", users)
    
    records = [
        (1, 'Fall 2023', 3.8, 95.0, 20.0),
        (2, 'Fall 2023', 2.5, 75.0, 10.0),
        (3, 'Fall 2023', 1.8, 60.0, 4.0)
    ]
    cur.executemany("INSERT INTO academic_records (student_id, semester, gpa, attendance_percentage, study_hours_per_week) VALUES (?, ?, ?, ?, ?)", records)
    
    subjects = [
        (1, 'Mathematics', 95, 100),
        (1, 'Physics', 88, 100),
        (1, 'Computer Science', 98, 100),
        (2, 'Mathematics', 55, 100),
        (2, 'Physics', 70, 100),
        (2, 'Computer Science', 75, 100),
        (3, 'Mathematics', 40, 100),
        (3, 'Physics', 45, 100),
        (3, 'Computer Science', 50, 100)
    ]
    cur.executemany("INSERT INTO subject_performance (record_id, subject_name, marks_obtained, max_marks) VALUES (?, ?, ?, ?)", subjects)
    
    conn.commit()
    print("Sample data seeded successfully.")

if __name__ == '__main__':
    init_db()
