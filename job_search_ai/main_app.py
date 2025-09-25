import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import threading
import logging
from config import Config
from gemini_client import GeminiClient
from gui_components import (
    ModernButton, ModernEntry, ModernComboBox, ModernTextArea, 
    ModernLabel, ModernFrame, LoadingDialog, ResultsDialog
)

# Configure logging
logging.basicConfig(level=logging.INFO)

class JobSearchAI:
    """Main application class for Job Search AI"""
    
    def __init__(self):
        self.root = ctk.CTk()
        self.gemini_client = None
        self.loading_dialog = None
        
        # Initialize the application
        self.setup_window()
        self.create_widgets()
        self.initialize_gemini()
    
    def setup_window(self):
        """Setup the main application window"""
        self.root.title(Config.APP_TITLE)
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
        self.root.minsize(Config.MIN_WINDOW_WIDTH, Config.MIN_WINDOW_HEIGHT)
        
        # Center the window
        self.center_window()
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - Config.WINDOW_WIDTH) // 2
        y = (screen_height - Config.WINDOW_HEIGHT) // 2
        
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}+{x}+{y}")
    
    def initialize_gemini(self):
        """Initialize Gemini AI client"""
        try:
            self.gemini_client = GeminiClient()
            self.status_label.configure(text="✅ AI Assistant Ready")
        except Exception as e:
            self.status_label.configure(text="❌ AI Assistant Error - Check API Key")
            logging.error(f"Failed to initialize Gemini client: {str(e)}")
    
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main container
        main_container = ModernFrame(self.root)
        main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Header
        self.create_header(main_container)
        
        # Content area
        content_frame = ModernFrame(main_container)
        content_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Left panel - Input form
        self.create_input_panel(content_frame)
        
        # Right panel - Quick actions
        self.create_actions_panel(content_frame)
        
        # Footer
        self.create_footer(main_container)
    
    def create_header(self, parent):
        """Create the application header"""
        header_frame = ModernFrame(parent)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        header_frame.grid_columnconfigure(1, weight=1)
        
        # App icon and title
        title_label = ModernLabel(
            header_frame, 
            text="🤖 Job Search AI Assistant", 
            size=24, 
            weight="bold"
        )
        title_label.grid(row=0, column=0, sticky="w", padx=20, pady=15)
        
        # Version label
        version_label = ModernLabel(
            header_frame, 
            text=f"v{Config.APP_VERSION}", 
            size=10
        )
        version_label.grid(row=0, column=1, sticky="e", padx=20, pady=15)
    
    def create_input_panel(self, parent):
        """Create the input form panel"""
        input_frame = ModernFrame(parent)
        input_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        input_frame.grid_columnconfigure(0, weight=1)
        
        # Panel title
        panel_title = ModernLabel(
            input_frame, 
            text="📝 Job Search Parameters", 
            size=16, 
            weight="bold"
        )
        panel_title.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))
        
        # Form fields
        form_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        form_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 20))
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Job Title
        ModernLabel(form_frame, text="Job Title:", size=12, weight="bold").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.job_title_entry = ModernEntry(
            form_frame, 
            placeholder_text="e.g., Software Engineer, Data Scientist, Product Manager"
        )
        self.job_title_entry.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        
        # Experience Level
        ModernLabel(form_frame, text="Experience Level:", size=12, weight="bold").grid(
            row=1, column=0, sticky="w", pady=(0, 5)
        )
        self.experience_combo = ModernComboBox(
            form_frame, 
            values=Config.DEFAULT_EXPERIENCE_LEVELS
        )
        self.experience_combo.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.experience_combo.set(Config.DEFAULT_EXPERIENCE_LEVELS[0])
        
        # Skills
        ModernLabel(form_frame, text="Skills:", size=12, weight="bold").grid(
            row=2, column=0, sticky="nw", pady=(5, 5)
        )
        self.skills_text = ModernTextArea(form_frame, height=80)
        self.skills_text.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.skills_text.insert("1.0", "e.g., Python, JavaScript, React, SQL, Machine Learning, Project Management...")
        
        # Expected Salary
        ModernLabel(form_frame, text="Expected Salary:", size=12, weight="bold").grid(
            row=3, column=0, sticky="w", pady=(0, 5)
        )
        self.salary_combo = ModernComboBox(
            form_frame, 
            values=Config.DEFAULT_SALARY_RANGES
        )
        self.salary_combo.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=(0, 20))
        self.salary_combo.set(Config.DEFAULT_SALARY_RANGES[0])
        
        # Search button
        self.search_button = ModernButton(
            input_frame,
            text="🔍 Generate Job Search Strategy",
            command=self.generate_job_search_strategy,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.search_button.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
    
    def create_actions_panel(self, parent):
        """Create the quick actions panel"""
        actions_frame = ModernFrame(parent)
        actions_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        # Panel title
        panel_title = ModernLabel(
            actions_frame, 
            text="⚡ Quick Actions", 
            size=16, 
            weight="bold"
        )
        panel_title.pack(pady=(20, 15), padx=20, anchor="w")
        
        # Action buttons
        buttons_frame = ctk.CTkFrame(actions_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Market Trends button
        trends_btn = ModernButton(
            buttons_frame,
            text="📈 Analyze Market Trends",
            command=self.analyze_market_trends,
            height=45
        )
        trends_btn.pack(fill="x", pady=(0, 10))
        
        # Resume Tips button
        resume_btn = ModernButton(
            buttons_frame,
            text="📄 Get Resume Tips",
            command=self.get_resume_tips,
            height=45
        )
        resume_btn.pack(fill="x", pady=(0, 10))
        
        # Clear Form button
        clear_btn = ModernButton(
            buttons_frame,
            text="🗑️ Clear Form",
            command=self.clear_form,
            height=45,
            fg_color="#FF6B6B",
            hover_color="#FF5252"
        )
        clear_btn.pack(fill="x", pady=(0, 20))
        
        # Tips section
        tips_frame = ModernFrame(actions_frame)
        tips_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        tips_title = ModernLabel(
            tips_frame, 
            text="💡 Pro Tips", 
            size=14, 
            weight="bold"
        )
        tips_title.pack(pady=(15, 10), anchor="w")
        
        tips_text = ModernLabel(
            tips_frame,
            text="• Be specific with job titles\n• List relevant skills clearly\n• Consider market salary ranges\n• Update your LinkedIn profile\n• Network within your industry\n• Customize applications for each role",
            size=10,
            justify="left"
        )
        tips_text.pack(padx=10, pady=(0, 15), anchor="w")
    
    def create_footer(self, parent):
        """Create the application footer"""
        footer_frame = ModernFrame(parent)
        footer_frame.grid(row=2, column=0, sticky="ew", pady=(20, 0))
        footer_frame.grid_columnconfigure(1, weight=1)
        
        # Status label
        self.status_label = ModernLabel(
            footer_frame, 
            text="🔄 Initializing AI Assistant...", 
            size=10
        )
        self.status_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        # Powered by label
        powered_label = ModernLabel(
            footer_frame, 
            text="Powered by Google Gemini AI", 
            size=10
        )
        powered_label.grid(row=0, column=1, sticky="e", padx=20, pady=10)
    
    def validate_inputs(self):
        """Validate user inputs"""
        job_title = self.job_title_entry.get().strip()
        skills = self.skills_text.get("1.0", "end-1c").strip()
        
        if not job_title:
            messagebox.showerror("Validation Error", "Please enter a job title.")
            return False
        
        if not skills or skills.startswith("e.g.,"):
            messagebox.showerror("Validation Error", "Please enter your skills.")
            return False
        
        return True
    
    def get_form_data(self):
        """Get data from form fields"""
        return {
            'job_title': self.job_title_entry.get().strip(),
            'experience': self.experience_combo.get(),
            'skills': self.skills_text.get("1.0", "end-1c").strip(),
            'expected_salary': self.salary_combo.get()
        }
    
    def generate_job_search_strategy(self):
        """Generate comprehensive job search strategy"""
        if not self.validate_inputs():
            return
        
        if not self.gemini_client:
            messagebox.showerror("Error", "AI Assistant is not available. Please check your API key.")
            return
        
        # Get form data
        data = self.get_form_data()
        
        # Show loading dialog
        self.loading_dialog = LoadingDialog(self.root, "Generating Strategy...")
        
        # Run AI generation in separate thread
        thread = threading.Thread(
            target=self._generate_strategy_thread,
            args=(data,)
        )
        thread.daemon = True
        thread.start()
    
    def _generate_strategy_thread(self, data):
        """Thread function for generating strategy"""
        try:
            self.loading_dialog.update_status("Analyzing your requirements...")
            
            # Generate strategy using Gemini AI
            strategy = self.gemini_client.generate_job_search_query(
                data['job_title'],
                data['experience'],
                data['skills'],
                data['expected_salary']
            )
            
            # Close loading dialog and show results
            self.root.after(0, self._show_strategy_results, strategy)
            
        except Exception as e:
            self.root.after(0, self._show_error, f"Error generating strategy: {str(e)}")
    
    def _show_strategy_results(self, strategy):
        """Show strategy results in a dialog"""
        if self.loading_dialog:
            self.loading_dialog.close()
        
        ResultsDialog(self.root, "Job Search Strategy", strategy)
    
    def _show_error(self, error_message):
        """Show error message"""
        if self.loading_dialog:
            self.loading_dialog.close()
        
        messagebox.showerror("Error", error_message)
    
    def analyze_market_trends(self):
        """Analyze job market trends"""
        job_title = self.job_title_entry.get().strip()
        skills = self.skills_text.get("1.0", "end-1c").strip()
        
        if not job_title:
            messagebox.showerror("Validation Error", "Please enter a job title first.")
            return
        
        if not self.gemini_client:
            messagebox.showerror("Error", "AI Assistant is not available.")
            return
        
        # Show loading dialog
        self.loading_dialog = LoadingDialog(self.root, "Analyzing Market Trends...")
        
        # Run analysis in separate thread
        thread = threading.Thread(
            target=self._analyze_trends_thread,
            args=(job_title, skills)
        )
        thread.daemon = True
        thread.start()
    
    def _analyze_trends_thread(self, job_title, skills):
        """Thread function for analyzing trends"""
        try:
            trends = self.gemini_client.analyze_job_market_trends(job_title, skills)
            self.root.after(0, self._show_trends_results, trends)
        except Exception as e:
            self.root.after(0, self._show_error, f"Error analyzing trends: {str(e)}")
    
    def _show_trends_results(self, trends):
        """Show trends results"""
        if self.loading_dialog:
            self.loading_dialog.close()
        
        ResultsDialog(self.root, "Market Trends Analysis", trends)
    
    def get_resume_tips(self):
        """Get personalized resume tips"""
        if not self.validate_inputs():
            return
        
        if not self.gemini_client:
            messagebox.showerror("Error", "AI Assistant is not available.")
            return
        
        data = self.get_form_data()
        
        # Show loading dialog
        self.loading_dialog = LoadingDialog(self.root, "Generating Resume Tips...")
        
        # Run generation in separate thread
        thread = threading.Thread(
            target=self._generate_resume_tips_thread,
            args=(data,)
        )
        thread.daemon = True
        thread.start()
    
    def _generate_resume_tips_thread(self, data):
        """Thread function for generating resume tips"""
        try:
            tips = self.gemini_client.generate_resume_tips(
                data['job_title'],
                data['experience'],
                data['skills']
            )
            self.root.after(0, self._show_resume_tips_results, tips)
        except Exception as e:
            self.root.after(0, self._show_error, f"Error generating resume tips: {str(e)}")
    
    def _show_resume_tips_results(self, tips):
        """Show resume tips results"""
        if self.loading_dialog:
            self.loading_dialog.close()
        
        ResultsDialog(self.root, "Resume Optimization Tips", tips)
    
    def clear_form(self):
        """Clear all form fields"""
        self.job_title_entry.delete(0, 'end')
        self.experience_combo.set(Config.DEFAULT_EXPERIENCE_LEVELS[0])
        self.skills_text.delete("1.0", "end")
        self.skills_text.insert("1.0", "e.g., Python, JavaScript, React, SQL, Machine Learning, Project Management...")
        self.salary_combo.set(Config.DEFAULT_SALARY_RANGES[0])
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    """Main function to run the application"""
    try:
        app = JobSearchAI()
        app.run()
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        messagebox.showerror("Application Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()