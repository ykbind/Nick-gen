# Coder Nickname Generator

A full-stack Flask application that analyzes your coding habits, intelligence, and skills to generate a unique digital identity, custom SVG avatar, and a distinct nickname.

## Features

- **Coding Habit Analyzer**: Evaluates your efficiency based on coding hours, frequency, and session preference (Day/Night).
- **Adaptive Intelligence Quiz**: Dynamically selects at least 15 MCQs from a pool of programming and logic questions based on your chosen languages (e.g., Python, Java, JS).
- **Programming Skill Badges**: Maps your self-evaluated language proficiency to "Beginner", "Intermediate", or "Advanced" professional badges.
- **Dynamic SVG Avatar Generator**: Generates custom, data-driven SVG avatars offline based on your intelligence level and coding profile.
- **Rule-Based Nickname Engine**: Constructs unique identities (e.g., "Rising Night Owl Engineer") using a multi-factor logic pipeline.
- **Team Mode**: Allows teams to be created and provides consolidated skill analysis and squad name suggestions.
- **Interview Readiness**: Analyzes your interview performance and technical confidence to provide actionable improvement plans.

## Tech Stack

- **Backend**: Python 3.9+, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2
- **Services**: Modular, service-oriented architecture for analysis and generation

## Project Structure

```text
Nick-gen/
├── app.py                  # Main entry point and route definitions
├── config.py               # Application configuration and environment variables
├── constants.py            # Centralized quiz questions and game constants
├── extensions.py           # Database and extension initialization
├── requirements.txt        # Python package dependencies
├── models/                 # Database Models
│   ├── user.py             # User profile and analysis storage
│   ├── skill.py            # Skills associated with users
│   └── team.py             # Team and squad management
├── services/               # Core Business Logic
│   ├── data_aggregator.py  # Form data processing
│   ├── analyzer_engine.py  # Habit and intelligence level scoring
│   ├── nickname_engine.py  # Identity generation logic
│   ├── avatar_generator.py # Procedural SVG avatar creation
│   ├── team_engine.py      # Collective team analysis
│   └── interview_analyzer.py # Career and readiness feedback
├── templates/              # Flask/Jinja2 HTML templates
└── static/                 # Static assets (CSS, JS, Generated Avatars)
```

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

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
The application will be accessible at `http://127.0.0.1:5000/`.

## Usage
1. **Home**: Enter your name and select your coding habits and languages.
2. **Quiz**: Take the dynamically generated quiz based on your profile.
3. **Identity**: View your custom nickname, professional badges, and generated avatar.
4. **Dashboard**: Track all generated profiles and their stats.
5. **Team Mode**: Form groups and see how your collective skills measure up.
6. **Career/Interview**: Get technical confidence analysis.
