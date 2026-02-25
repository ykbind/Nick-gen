# Coder Nickname Generator

A full-stack Flask application that analyzes your coding habits, intelligence, and skills to generate a unique digital identity, avatar, and nickname.

## Features

- **Coding Habit Analyzer**: Evaluates your efficiency based on hours, frequency, and preference.
- **Intelligence Quiz**: A 10-question MCQ logic and programming quiz to classify your level (Beginner/Intermediate/Pro).
- **Programming Skill Badges**: Converts your self-evaluated skill levels into professional badges.
- **Dynamic Avatar Generator**: Generates SVG avatars offline based on your profile analysis.
- **Rule-Based Nickname Engine**: Creates custom nicknames using a centralized logic pipeline.
- **Team Mode**: Analyze consolidated team skills and generate squad names.
- **Interview Readiness**: Evaluates your technical confidence and provides improvement plans.

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2
- **Logic**: Modular Service-oriented Architecture

## Project Structure

```text
coder_nickname_app/
├── app.py                  # Entry point & Routes
├── config.py               # App configuration
├── requirements.txt        # Dependencies
├── models/                 # Database Models
│   ├── user.py
│   ├── skill.py
│   └── team.py
├── services/               # Business Logic
│   ├── data_aggregator.py
│   ├── analyzer_engine.py
│   ├── nickname_engine.py
│   ├── avatar_generator.py
│   ├── team_engine.py
│   └── interview_analyzer.py
├── templates/              # Jinja2 Templates
└── static/                 # Static Assets (CSS, JS, Avatars)
```

## Setup Instructions

### 1. Prerequisite
Ensure you have Python 3.9+ installed.

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000/`.

## Usage
1. Enter your name and coding habits on the home page.
2. Complete the 10-question intelligence quiz.
3. View your generated Nickname and custom SVG Avatar.
4. Explore 'Team Mode' to see consolidated stats.
5. Use 'Interview Prep' for personalized career feedback.
