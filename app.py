import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from extensions import db
from config import Config

def create_app():
    """Application factory to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # MongoDB handles collection creation on first insert
        pass

    return app

app = create_app()

# Import Services
from services.data_aggregator import DataAggregator
from services.analyzer_engine import AnalyzerEngine
from services.nickname_engine import NicknameEngine
from services.avatar_generator import AvatarGenerator
from services.team_engine import TeamEngine
from services.interview_analyzer import InterviewAnalyzer
from models.user import User
from models.team import Team
from constants import CATEGORIZED_QUESTIONS
import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-analysis', methods=['POST'])
def start_analysis():
    # Store initial data in session
    session['user_name'] = request.form.get('name')
    session['habit_data'] = DataAggregator.aggregate_habit_data(request.form)
    
    languages = request.form.getlist('languages[]')
    levels = request.form.getlist('levels[]')
    session['skill_data'] = DataAggregator.aggregate_skill_data(languages, levels)
    
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    # Dynamically select at least 15 questions based on user's interests
    skill_data = session.get('skill_data', [])
    user_languages = [s['language'].upper() for s in skill_data]
    
    question_pool = []
    
    # 1. Pull from user's specific languages
    for lang in user_languages:
        if lang in CATEGORIZED_QUESTIONS:
            # Pick a subset of questions from each language to ensure diversity
            # For Python, we'll try to include more as requested
            count = 5 if lang == "PYTHON" else 4
            pool = list(CATEGORIZED_QUESTIONS[lang])
            if len(pool) < count:
                count = len(pool)
            question_pool.extend(random.sample(pool, count))

    # 2. Fill the rest from the DEV / General pool
    dev_pool = list(CATEGORIZED_QUESTIONS['DEV'])
    
    # We want at least 15 questions total
    remaining = max(15 - len(question_pool), 5) # At least 5 dev questions for generality
    if len(dev_pool) < remaining:
        remaining = len(dev_pool)
    question_pool.extend(random.sample(dev_pool, remaining))
    
    # Shuffle the final selection
    random.shuffle(question_pool)
    
    # Store the actual question dictionaries in the session for evaluation
    session['current_quiz'] = question_pool
    
    return render_template('quiz.html', questions=question_pool)

@app.route('/evaluate-quiz', methods=['POST'])
def evaluate_quiz():
    # Retrieve the questions that were actually asked
    asked_questions = session.get('current_quiz', [])
    
    user_answers = [request.form.get(f'q{i}') for i in range(len(asked_questions))]
    correct_answers = [q['answer'] for q in asked_questions]
    
    intel_results = AnalyzerEngine.analyze_intelligence(user_answers, correct_answers)
    habit_results = AnalyzerEngine.analyze_habits(session.get('habit_data', {}))
    processed_skills = AnalyzerEngine.process_skills(session.get('skill_data', []))
    
    # Get top skill badge for nickname gen
    top_badge = "Beginner"
    if processed_skills:
        top_skill = max(processed_skills, key=lambda x: x['level'])
        top_badge = top_skill['badge']

    # Generate Nickname
    nickname = NicknameEngine.generate(intel_results['level'], habit_results['tag'], top_badge)
    
    # Save to MongoDB
    new_user = User.create(
        name=session.get('user_name'),
        habit_score=habit_results['score'],
        habit_tag=habit_results['tag'],
        intelligence_score=intel_results['score'],
        intelligence_level=intel_results['level'],
        nickname=nickname
    )
    user_id = new_user["_id"]
    
    # Add Skills
    for s in processed_skills:
        User.add_skill(user_id, {
            'language': s['language'], 
            'expertise_level': s['level'], 
            'badge': s['badge']
        })
    
    # Generate Avatar (Now returns Base64 string for Vercel support)
    avatar_data = AvatarGenerator.generate_svg(
        str(user_id), 
        intel_results['level'], 
        habit_results['tag'], 
        top_badge
    )
    User.update_avatar(user_id, avatar_data)
    
    session['last_user_id'] = str(user_id)
    return redirect(url_for('result', user_id=str(user_id)))

@app.route('/result/<user_id>')
def result(user_id):
    user = User.get_by_id(user_id)
    if not user:
        flash("User not found!")
        return redirect(url_for('index'))
    return render_template('result.html', user=user)

@app.route('/dashboard')
def dashboard():
    users = User.get_all()
    return render_template('dashboard.html', users=users)

@app.route('/team-mode')
def team_list():
    teams = Team.get_all()
    
    # Simple analysis based on all users
    all_users = User.get_all()
    analysis = None
    if all_users:
        members_data = []
        for u in all_users:
            members_data.append({
                'intelligence_score': u['intelligence_score'],
                'habit_tag': u['habit_tag'],
                'skills': u['skills']
            })
        analysis = TeamEngine.generate_team_analysis(members_data)
        
    return render_template('team.html', teams=teams, team_analysis=analysis)

@app.route('/create-team', methods=['POST'])
def create_team():
    name = request.form.get('team_name')
    Team.create(name)
    flash(f'Team "{name}" created successfully!')
    return redirect(url_for('team_list'))

@app.route('/interview')
def interview():
    return render_template('interview.html')

@app.route('/analyze-interview', methods=['POST'])
def analyze_interview():
    data = DataAggregator.aggregate_interview_data(request.form)
    result = InterviewAnalyzer.analyze(data)
    return render_template('interview.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

# Vercel entry point
main = app
