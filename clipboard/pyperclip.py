"""
Clipboard Access Example using pyperclip

This script demonstrates how to read from and write to the Windows clipboard
using the pyperclip module, which is a simple cross-platform clipboard interface.

Requirements:
- pip install pyperclip
"""

import pyperclip
import time

def main():
    # Get current clipboard content
    clipboard_content = pyperclip.paste()
    print(f"Current clipboard content: {clipboard_content}")
    
    # Set new content to clipboard
    new_text = f"This text was copied to clipboard by Python at {time.strftime('%H:%M:%S')}"
    pyperclip.copy(new_text)
    print(f"Set clipboard to: {new_text}")
    
    # Verify it worked by reading again
    updated_content = pyperclip.paste()
    print(f"Updated clipboard content: {updated_content}")
    
    # Example of clipboard monitoring
    print("\nClipboard Monitor Demo:")
    print("Copy some text anywhere (Ctrl+C), and I'll detect it. Press Ctrl+C in terminal to exit.")
    
    last_value = pyperclip.paste()
    try:
        while True:
            current_value = pyperclip.paste()
            if current_value != last_value:
                print(f"Clipboard changed to: {current_value}")
                last_value = current_value
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Monitor stopped")

if __name__ == "__main__":
    main() 