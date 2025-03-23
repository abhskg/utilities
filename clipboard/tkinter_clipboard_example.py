"""
Clipboard Access Example using tkinter

This script demonstrates how to read from and write to the Windows clipboard
using tkinter, which is included in the Python standard library.

No additional installations required!
"""

import tkinter as tk
import time

def get_clipboard_text(root):
    """Get text from clipboard using tkinter."""
    try:
        return root.clipboard_get()
    except tk.TclError:
        # This happens when clipboard is empty or contains non-text data
        return "No text in clipboard"

def set_clipboard_text(root, text):
    """Set text to clipboard using tkinter."""
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Required to finalize clipboard changes

def main():
    # Create hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    # Get current clipboard content
    clipboard_content = get_clipboard_text(root)
    print(f"Current clipboard content: {clipboard_content}")
    
    # Set new content to clipboard
    new_text = f"This text was copied to clipboard by tkinter at {time.strftime('%H:%M:%S')}"
    set_clipboard_text(root, new_text)
    print(f"Set clipboard to: {new_text}")
    
    # Verify it worked by reading again
    updated_content = get_clipboard_text(root)
    print(f"Updated clipboard content: {updated_content}")
    
    # Example of clipboard monitoring
    print("\nClipboard Monitor Demo:")
    print("Copy some text anywhere (Ctrl+C), and I'll detect it. Press Ctrl+C in terminal to exit.")
    
    last_value = get_clipboard_text(root)
    try:
        while True:
            # Need to call update periodically to keep tkinter app running
            root.update()
            
            current_value = get_clipboard_text(root)
            if current_value != last_value:
                print(f"[{time.strftime('%H:%M:%S')}] Clipboard changed to: {current_value}")
                last_value = current_value
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Monitor stopped")
    finally:
        root.destroy()

if __name__ == "__main__":
    main() 