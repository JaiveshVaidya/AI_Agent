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
    
    def generate_job_search_query(self, job_title, experience, skills, expected_salary):
        """Generate a comprehensive job search strategy using Gemini AI"""
        
        prompt = f"""
        You are a professional career advisor and job search expert. Help create a comprehensive job search strategy based on the following parameters:

        Job Title: {job_title}
        Experience Level: {experience}
        Skills: {skills}
        Expected Salary: {expected_salary}

        Please provide a detailed response that includes:

        1. **Optimized Job Search Keywords**: Suggest the best keywords and phrases to use when searching for this position on job boards.

        2. **Job Board Recommendations**: Recommend the top 5-7 job boards and platforms where this type of position is commonly posted.

        3. **Skills Gap Analysis**: Based on the provided skills, identify any additional skills that would make the candidate more competitive for this role.

        4. **Salary Insights**: Provide insights about the salary expectations for this role and experience level, including factors that might affect compensation.

        5. **Application Strategy**: Suggest the best approach for applying to these positions, including:
           - How to tailor resumes for this role
           - Key points to highlight in cover letters
           - Interview preparation tips

        6. **Networking Opportunities**: Suggest professional networks, communities, or events where one could connect with professionals in this field.

        7. **Company Types**: Recommend types of companies (startups, enterprises, specific industries) that typically hire for this role.

        8. **Timeline and Expectations**: Provide realistic expectations about the job search timeline for this level of position.

        Format your response in a clear, organized manner with proper headings and bullet points for easy reading.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            logging.error(f"Error generating job search query: {str(e)}")
            return f"Error generating job search strategy: {str(e)}"
    
    def analyze_job_market_trends(self, job_title, skills):
        """Analyze current job market trends for the specified role"""
        
        prompt = f"""
        As a job market analyst, provide insights about current market trends for:

        Job Title: {job_title}
        Skills: {skills}

        Please analyze and provide:

        1. **Market Demand**: Current demand for this role in the job market
        2. **Growth Trends**: Whether this field is growing, stable, or declining
        3. **Emerging Skills**: New skills that are becoming important in this field
        4. **Remote Work Opportunities**: Availability of remote/hybrid positions
        5. **Geographic Hotspots**: Cities or regions with high demand for this role
        6. **Industry Trends**: Key trends affecting this profession

        Keep the response concise but informative.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            logging.error(f"Error analyzing job market trends: {str(e)}")
            return f"Error analyzing market trends: {str(e)}"
    
    def generate_resume_tips(self, job_title, experience, skills):
        """Generate personalized resume optimization tips"""
        
        prompt = f"""
        As a professional resume writer, provide specific resume optimization tips for:

        Target Job Title: {job_title}
        Experience Level: {experience}
        Current Skills: {skills}

        Provide actionable advice on:

        1. **Resume Structure**: Best format for this experience level
        2. **Key Sections**: Essential sections to include
        3. **Skills Presentation**: How to best showcase the provided skills
        4. **Experience Description**: How to describe work experience effectively
        5. **Keywords**: Important keywords to include for ATS systems
        6. **Common Mistakes**: What to avoid for this type of role

        Keep recommendations specific and actionable.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            logging.error(f"Error generating resume tips: {str(e)}")
            return f"Error generating resume tips: {str(e)}"