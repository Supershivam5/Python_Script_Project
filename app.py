import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog
from pathlib import Path

class ModernFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            bg="#1e1e1e",  # Dark background
            highlightbackground="#2d2d2d",  # Darker border
            highlightthickness=1,
            relief="flat",
            padx=15,
            pady=15
        )

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Note Taking App")
        
        # Initialize theme
        self.is_dark_theme = True
        
        # Load Dosis font
        self.custom_font = ("Dosis", 12)
        self.title_font = ("Dosis", 12, "bold")
        
        # Set modern styling
        self.style = ttk.Style()
        self.style.configure(
            "Modern.TButton",
            padding=10,
            relief="flat",
            background="#2d2d2d",
            foreground="#ffffff",
            borderwidth=0,
            font=self.custom_font
        )
        
        self.note_counter = 1
        self.current_note_file = f"note_{self.note_counter}.txt"
        
        # Create UI elements
        self.create_ui()
        
        # Now set the theme after UI elements are created
        self.set_theme()

    def create_ui(self):
        # Create main container with rounded corners
        self.container = ModernFrame(self.root, padx=20, pady=20)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create horizontal split container
        self.split_container = tk.PanedWindow(
            self.container,
            orient=tk.HORIZONTAL,
            bg="#1e1e1e",
            sashwidth=4,
            sashrelief="flat", 
            borderwidth=0
        )
        self.split_container.pack(fill=tk.BOTH, expand=True)
        
        # Create frames with rounded corners
        self.active_frame = ModernFrame(self.split_container)
        self.pinned_frame = ModernFrame(self.split_container)
        
        # Initially only add the active frame
        self.split_container.add(self.active_frame, width=800)  # Full width initially
        
        # Create labels and text areas
        self.create_note_areas()
        
        # Create buttons
        self.create_buttons()

    def create_note_areas(self):
        # Active note label
        self.active_label = tk.Label(
            self.active_frame,
            text="Active Note",
            font=self.title_font,
            bg="#1e1e1e",
            fg="#ffffff"
        )
        self.active_label.pack(pady=(0, 10))
        
        # Active text area
        self.text_area = tk.Text(
            self.active_frame,
            height=15,
            width=40,
            bg="#2d2d2d",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
            font=self.custom_font,
            padx=10,
            pady=10
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Pinned note label
        self.pinned_label = tk.Label(
            self.pinned_frame,
            text="Pinned Notes",
            font=self.title_font,
            bg="#1e1e1e",
            fg="#ffffff"
        )
        self.pinned_label.pack(pady=(0, 10))
        
        # Pinned text area
        self.pinned_text = tk.Text(
            self.pinned_frame,
            height=15,
            width=40,
            bg="#2d2d2d",
            fg="#ffffff",
            relief="flat",
            font=self.custom_font,
            padx=10,
            pady=10,
            state='disabled'
        )
        self.pinned_text.pack(fill=tk.BOTH, expand=True)

    def set_theme(self):
        if self.is_dark_theme:
            bg_color = "#1e1e1e"
            text_color = "#ffffff"
            text_bg = "#2d2d2d"
            button_frame_bg = "#2d2d2d"
            
            # Button colors for dark theme
            self.save_button.configure(bg="#90EE90", fg="#000000")
            self.open_button.configure(bg="#FFA500", fg="#000000")
            self.pin_button.configure(bg="#ADD8E6", fg="#000000")
            self.delete_button.configure(bg="#FF6B6B", fg="#ffffff")
            self.theme_button.configure(bg="#2d2d2d", fg="#ffffff", text="Dark Theme")
            
        else:
            bg_color = "#ffffff"
            text_color = "#000000"
            text_bg = "#f0f0f0"
            button_frame_bg = "#f0f0f0"
            
            # Button colors for light theme
            self.save_button.configure(bg="#98FB98", fg="#000000")  # Lighter green
            self.open_button.configure(bg="#FFB84D", fg="#000000")  # Lighter orange
            self.pin_button.configure(bg="#B0E0E6", fg="#000000")  # Lighter blue
            self.delete_button.configure(bg="#FFB6B6", fg="#000000")  # Lighter red
            self.theme_button.configure(bg="#f0f0f0", fg="#000000", text="Light Theme")
        
        # Configure frame backgrounds
        self.root.configure(bg=bg_color)
        self.container.configure(bg=bg_color)
        self.split_container.configure(bg=bg_color)
        self.active_frame.configure(bg=bg_color)
        self.pinned_frame.configure(bg=bg_color)
        self.button_frame.configure(bg=button_frame_bg)  # Update button frame background
        
        # Configure text elements
        self.active_label.configure(bg=bg_color, fg=text_color)
        self.pinned_label.configure(bg=bg_color, fg=text_color)
        self.text_area.configure(bg=text_bg, fg=text_color, insertbackground=text_color)
        self.pinned_text.configure(bg=text_bg, fg=text_color)

    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.set_theme()
        # Update theme button text
        self.theme_button.configure(
            text="Dark Theme" if self.is_dark_theme else "Light Theme"
        )
    
    def pin_note(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "Cannot pin empty note!")
            return
            
        # Add pinned frame if it's not already visible
        if len(self.split_container.panes()) == 1:
            self.split_container.add(self.pinned_frame, width=400)
            # Adjust active frame width
            self.split_container.paneconfig(self.active_frame, width=400)
            
        self.pinned_text.configure(state='normal')
        self.pinned_text.delete("1.0", tk.END)
        self.pinned_text.insert("1.0", self.text_area.get("1.0", tk.END))
        self.pinned_text.configure(state='disabled')
        
        self.delete_button.configure(state='normal')
        self.text_area.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Note pinned successfully!")
    
    def save_note(self):
        note_content = self.text_area.get("1.0", tk.END).strip()
        if not note_content:
            messagebox.showwarning("Warning", "Cannot save empty note!")
            return
            
        try:
            with open(self.current_note_file, "w", encoding='utf-8') as f:
                f.write(note_content)
            messagebox.showinfo("Success", f"Note saved successfully as {self.current_note_file}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save note: {str(e)}")
    
    def clear_note(self):
        self.text_area.delete("1.0", tk.END)
    
    def load_notes(self):
        # Show file selection dialog
        file_path = filedialog.askopenfilename(
            title="Open Note",
            filetypes=[("Text files", "*.txt")],
            initialdir="."
        )
        
        if file_path:
            try:
                with open(file_path, "r", encoding='utf-8') as f:
                    content = f.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert("1.0", content)
                    messagebox.showinfo("Success", f"Note loaded successfully from {file_path}!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load note: {str(e)}")
    
    def show_active_note_frame(self):
        self.pinned_frame.pack_forget()
        self.active_frame.pack(fill=tk.BOTH, expand=True)
    
    def show_pinned_note_frame(self):
        self.active_frame.pack_forget()
        self.pinned_frame.pack(fill=tk.BOTH, expand=True)
    
    def on_hover(self, event, button, color):
        if button['state'] != 'disabled':
            button.configure(bg=color)

    def on_leave(self, event, button, color):
        if button['state'] != 'disabled':
            button.configure(bg=color)

    def delete_pinned_note(self):
        self.pinned_text.configure(state='normal')
        self.pinned_text.delete("1.0", tk.END)
        self.pinned_text.configure(state='disabled')
        self.delete_button.configure(state='disabled')
        
        # Remove pinned frame and adjust active frame width
        self.split_container.remove(self.pinned_frame)
        self.split_container.paneconfig(self.active_frame, width=800)
        
        # Increment counter for next note
        self.note_counter += 1
        self.current_note_file = f"note_{self.note_counter}.txt"
        messagebox.showinfo("Success", "Pinned note deleted successfully!")

    def create_buttons(self):
        # Create button frame
        self.button_frame = ModernFrame(self.container) 
        # Make it instance variable
        self.button_frame.pack(fill=tk.X, pady=(10, 0))

        # Save button (light green)
        self.save_button = tk.Button(
            self.button_frame,
            text="Save",
            command=self.save_note,
            relief="flat",
            font=self.custom_font,
            padx=15,
            pady=5
        )
        self.save_button.pack(side=tk.LEFT, padx=5)

        # Open saved notes button (orange)
        self.open_button = tk.Button(
            self.button_frame,
            text="Open Notes",
            command=self.load_notes,
            relief="flat",
            font=self.custom_font,
            padx=15,
            pady=5
        )
        self.open_button.pack(side=tk.LEFT, padx=5)

        # Pin button (light blue)
        self.pin_button = tk.Button(
            self.button_frame,
            text="Pin Note",
            command=self.pin_note,
            relief="flat",
            font=self.custom_font,
            padx=15,
            pady=5
        )
        self.pin_button.pack(side=tk.LEFT, padx=5)

        # Delete button (red)
        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete",
            command=self.delete_pinned_note,
            relief="flat",
            font=self.custom_font,
            padx=15,
            pady=5,
            state='disabled'
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Theme toggle button
        self.theme_button = tk.Button(
            self.button_frame,
            text="Dark Theme",
            command=self.toggle_theme,
            relief="flat",
            font=self.custom_font,
            padx=15,
            pady=5
        )
        self.theme_button.pack(side=tk.RIGHT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = NoteTakingApp(root)
    root.mainloop()
