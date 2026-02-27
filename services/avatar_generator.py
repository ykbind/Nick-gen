import os
import uuid

class AvatarGenerator:
    """Generates offline SVG avatars based on user analysis."""

    COLORS = {
        'Beginner': '#6c757d', # Gray
        'Intermediate': '#007bff', # Blue
        'Pro': '#28a745' # Green
    }

    HABIT_DECOR = {
        'Night Owl': '<circle cx="50" cy="50" r="45" fill="#2c3e50"/><path d="M70 20 A30 30 0 1 0 70 80" fill="#f1c40f"/>', # Moon/Dark
        'Bug Hunter': '<circle cx="50" cy="50" r="45" fill="#c0392b"/><path d="M30 30 L70 70 M30 70 L70 30" stroke="white" stroke-width="5"/>', # Red/Cross
        'Consistency King': '<circle cx="50" cy="50" r="45" fill="#8e44ad"/><rect x="30" y="30" width="40" height="40" fill="white" fill-opacity="0.3"/>',
        'Sprint Coder': '<circle cx="50" cy="50" r="45" fill="#d35400"/><path d="M50 10 L40 50 L60 50 L50 90" fill="yellow"/>' # Lightning
    }

    @classmethod
    def generate_svg(cls, user_id: str, intel_level: str, habit_tag: str, top_skill_badge: str) -> str:
        color = cls.COLORS.get(intel_level, '#343a40')
        habit_svg = cls.HABIT_DECOR.get(habit_tag, f'<circle cx="50" cy="50" r="45" fill="{color}"/>')
        
        # Sparkles for Advanced skills
        sparkle = ''
        if top_skill_badge == 'Advanced':
            sparkle = '<circle cx="15" cy="15" r="2" fill="white"/><circle cx="85" cy="15" r="2" fill="white"/><circle cx="85" cy="85" r="2" fill="white"/><circle cx="15" cy="85" r="2" fill="white"/>'

        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
<defs>
    <filter id="shadow">
        <feDropShadow dx="0" dy="1" stdDeviation="1" flood-opacity="0.3"/>
    </filter>
</defs>
{habit_svg}
<g filter="url(#shadow)">
    <circle cx="50" cy="40" r="18" fill="white" fill-opacity="0.8"/>
    <path d="M25 80 Q50 60 75 80" stroke="white" stroke-width="6" fill="none" stroke-linecap="round"/>
</g>
<circle cx="50" cy="50" r="48" fill="none" stroke="{color}" stroke-width="2"/>
<text x="50" y="92" font-family="Arial, sans-serif" font-size="7" font-weight="bold" text-anchor="middle" fill="white" style="text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">{intel_level.upper()}</text>
{sparkle}
</svg>"""
        
        import base64
        return f"data:image/svg+xml;base64,{base64.b64encode(svg_content.strip().encode()).decode()}"
