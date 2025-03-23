"""
Clipboard Access Example using win32clipboard

This script demonstrates how to read from and write to the Windows clipboard
using the win32clipboard module from pywin32, which provides direct Windows API access.

Requirements:
- pip install pywin32
"""

import win32clipboard
import win32con
import time

def get_clipboard_text():
    """Get text from clipboard."""
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            data = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
            return data
        elif win32clipboard.IsClipboardFormatAvailable(win32con.CF_TEXT):
            data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
            return data.decode('utf-8')
        else:
            return "No text in clipboard"
    finally:
        win32clipboard.CloseClipboard()

def set_clipboard_text(text):
    """Set text to clipboard."""
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text, win32con.CF_UNICODETEXT)
    finally:
        win32clipboard.CloseClipboard()

def get_clipboard_format():
    """Get information about current clipboard format."""
    win32clipboard.OpenClipboard()
    try:
        formats = []
        
        # Check common formats
        format_pairs = [
            (win32con.CF_TEXT, "CF_TEXT (Text)"),
            (win32con.CF_UNICODETEXT, "CF_UNICODETEXT (Unicode Text)"),
            (win32con.CF_BITMAP, "CF_BITMAP (Bitmap)"),
            (win32con.CF_METAFILEPICT, "CF_METAFILEPICT (Metafile)"),
            (win32con.CF_DIB, "CF_DIB (Device Independent Bitmap)"),
            (win32con.CF_HDROP, "CF_HDROP (File List)"),
        ]
        
        for format_id, format_name in format_pairs:
            if win32clipboard.IsClipboardFormatAvailable(format_id):
                formats.append(format_name)
                
        return formats if formats else ["No recognized format"]
    finally:
        win32clipboard.CloseClipboard()

def main():
    # Get current clipboard content
    clipboard_content = get_clipboard_text()
    print(f"Current clipboard content: {clipboard_content}")
    
    # Check clipboard format
    formats = get_clipboard_format()
    print(f"Current clipboard formats: {', '.join(formats)}")
    
    # Set new content to clipboard
    new_text = f"This text was copied to clipboard by win32clipboard at {time.strftime('%H:%M:%S')}"
    set_clipboard_text(new_text)
    print(f"Set clipboard to: {new_text}")
    
    # Verify it worked by reading again
    updated_content = get_clipboard_text()
    print(f"Updated clipboard content: {updated_content}")
    
    # Example of clipboard monitoring
    print("\nClipboard Monitor Demo:")
    print("Copy some text anywhere (Ctrl+C), and I'll detect it. Press Ctrl+C in terminal to exit.")
    
    last_value = get_clipboard_text()
    try:
        while True:
            current_value = get_clipboard_text()
            if current_value != last_value:
                print(f"Clipboard changed to: {current_value}")
                print(f"Format: {', '.join(get_clipboard_format())}")
                last_value = current_value
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Monitor stopped")

if __name__ == "__main__":
    main() 