from typing import Dict, Any, List

class AnalyzerEngine:
    """Analyzes aggregated data to produce scores, classifications, and tags."""

    @staticmethod
    def analyze_habits(data: Dict[str, Any]) -> Dict[str, Any]:
        # Simple scoring formula
        raw_score = (data['hours'] * 10) + (data['frequency'] * 5) + (data['debug_skill'] * 10) + (data['consistency'] * 10)
        habit_score = min(100, raw_score)
        
        # Determine tag
        if data['preference'] == 'Night' and data['hours'] > 6:
            tag = "Night Owl"
        elif data['debug_skill'] >= 4:
            tag = "Bug Hunter"
        elif data['consistency'] >= 4:
            tag = "Consistency King"
        else:
            tag = "Sprint Coder"
            
        return {
            'score': habit_score,
            'tag': tag
        }

    @staticmethod
    def analyze_intelligence(quiz_answers: List[str], correct_answers: List[str]) -> Dict[str, Any]:
        correct_count = sum(1 for a, b in zip(quiz_answers, correct_answers) if a == b)
        score = (correct_count / len(correct_answers)) * 100
        
        if score <= 40:
            level = "Beginner"
        elif score <= 70:
            level = "Intermediate"
        else:
            level = "Pro"
            
        return {
            'score': int(score),
            'level': level
        }

    @staticmethod
    def process_skills(skills: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for skill in skills:
            lvl = skill['level']
            if lvl <= 2:
                skill['badge'] = "Beginner"
            elif lvl <= 4:
                skill['badge'] = "Intermediate"
            else:
                skill['badge'] = "Advanced"
        return skills
