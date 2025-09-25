import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Job Search AI application"""
    
    # Gemini AI Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = 'gemini-1.5-flash'
    
    # Application Configuration
    APP_TITLE = "Job Search AI Assistant"
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
    
    # Job Search Parameters
    DEFAULT_EXPERIENCE_LEVELS = [
        "Entry Level (0-2 years)",
        "Mid Level (3-5 years)",
        "Senior Level (6-10 years)",
        "Lead/Principal (10+ years)",
        "Executive Level"
    ]
    
    DEFAULT_SALARY_RANGES = [
        "Not specified",
        "$30,000 - $50,000",
        "$50,000 - $70,000",
        "$70,000 - $100,000",
        "$100,000 - $150,000",
        "$150,000 - $200,000",
        "$200,000+"
    ]