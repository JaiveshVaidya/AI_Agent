# Quick Setup Guide 🚀

## Step 1: Get Your Gemini API Key 🔑

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

## Step 2: Configure the Application ⚙️

1. Open the `.env` file in this directory
2. Replace `your_gemini_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. Save the file

## Step 3: Install Dependencies 📦

Open PowerShell/Command Prompt in this directory and run:
```bash
pip install -r requirements.txt
```

## Step 4: Test the Setup ✅

Run the test script to verify everything is working:
```bash
python test_setup.py
```

## Step 5: Launch the Application 🎯

Run the main application:
```bash
python main_app.py
```

Or double-click the `run_app.bat` file.

## Troubleshooting 🔧

### "AI Assistant Error - Check API Key"
- Verify your API key is correctly set in the `.env` file
- Make sure you have internet connectivity
- Check if your API key has proper permissions

### Import Errors
- Run: `pip install -r requirements.txt`
- Make sure you're using Python 3.8 or higher

### GUI Issues
- Update your display drivers
- Try running with different scaling settings

## Features Overview 🌟

### Main Features:
- **Job Search Strategy**: Get comprehensive, AI-powered job search recommendations
- **Market Trend Analysis**: Understand current job market trends for your field
- **Resume Optimization**: Receive personalized resume improvement tips
- **Modern GUI**: Clean, professional interface with dark theme

### Input Parameters:
1. **Job Title**: The position you're targeting
2. **Experience Level**: Your professional experience level
3. **Skills**: Your technical and professional skills
4. **Expected Salary**: Your salary expectations

### Quick Actions:
- 📈 Analyze Market Trends
- 📄 Get Resume Tips
- 🗑️ Clear Form

## Usage Tips 💡

1. **Be Specific**: Use specific job titles for better results
2. **List Skills Clearly**: Include both technical and soft skills
3. **Consider Market Rates**: Research salary ranges for your area
4. **Update Regularly**: Keep your LinkedIn and resume updated
5. **Network Actively**: Connect with professionals in your field
6. **Customize Applications**: Tailor each application to the specific role

## Support 💬

If you encounter any issues:
1. Check this setup guide
2. Run the test script: `python test_setup.py`
3. Verify your API key configuration
4. Ensure all dependencies are installed

---

**Happy Job Hunting! 🎯**

*Your AI-powered career assistant is ready to help you find your dream job!*