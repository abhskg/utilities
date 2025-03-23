"""
Clipboard Access Example with GUI using tkinter

This script provides a graphical interface for:
- Viewing the last 10 clipboard items
- Setting any historical item as the current clipboard content
- Monitoring clipboard changes
"""

import tkinter as tk
from tkinter import scrolledtext
import time
import threading
from collections import deque

class ClipboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Manager")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)
        
        self.monitoring = False
        self.monitor_thread = None
        self.clipboard_history = deque(maxlen=10)  # Store last 10 clipboard items
        self.history_frames = []  # To track the frames displaying history items
        
        self.setup_gui()
    
    def setup_gui(self):
        # Frame for clipboard history
        history_frame = tk.LabelFrame(self.root, text="Clipboard History (Last 10 Items)")
        history_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Container for history items
        self.history_container = tk.Frame(history_frame)
        self.history_container.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Add a scrollbar to the history container
        history_canvas = tk.Canvas(self.history_container)
        scrollbar = tk.Scrollbar(self.history_container, orient="vertical", command=history_canvas.yview)
        self.scrollable_frame = tk.Frame(history_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: history_canvas.configure(scrollregion=history_canvas.bbox("all"))
        )
        
        history_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        history_canvas.configure(yscrollcommand=scrollbar.set)
        
        history_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Refresh button
        refresh_btn = tk.Button(history_frame, text="Refresh", command=self.refresh_clipboard)
        refresh_btn.pack(padx=5, pady=5)
        
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
        """Refresh the clipboard display and update history."""
        clipboard_content = self.get_clipboard_text()
        
        # Only add to history if it's different from the most recent item
        if not self.clipboard_history or clipboard_content != self.clipboard_history[0]:
            self.clipboard_history.appendleft(clipboard_content)
            self.update_history_display()
        
        self.status_var.set(f"Clipboard content refreshed at {time.strftime('%H:%M:%S')}")
    
    def update_history_display(self):
        """Update the history display with current clipboard history."""
        # Clear existing history frames
        for frame in self.history_frames:
            frame.destroy()
        self.history_frames = []
        
        # Create a new frame for each history item
        for i, content in enumerate(self.clipboard_history):
            item_frame = tk.Frame(self.scrollable_frame)
            item_frame.pack(fill=tk.X, padx=5, pady=2)
            self.history_frames.append(item_frame)
            
            # Truncate long content for display
            display_content = content if len(content) < 50 else content[:47] + "..."
            
            # Label to show the clipboard content
            label = tk.Label(item_frame, text=display_content, anchor="w", justify=tk.LEFT)
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Button to set this item as the current clipboard
            use_btn = tk.Button(
                item_frame, 
                text="Use", 
                command=lambda c=content: self.use_history_item(c)
            )
            use_btn.pack(side=tk.RIGHT)
    
    def use_history_item(self, content):
        """Set a history item as the current clipboard content."""
        self.set_clipboard_text(content)
        self.status_var.set(f"Clipboard set to selected item at {time.strftime('%H:%M:%S')}")
    
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
                self.root.after(0, self.refresh_clipboard)  # Also update the history
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