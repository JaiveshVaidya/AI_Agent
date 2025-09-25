import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import customtkinter as ctk
from config import Config

# Set CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ModernButton(ctk.CTkButton):
    """Custom modern button component"""
    
    def __init__(self, parent, text, command=None, **kwargs):
        # Set default values if not provided
        if 'height' not in kwargs:
            kwargs['height'] = 40
        if 'corner_radius' not in kwargs:
            kwargs['corner_radius'] = 8
        if 'font' not in kwargs:
            kwargs['font'] = ctk.CTkFont(size=14, weight="bold")
            
        super().__init__(
            parent,
            text=text,
            command=command,
            **kwargs
        )

class ModernEntry(ctk.CTkEntry):
    """Custom modern entry component"""
    
    def __init__(self, parent, placeholder_text="", **kwargs):
        # Set default values if not provided
        if 'height' not in kwargs:
            kwargs['height'] = 35
        if 'corner_radius' not in kwargs:
            kwargs['corner_radius'] = 6
        if 'font' not in kwargs:
            kwargs['font'] = ctk.CTkFont(size=12)
            
        super().__init__(
            parent,
            placeholder_text=placeholder_text,
            **kwargs
        )

class ModernComboBox(ctk.CTkComboBox):
    """Custom modern combobox component"""
    
    def __init__(self, parent, values, **kwargs):
        # Set default values if not provided
        if 'height' not in kwargs:
            kwargs['height'] = 35
        if 'corner_radius' not in kwargs:
            kwargs['corner_radius'] = 6
        if 'font' not in kwargs:
            kwargs['font'] = ctk.CTkFont(size=12)
            
        super().__init__(
            parent,
            values=values,
            **kwargs
        )

class ModernTextArea(ctk.CTkTextbox):
    """Custom modern text area component"""
    
    def __init__(self, parent, **kwargs):
        # Set default values if not provided
        if 'corner_radius' not in kwargs:
            kwargs['corner_radius'] = 6
        if 'font' not in kwargs:
            kwargs['font'] = ctk.CTkFont(size=11)
            
        super().__init__(
            parent,
            **kwargs
        )

class ModernLabel(ctk.CTkLabel):
    """Custom modern label component"""
    
    def __init__(self, parent, text, size=12, weight="normal", **kwargs):
        super().__init__(
            parent,
            text=text,
            font=ctk.CTkFont(size=size, weight=weight),
            **kwargs
        )

class ModernFrame(ctk.CTkFrame):
    """Custom modern frame component"""
    
    def __init__(self, parent, **kwargs):
        # Set default values if not provided
        if 'corner_radius' not in kwargs:
            kwargs['corner_radius'] = 10
            
        super().__init__(
            parent,
            **kwargs
        )

class LoadingDialog:
    """Modern loading dialog"""
    
    def __init__(self, parent, title="Processing..."):
        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("300x150")
        self.dialog.resizable(False, False)
        
        # Center the dialog
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Create loading content
        self.create_loading_content()
        
        # Center on parent
        self.center_on_parent(parent)
    
    def create_loading_content(self):
        """Create the loading dialog content"""
        main_frame = ModernFrame(self.dialog)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Loading label
        loading_label = ModernLabel(
            main_frame, 
            text="🤖 AI is thinking...", 
            size=14, 
            weight="bold"
        )
        loading_label.pack(pady=(10, 5))
        
        # Progress bar
        self.progress = ctk.CTkProgressBar(main_frame)
        self.progress.pack(pady=10, padx=20, fill="x")
        self.progress.configure(mode="indeterminate")
        self.progress.start()
        
        # Status label
        self.status_label = ModernLabel(
            main_frame, 
            text="Please wait while we generate your job search strategy...", 
            size=10
        )
        self.status_label.pack(pady=5)
    
    def center_on_parent(self, parent):
        """Center the dialog on the parent window"""
        self.dialog.update_idletasks()
        
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        dialog_width = self.dialog.winfo_width()
        dialog_height = self.dialog.winfo_height()
        
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2
        
        self.dialog.geometry(f"+{x}+{y}")
    
    def update_status(self, status_text):
        """Update the status text"""
        self.status_label.configure(text=status_text)
        self.dialog.update()
    
    def close(self):
        """Close the loading dialog"""
        self.progress.stop()
        self.dialog.destroy()

class ResultsDialog:
    """Modern results display dialog"""
    
    def __init__(self, parent, title, content):
        self.dialog = ctk.CTkToplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("900x700")
        
        # Make it resizable
        self.dialog.resizable(True, True)
        
        # Center the dialog
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Create content
        self.create_content(content)
        
        # Center on parent
        self.center_on_parent(parent)
    
    def create_content(self, content):
        """Create the results dialog content"""
        main_frame = ModernFrame(self.dialog)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ModernLabel(
            main_frame, 
            text="🎯 Your Personalized Job Search Strategy", 
            size=16, 
            weight="bold"
        )
        title_label.pack(pady=(10, 20))
        
        # Results text area
        self.results_text = ModernTextArea(main_frame, height=400)
        self.results_text.pack(fill="both", expand=True, pady=(0, 20))
        
        # Insert content
        self.results_text.insert("1.0", content)
        
        # Button frame
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))
        
        # Copy button
        copy_btn = ModernButton(
            button_frame,
            text="📋 Copy to Clipboard",
            command=self.copy_to_clipboard,
            width=150
        )
        copy_btn.pack(side="left", padx=(0, 10))
        
        # Close button
        close_btn = ModernButton(
            button_frame,
            text="✅ Close",
            command=self.dialog.destroy,
            width=100
        )
        close_btn.pack(side="right")
    
    def copy_to_clipboard(self):
        """Copy results to clipboard"""
        content = self.results_text.get("1.0", "end-1c")
        self.dialog.clipboard_clear()
        self.dialog.clipboard_append(content)
        messagebox.showinfo("Success", "Results copied to clipboard!")
    
    def center_on_parent(self, parent):
        """Center the dialog on the parent window"""
        self.dialog.update_idletasks()
        
        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        dialog_width = self.dialog.winfo_width()
        dialog_height = self.dialog.winfo_height()
        
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2
        
        self.dialog.geometry(f"+{x}+{y}")