# Job Search AI Assistant 🤖

A modern, AI-powered job search assistant built with Python and Google's Gemini AI Flash model. This application provides personalized job search strategies, market trend analysis, and resume optimization tips through an intuitive GUI.

## Features ✨

- **AI-Powered Job Search Strategy**: Get comprehensive, personalized job search recommendations
- **Market Trend Analysis**: Understand current job market trends for your field
- **Resume Optimization Tips**: Receive tailored advice to improve your resume
- **Modern GUI**: Clean, dark-themed interface built with CustomTkinter
- **Real-time AI Processing**: Powered by Google's Gemini AI Flash model

## Parameters 📋

The application allows you to input the following job search parameters:

1. **Job Title**: Target position you're seeking
2. **Experience Level**: Your professional experience level
3. **Skills**: Your technical and professional skills
4. **Expected Salary**: Your salary expectations

## Installation 🚀

1. **Clone or download the project**:
   ```bash
   cd job_search_ai
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Open the `.env` file
   - Replace `your_gemini_api_key_here` with your actual API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Usage 💼

1. **Run the application**:
   ```bash
   python main_app.py
   ```

2. **Fill in your job search parameters**:
   - Enter your target job title
   - Select your experience level
   - List your relevant skills
   - Choose your expected salary range

3. **Generate your strategy**:
   - Click "Generate Job Search Strategy" for comprehensive recommendations
   - Use "Analyze Market Trends" for current market insights
   - Click "Get Resume Tips" for personalized resume advice

## Features in Detail 🔍

### Job Search Strategy Generation
- Optimized keywords for job searches
- Recommended job boards and platforms
- Skills gap analysis
- Salary insights and market data
- Application strategies and tips
- Networking opportunities
- Company type recommendations
- Realistic timeline expectations

### Market Trend Analysis
- Current demand analysis
- Growth trends in your field
- Emerging skills identification
- Remote work opportunities
- Geographic job hotspots
- Industry trend insights

### Resume Optimization
- Best resume structure recommendations
- Key sections to include
- Skills presentation strategies
- Experience description tips
- ATS-friendly keywords
- Common mistakes to avoid

## Technical Stack 🛠️

- **Python 3.8+**
- **Google Generative AI (Gemini Flash)**
- **CustomTkinter** - Modern GUI framework
- **Tkinter** - Base GUI library
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing
- **Requests** - HTTP library

## Project Structure 📁

```
job_search_ai/
├── main_app.py          # Main application file
├── config.py            # Configuration settings
├── gemini_client.py     # Gemini AI client
├── gui_components.py    # Custom GUI components
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md           # This file
```

## Configuration ⚙️

The application can be customized through the `config.py` file:

- **Window dimensions and appearance**
- **Color themes and styling**
- **Default experience levels**
- **Salary ranges**
- **Gemini AI model settings**

## API Key Setup 🔑

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and paste it in your `.env` file
5. Keep your API key secure and never share it publicly

## Troubleshooting 🔧

### Common Issues:

1. **"AI Assistant Error - Check API Key"**:
   - Verify your API key is correctly set in the `.env` file
   - Ensure you have internet connectivity
   - Check if your API key has proper permissions

2. **Import errors**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're using Python 3.8 or higher

3. **GUI display issues**:
   - Update your display drivers
   - Try running with different scaling settings

## Contributing 🤝

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License 📄

This project is open source and available under the MIT License.

## Support 💬

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the error messages in the console
3. Ensure your API key is properly configured
4. Verify all dependencies are installed correctly

---

**Happy Job Hunting! 🎯**

*Powered by Google Gemini AI Flash Model*