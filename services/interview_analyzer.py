from typing import Dict, List, Any

class InterviewAnalyzer:
    """Analyzes personal traits and interview readiness."""

    @staticmethod
    def analyze(data: Dict[str, Any]) -> Dict[str, Any]:
        strengths = []
        weaknesses = []
        improvements = []

        if data['confidence'] >= 4:
            strengths.append("High Presentation Confidence")
        else:
            weaknesses.append("Lack of Presentation Confidence")
            improvements.append("Practice mock interviews to build voice clarity.")

        if data['dsa_knowledge'] >= 4:
            strengths.append("Strong Algorithmic Foundation")
        elif data['dsa_knowledge'] <= 2:
            weaknesses.append("DSA Fundamentals")
            improvements.append("Focus on Big O, Trees, and Dynamic Programming.")

        if data['communication'] >= 4:
            strengths.append("Clear Explanatory Skills")
        else:
            weaknesses.append("Complex Concept Articulation")
            improvements.append("Try explaining code line-by-line to peers.")

        if data['experience'] >= 4:
            strengths.append("Robust Practical Experience")
        elif data['experience'] <= 2:
            weaknesses.append("Limited Project Portfolio")
            improvements.append("Build 2 more full-stack projects using modern frameworks.")

        return {
            'strengths': strengths,
            'weaknesses': weaknesses,
            'improvements': improvements
        }
