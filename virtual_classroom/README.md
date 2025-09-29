# Virtual Classroom Platform

## Overview
The **Virtual Classroom** project delivers a web-based learning experience focused on mathematics instruction. It combines live video sessions (powered by a third-party provider such as Twilio or Zoom) with an interactive whiteboard that supports drawing equations, annotating problem statements, and sharing lesson content in real time.

## High-Level Architecture
```text
virtual_classroom/
├── README.md
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── App.jsx
        ├── main.jsx
        ├── config.js
        ├── styles.css
        └── components/
            ├── VideoRoom.jsx
            ├── Whiteboard.jsx
            └── MathLessonPanel.jsx
```

- **Frontend (React + Vite)**: Handles the classroom UI, including the embedded video area and collaborative math whiteboard.
- **Backend (FastAPI)**: Exposes secure endpoints for generating video access tokens and can later be extended for user/session management.
- **Third-Party Video SDK**: Designed to integrate with providers such as Twilio Video. The current implementation includes a token endpoint and client scaffolding.

## Getting Started

### 1. Backend Setup
1. Navigate to the backend folder:
   ```powershell
   Set-Location "c:\Users\jaive\Documents\GitHub\AI_Agent\virtual_classroom\backend"
   ```
2. Create and activate a virtual environment, then install dependencies:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in the Twilio credentials:
   ```text
   TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   TWILIO_API_KEY=SKXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   TWILIO_API_SECRET=your_api_secret
   TWILIO_ROOM_NAME=math_classroom
   ```
4. Run the FastAPI server:
   ```powershell
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

### 2. Frontend Setup
1. Navigate to the frontend folder:
   ```powershell
   Set-Location "c:\Users\jaive\Documents\GitHub\AI_Agent\virtual_classroom\frontend"
   ```
2. Install dependencies:
   ```powershell
   npm install
   ```
3. Start the development server:
   ```powershell
   npm run dev
   ```
4. Open the provided local URL (e.g., `http://localhost:5173`) to access the classroom interface.

## Key Features
- **Live Video Classroom**: Connects instructors and students via Twilio Video (token provisioning is implemented server-side).
- **Interactive Math Whiteboard**: Built using `react-canvas-draw`, supporting pen tools, colors, undo/redo, and export.
- **Lesson Panel**: Offers quick access to math topics, problem statements, and suggested exercises to guide the session.

## Next Steps & Enhancements
- **Authentication & Roles**: Add login/signup flows with teacher/student permissions.
- **Real-Time Collaboration**: Sync the whiteboard canvas and lesson notes across participants via WebSockets.
- **Class Management**: Track attendance, assignments, and session history.
- **Recording & Playback**: Integrate session recording for asynchronous review.
- **Homework Modules**: Embed quizzes or formative assessments tailored to the math curriculum.

Feel free to build on this scaffold to meet your platform requirements. Let me know if you’d like help extending any portion of the system! :rocket: