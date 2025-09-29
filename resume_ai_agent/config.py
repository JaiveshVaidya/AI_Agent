import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResumeTemplates:
    """Reusable templates for resume sections."""

    HEADER = """### {name}\n**Target Role:** {target_role}\n**Experience Level:** {experience}\n"""

    SUMMARY = """### Professional Summary\n{summary}\n"""

    EXPERIENCE = """### Experience Highlights\n{experience_highlights}\n"""

    ACHIEVEMENTS = """### Key Achievements\n{achievements}\n"""

    SKILLS = """### Core Competencies\n{skills}\n"""

    INDUSTRIES = """### Target Industries\n{industries}\n"""

class Config:
    """Configuration class for the Resume AI Agent"""

    # Gemini AI Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')

    # Application Configuration
    APP_TITLE = "Resume AI Agent"
    APP_VERSION = "1.0.0"

    # GUI Configuration
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    MIN_WINDOW_WIDTH = 800
    MIN_WINDOW_HEIGHT = 600

    # Colors (Modern Dark Theme)
    PRIMARY_COLOR = "#2B2B2B"
    SECONDARY_COLOR = "#3C3C3C"
    ACCENT_COLOR = "#007ACC"
    SUCCESS_COLOR = "#4CAF50"
    WARNING_COLOR = "#FF9800"
    ERROR_COLOR = "#F44336"
    TEXT_COLOR = "#FFFFFF"
    SECONDARY_TEXT_COLOR = "#B0B0B0"

    # Experience options reused from job search app
    DEFAULT_EXPERIENCE_LEVELS = [
        "Entry Level (0-2 years)",
        "Mid Level (3-5 years)",
        "Senior Level (6-10 years)",
        "Lead/Principal (10+ years)",
        "Executive Level"
    ]