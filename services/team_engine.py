from typing import List, Dict, Any

class TeamEngine:
    """Logic for team classification and name generation."""

    @staticmethod
    def generate_team_analysis(members: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not members:
            return {}

        # Combine languages
        all_langs = {}
        total_intel = 0
        habit_counts = {}

        for m in members:
            total_intel += m['intelligence_score']
            h_tag = m['habit_tag']
            habit_counts[h_tag] = habit_counts.get(h_tag, 0) + 1
            
            for s in m['skills']:
                lang = s['language']
                all_langs[lang] = all_langs.get(lang, 0) + s['expertise_level']

        # Most common habit tag
        prevalent_habit = max(habit_counts, key=habit_counts.get)
        # Strongest language
        strongest_lang = max(all_langs, key=all_langs.get)
        # Average intelligence
        avg_intel = total_intel / len(members)

        # Name Generation
        prefixes = ['Neural', 'Binary', 'Stack', 'Logic', 'Code', 'Cyber']
        suffixes = ['Hackers', 'Titans', 'Spartans', 'Dominators', 'Wizards', 'Devs']
        
        import random
        team_name = f"{random.choice(prefixes)} {random.choice(suffixes)}"

        return {
            'team_name': team_name,
            'avg_intelligence': avg_intel,
            'primary_tech': strongest_lang,
            'dominant_habit': prevalent_habit
        }
