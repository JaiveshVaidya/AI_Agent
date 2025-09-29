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

logging.basicConfig(level=logging.INFO)

class ResumeAIAgent:
    """Main application class for the Resume AI Agent"""

    def __init__(self):
        self.root = ctk.CTk()
        self.gemini_client = None
        self.loading_dialog = None

        self.setup_window()
        self.create_widgets()
        self.initialize_gemini()

    def setup_window(self):
        self.root.title("Resume AI Agent")
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
        self.root.minsize(Config.MIN_WINDOW_WIDTH, Config.MIN_WINDOW_HEIGHT)
        self.center_window()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - Config.WINDOW_WIDTH) // 2
        y = (screen_height - Config.WINDOW_HEIGHT) // 2
        self.root.geometry(f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}+{x}+{y}")

    def initialize_gemini(self):
        try:
            self.gemini_client = GeminiClient()
            self.status_label.configure(text="✅ Gemini Ready")
        except Exception as exc:
            self.status_label.configure(text="❌ Gemini Error - Check API Key")
            logging.error("Failed to initialize Gemini client: %s", exc)

    def create_widgets(self):
        main_container = ModernFrame(self.root)
        main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_container.grid_rowconfigure(1, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        self.create_header(main_container)
        content_frame = ModernFrame(main_container)
        content_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)

        self.create_profile_panel(content_frame)
        self.create_job_requirements_panel(content_frame)
        self.create_footer(main_container)

    def create_header(self, parent):
        header_frame = ModernFrame(parent)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        header_frame.grid_columnconfigure(1, weight=1)

        title_label = ModernLabel(
            header_frame,
            text="🧠 Resume AI Agent",
            size=24,
            weight="bold"
        )
        title_label.grid(row=0, column=0, sticky="w", padx=20, pady=15)

        version_label = ModernLabel(
            header_frame,
            text=f"v{Config.APP_VERSION}",
            size=10
        )
        version_label.grid(row=0, column=1, sticky="e", padx=20, pady=15)

    def create_profile_panel(self, parent):
        profile_frame = ModernFrame(parent)
        profile_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        profile_frame.grid_columnconfigure(0, weight=1)

        panel_title = ModernLabel(
            profile_frame,
            text="👤 Your Profile",
            size=16,
            weight="bold"
        )
        panel_title.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        form_frame = ctk.CTkFrame(profile_frame, fg_color="transparent")
        form_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 20))
        form_frame.grid_columnconfigure(1, weight=1)

        ModernLabel(form_frame, text="Name:", size=12, weight="bold").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.name_entry = ModernEntry(
            form_frame,
            placeholder_text="e.g., Jane Doe"
        )
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))

        ModernLabel(form_frame, text="Current Role:", size=12, weight="bold").grid(
            row=1, column=0, sticky="w", pady=(0, 5)
        )
        self.current_role_entry = ModernEntry(
            form_frame,
            placeholder_text="e.g., Backend Developer"
        )
        self.current_role_entry.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))

        ModernLabel(form_frame, text="Years of Experience:", size=12, weight="bold").grid(
            row=2, column=0, sticky="w", pady=(0, 5)
        )
        self.experience_combo = ModernComboBox(
            form_frame,
            values=Config.DEFAULT_EXPERIENCE_LEVELS
        )
        self.experience_combo.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.experience_combo.set(Config.DEFAULT_EXPERIENCE_LEVELS[0])

        ModernLabel(form_frame, text="Core Skills:", size=12, weight="bold").grid(
            row=3, column=0, sticky="nw", pady=(5, 5)
        )
        self.skills_text = ModernTextArea(form_frame, height=80)
        self.skills_text.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.skills_text.insert(
            "1.0",
            "List your key skills, tools, and technologies separated by commas"
        )

        ModernLabel(form_frame, text="Achievements / Highlights:", size=12, weight="bold").grid(
            row=4, column=0, sticky="nw", pady=(5, 5)
        )
        self.achievements_text = ModernTextArea(form_frame, height=80)
        self.achievements_text.grid(row=4, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.achievements_text.insert(
            "1.0",
            "Summarize top achievements, metrics, or noteworthy projects"
        )

        ModernLabel(form_frame, text="Target Industries:", size=12, weight="bold").grid(
            row=5, column=0, sticky="nw", pady=(5, 5)
        )
        self.industries_text = ModernTextArea(form_frame, height=60)
        self.industries_text.grid(row=5, column=1, sticky="ew", padx=(10, 0), pady=(0, 15))
        self.industries_text.insert(
            "1.0",
            "Optional: List industries or company types you are targeting"
        )

    def create_job_requirements_panel(self, parent):
        requirements_frame = ModernFrame(parent)
        requirements_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        requirements_frame.grid_columnconfigure(0, weight=1)

        panel_title = ModernLabel(
            requirements_frame,
            text="📄 Target Role Requirements",
            size=16,
            weight="bold"
        )
        panel_title.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 15))

        form_frame = ctk.CTkFrame(requirements_frame, fg_color="transparent")
        form_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 20))
        form_frame.grid_columnconfigure(0, weight=1)

        ModernLabel(form_frame, text="Target Job Title:", size=12, weight="bold").grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.target_role_entry = ModernEntry(
            form_frame,
            placeholder_text="e.g., Senior Backend Engineer"
        )
        self.target_role_entry.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        ModernLabel(form_frame, text="Job Requirements (optional):", size=12, weight="bold").grid(
            row=2, column=0, sticky="w", pady=(0, 5)
        )
        self.requirements_text = ModernTextArea(form_frame, height=140)
        self.requirements_text.grid(row=3, column=0, sticky="ew", pady=(0, 15))
        self.requirements_text.insert(
            "1.0",
            "Paste key responsibilities or qualifications from a job description"
        )

        primary_action_btn = ModernButton(
            requirements_frame,
            text="✨ Generate Resume Content",
            command=self.generate_resume_content,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        primary_action_btn.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 10))

        reset_btn = ModernButton(
            requirements_frame,
            text="🗑️ Clear All",
            command=self.clear_form,
            height=45,
            fg_color="#FF6B6B",
            hover_color="#FF5252"
        )
        reset_btn.grid(row=3, column=0, sticky="ew", padx=20, pady=(0, 20))

    def create_footer(self, parent):
        footer_frame = ModernFrame(parent)
        footer_frame.grid(row=2, column=0, sticky="ew", pady=(20, 0))
        footer_frame.grid_columnconfigure(1, weight=1)

        self.status_label = ModernLabel(
            footer_frame,
            text="🔄 Initializing Gemini...",
            size=10
        )
        self.status_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        powered_label = ModernLabel(
            footer_frame,
            text="Powered by Google Gemini AI",
            size=10
        )
        powered_label.grid(row=0, column=1, sticky="e", padx=20, pady=10)

    def validate_inputs(self):
        target_role = self.target_role_entry.get().strip()
        skills = self.skills_text.get("1.0", "end-1c").strip()
        if not target_role:
            messagebox.showerror("Validation Error", "Please enter a target job title.")
            return False
        if not skills or skills.startswith("List your key skills"):
            messagebox.showerror("Validation Error", "Please enter your core skills.")
            return False
        return True

    def collect_profile_data(self):
        return {
            "name": self.name_entry.get().strip(),
            "current_role": self.current_role_entry.get().strip(),
            "experience": self.experience_combo.get(),
            "skills": self.skills_text.get("1.0", "end-1c").strip(),
            "achievements": self.achievements_text.get("1.0", "end-1c").strip(),
            "target_role": self.target_role_entry.get().strip(),
            "requirements": self.requirements_text.get("1.0", "end-1c").strip(),
            "industries": self.industries_text.get("1.0", "end-1c").strip()
        }

    def generate_resume_content(self):
        if not self.validate_inputs():
            return
        if not self.gemini_client:
            messagebox.showerror("Error", "AI Assistant is not available. Please check your API key.")
            return

        data = self.collect_profile_data()
        self.loading_dialog = LoadingDialog(self.root, "Crafting resume content...")
        worker = threading.Thread(target=self._generate_resume_thread, args=(data,))
        worker.daemon = True
        worker.start()

    def _generate_resume_thread(self, profile_data):
        try:
            self.loading_dialog.update_status("Analyzing your profile and target role...")
            resume_sections = self.gemini_client.generate_resume_sections(profile_data)
            self.root.after(0, self._show_resume_results, resume_sections)
        except Exception as exc:
            logging.error("Error generating resume content: %s", exc)
            self.root.after(0, self._show_error, f"Error generating resume content: {exc}")

    def _show_resume_results(self, sections):
        if self.loading_dialog:
            self.loading_dialog.close()
        ResultsDialog(self.root, "AI-Generated Resume Content", sections)

    def _show_error(self, error_message):
        if self.loading_dialog:
            self.loading_dialog.close()
        messagebox.showerror("Error", error_message)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.current_role_entry.delete(0, tk.END)
        self.experience_combo.set(Config.DEFAULT_EXPERIENCE_LEVELS[0])
        self.skills_text.delete("1.0", tk.END)
        self.skills_text.insert("1.0", "List your key skills, tools, and technologies separated by commas")
        self.achievements_text.delete("1.0", tk.END)
        self.achievements_text.insert("1.0", "Summarize top achievements, metrics, or noteworthy projects")
        self.industries_text.delete("1.0", tk.END)
        self.industries_text.insert("1.0", "Optional: List industries or company types you are targeting")
        self.target_role_entry.delete(0, tk.END)
        self.requirements_text.delete("1.0", tk.END)
        self.requirements_text.insert("1.0", "Paste key responsibilities or qualifications from a job description")

    def run(self):
        self.root.mainloop()


def main():
    app = ResumeAIAgent()
    app.run()


if __name__ == "__main__":
    main()