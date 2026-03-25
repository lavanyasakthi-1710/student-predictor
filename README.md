# AI-Based Student Performance Predictor & Mentor System

A comprehensive web application designed to help students track their academic progress, receive performance predictions, and get personalized study recommendations using heuristic models.

## Features
- **Student Dashboard**: View GPA, attendance, and subject marks.
- **Performance Prediction Engine**: Mentorship classification into "Good", "Average", and "At Risk".
- **Progress Tracking**: Visual GPA trends using Chart.js.
- **Study Suggestions**: Actionable study advice targeted at weak subjects.
- **AI Chatbot**: Rule-based virtual mentor answering common study questions.
- **Authentication System**: Secure JWT-based login and registration.

## Tech Stack
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 (Glassmorphism & Dark Mode UI), Chart.js
- **Backend**: Python, Flask, Flask-CORS, PyJWT, Werkzeug (Password hashing)
- **Database**: SQLite3

## Installation & Setup

1. **Navigate to the Project Directory**
   ```bash
   cd student_predictor
   ```
   
2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   # Activate on Windows:
   .\venv\Scripts\activate
   # Activate on Mac/Linux:
   source venv/bin/activate
   ```
   
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Start the Application**
   ```bash
   python app.py
   ```
   *Note: Starting `app.py` automatically initializes the database schema and seeds sample student data if the database is empty.*

5. **Access the Application**
   Open your browser and navigate to: `http://localhost:3000`

## Default Seeded Accounts
You can log in immediately testing the following sample accounts:
- **Alice Johnson** (Good Performance) -> `alice@student.com` | Password: `password123`
- **Bob Smith** (Average Performance) -> `bob@student.com` | Password: `password123`
- **Charlie Brown** (At Risk Performance) -> `charlie@student.com` | Password: `password123`
