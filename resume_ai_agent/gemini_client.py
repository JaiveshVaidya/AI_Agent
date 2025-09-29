import google.generativeai as genai
from config import Config
import logging

class GeminiClient:
    """Client for interacting with Google's Gemini AI model"""
    
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.model_name = Config.GEMINI_MODEL
        self.model = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Gemini AI client"""
        try:
            if not self.api_key:
                raise ValueError("Gemini API key not found. Please set GEMINI_API_KEY in your .env file")
            
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            logging.info("Gemini AI client initialized successfully")
            
        except Exception as e:
            logging.error(f"Failed to initialize Gemini AI client: {str(e)}")
            raise
    
    def generate_resume_sections(self, profile_data):
        """Generate resume sections tailored to the user's profile and target role."""

        prompt = f"""
        You are an expert resume writer creating tailored resume content. Use the details below to craft a professional resume draft:

        Candidate Name: {profile_data['name'] or 'Candidate'}
        Current Role: {profile_data['current_role'] or 'Not specified'}
        Experience Level: {profile_data['experience']}
        Core Skills: {profile_data['skills']}
        Achievements: {profile_data['achievements']}
        Target Role: {profile_data['target_role']}
        Target Industries: {profile_data['industries']}
        Job Requirements: {profile_data['requirements']}

        Produce a markdown-formatted resume draft that includes:
        - A concise professional summary aligned with the target role
        - 4-5 bullet points highlighting relevant experience and accomplishments
        - A dedicated achievements section leveraging provided highlights (focus on metrics)
        - A core competencies section grouping skills into categories
        - Optional industry alignment notes if industries are provided

        Ensure content is ATS-friendly, uses strong action verbs, and incorporates keywords from the target role and requirements.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception as e:
            logging.error(f"Error generating resume content: {str(e)}")
            return f"Error generating resume content: {str(e)}"