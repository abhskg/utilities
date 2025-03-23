"""
Clipboard Access Example with GUI using tkinter

This script provides a graphical interface for:
- Reading the current clipboard content
- Setting new content to the clipboard
- Monitoring clipboard changes
"""

import tkinter as tk
from tkinter import scrolledtext
import time
import threading

class ClipboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Manager")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)
        
        self.monitoring = False
        self.monitor_thread = None
        
        self.setup_gui()
    
    def setup_gui(self):
        # Frame for current clipboard content
        current_frame = tk.LabelFrame(self.root, text="Current Clipboard Content")
        current_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.clipboard_display = scrolledtext.ScrolledText(current_frame, wrap=tk.WORD, height=5)
        self.clipboard_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Refresh button
        refresh_btn = tk.Button(current_frame, text="Refresh", command=self.refresh_clipboard)
        refresh_btn.pack(padx=5, pady=5)
        
        # Frame for setting clipboard content
        set_frame = tk.LabelFrame(self.root, text="Set Clipboard Content")
        set_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.new_content = tk.Entry(set_frame, width=50)
        self.new_content.pack(padx=5, pady=5, fill=tk.X)
        
        set_btn = tk.Button(set_frame, text="Copy to Clipboard", command=self.set_clipboard)
        set_btn.pack(padx=5, pady=5)
        
        # Frame for monitoring
        monitor_frame = tk.LabelFrame(self.root, text="Clipboard Monitor")
        monitor_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.monitor_display = scrolledtext.ScrolledText(monitor_frame, wrap=tk.WORD, height=10)
        self.monitor_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.monitor_btn = tk.Button(monitor_frame, text="Start Monitoring", command=self.toggle_monitoring)
        self.monitor_btn.pack(padx=5, pady=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Initial refresh
        self.refresh_clipboard()
    
    def get_clipboard_text(self):
        """Get text from clipboard using tkinter."""
        try:
            return self.root.clipboard_get()
        except tk.TclError:
            return "No text in clipboard"
    
    def set_clipboard_text(self, text):
        """Set text to clipboard using tkinter."""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()  # Required to finalize clipboard changes
    
    def refresh_clipboard(self):
        """Refresh the clipboard display."""
        clipboard_content = self.get_clipboard_text()
        self.clipboard_display.delete(1.0, tk.END)
        self.clipboard_display.insert(tk.END, clipboard_content)
        self.status_var.set(f"Clipboard content refreshed at {time.strftime('%H:%M:%S')}")
    
    def set_clipboard(self):
        """Set clipboard to the entered text."""
        new_text = self.new_content.get()
        if new_text:
            self.set_clipboard_text(new_text)
            self.refresh_clipboard()
            self.status_var.set(f"Text copied to clipboard at {time.strftime('%H:%M:%S')}")
        else:
            self.status_var.set("Please enter text to copy")
    
    def toggle_monitoring(self):
        """Start or stop clipboard monitoring."""
        if self.monitoring:
            self.monitoring = False
            self.monitor_btn.config(text="Start Monitoring")
            self.status_var.set("Monitoring stopped")
        else:
            self.monitoring = True
            self.monitor_btn.config(text="Stop Monitoring")
            self.status_var.set("Monitoring started")
            
            # Start monitoring in a separate thread
            self.monitor_thread = threading.Thread(target=self.monitor_clipboard)
            self.monitor_thread.daemon = True
            self.monitor_thread.start()
    
    def monitor_clipboard(self):
        """Monitor clipboard changes in a separate thread."""
        last_value = self.get_clipboard_text()
        
        while self.monitoring:
            current_value = self.get_clipboard_text()
            if current_value != last_value:
                timestamp = time.strftime('%H:%M:%S')
                message = f"[{timestamp}] Clipboard changed to: {current_value}\n"
                
                # Update UI in the main thread
                self.root.after(0, self.update_monitor_display, message)
                last_value = current_value
            
            time.sleep(0.5)
    
    def update_monitor_display(self, message):
        """Update the monitor display with new clipboard content."""
        self.monitor_display.insert(tk.END, message)
        self.monitor_display.see(tk.END)  # Auto-scroll to the end

def main():
    root = tk.Tk()
    app = ClipboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()