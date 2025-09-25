#!/usr/bin/env python3
"""
Test script to verify the Job Search AI setup
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import tkinter as tk
        print("✅ tkinter - OK")
    except ImportError as e:
        print(f"❌ tkinter - FAILED: {e}")
        return False
    
    try:
        import customtkinter as ctk
        print("✅ customtkinter - OK")
    except ImportError as e:
        print(f"❌ customtkinter - FAILED: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai - OK")
    except ImportError as e:
        print(f"❌ google.generativeai - FAILED: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv - OK")
    except ImportError as e:
        print(f"❌ python-dotenv - FAILED: {e}")
        return False
    
    try:
        import requests
        print("✅ requests - OK")
    except ImportError as e:
        print(f"❌ requests - FAILED: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow - OK")
    except ImportError as e:
        print(f"❌ Pillow - FAILED: {e}")
        return False
    
    return True

def test_config():
    """Test if configuration loads properly"""
    print("\nTesting configuration...")
    
    try:
        from config import Config
        print("✅ Config module - OK")
        
        # Test some config values
        print(f"   App Title: {Config.APP_TITLE}")
        print(f"   Window Size: {Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}")
        print(f"   Gemini Model: {Config.GEMINI_MODEL}")
        
        return True
    except Exception as e:
        print(f"❌ Config - FAILED: {e}")
        return False

def test_env_file():
    """Test if .env file exists"""
    print("\nTesting environment file...")
    
    env_path = ".env"
    if os.path.exists(env_path):
        print("✅ .env file exists")
        
        # Check if API key is set (but don't show it)
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key and api_key != 'your_gemini_api_key_here':
            print("✅ Gemini API key is configured")
        else:
            print("⚠️  Gemini API key needs to be set in .env file")
        
        return True
    else:
        print("❌ .env file not found")
        return False

def test_gui_components():
    """Test if GUI components can be imported"""
    print("\nTesting GUI components...")
    
    try:
        from gui_components import (
            ModernButton, ModernEntry, ModernComboBox, 
            ModernTextArea, ModernLabel, ModernFrame
        )
        print("✅ GUI components - OK")
        return True
    except Exception as e:
        print(f"❌ GUI components - FAILED: {e}")
        return False

def main():
    """Run all tests"""
    print("🤖 Job Search AI - Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_config,
        test_env_file,
        test_gui_components
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the application:")
        print("1. Set your Gemini API key in the .env file")
        print("2. Run: python main_app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())