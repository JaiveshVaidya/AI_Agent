# Resume AI Agent

## Overview
This project provides a Tkinter-based desktop assistant that crafts tailored resume content using the existing Gemini integration. Users can input their profile information and immediately receive AI-generated resume sections aligned with specific job requirements.

## Key Features
- **Generate resume content from user profile** using Google's Gemini API.
- **Graphical desktop experience** leveraging `customtkinter` for a modern look and feel.
- **Configurable prompts** so the assistant can adapt to different role requirements or industries.

## Project Structure
```text
resume_ai_agent/
├── README.md
├── requirements.txt
├── config.py
├── gemini_client.py
├── gui_components.py
└── main_app.py
```

## Getting Started
1. **Install dependencies**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. **Set environment variables** in a `.env` file at the project root:
   ```text
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-1.5-flash
   ```
3. **Run the application**
   ```powershell
   python main_app.py
   ```

## Next Steps
- Add resume section templates (experience, skills, achievements).
- Support exporting generated content to PDF/Word.
- Incorporate job description parsing for advanced tailoring.