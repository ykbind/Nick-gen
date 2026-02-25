import random
from typing import Dict, Any, List

class NicknameEngine:
    """Generates unique nicknames based on user data analysis."""

    PREFIXES = {
        'Beginner': ['Learning', 'Rising', 'Fresh', 'Aspiring'],
        'Intermediate': ['Logic', 'Binary', 'Script', 'Array'],
        'Pro': ['Ultra', 'Cyber', 'Neural', 'Quantum']
    }

    CORE_WORDS = {
        'Night Owl': ['Moon', 'Shadow', 'Eclipse', 'Nocturnal'],
        'Bug Hunter': ['Titan', 'Slayer', 'Glitch', 'Exterminator'],
        'Consistency King': ['Zen', 'Steady', 'Mountain', 'Immutable'],
        'Sprint Coder': ['Storm', 'Flash', 'Volt', 'Turbo']
    }

    SUFFIXES = {
        'Advanced': ['Architect', 'Master', 'WIZARD', 'Elite'],
        'Intermediate': ['Developer', 'Engineer', 'Coder', 'Ninja'],
        'Beginner': ['Associate', 'Enthusiast', 'Prodigy', 'Trainee']
    }

    @classmethod
    def generate(cls, intel_level: str, habit_tag: str, top_skill_badge: str) -> str:
        """
        Formula: Prefix (intelligence) + Core (habit) + Suffix (skill badge)
        """
        prefix = random.choice(cls.PREFIXES.get(intel_level, ['Code']))
        core = random.choice(cls.CORE_WORDS.get(habit_tag, ['Warrior']))
        suffix = random.choice(cls.SUFFIXES.get(top_skill_badge, ['Pro']))
        
        return f"{prefix} {core} {suffix}"
