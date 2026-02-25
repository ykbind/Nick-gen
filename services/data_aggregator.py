from typing import Dict, Any

class DataAggregator:
    """Consolidates user input from multiple sources/forms into a single unified profile."""

    @staticmethod
    def aggregate_habit_data(form_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'hours': int(form_data.get('hours', 0)),
            'frequency': int(form_data.get('frequency', 0)),
            'preference': form_data.get('preference', 'Day'),
            'debug_skill': int(form_data.get('debug_skill', 1)),
            'consistency': int(form_data.get('consistency', 1))
        }

    @staticmethod
    def aggregate_skill_data(languages: list, levels: list) -> list:
        skills = []
        for lang, lvl in zip(languages, levels):
            if lang:
                skills.append({
                    'language': lang,
                    'level': int(lvl)
                })
        return skills

    @staticmethod
    def aggregate_interview_data(form_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'confidence': int(form_data.get('confidence', 1)),
            'dsa_knowledge': int(form_data.get('dsa', 1)),
            'communication': int(form_data.get('comm', 1)),
            'experience': int(form_data.get('exp', 1))
        }
