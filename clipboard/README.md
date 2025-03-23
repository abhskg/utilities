# Python Clipboard Access Examples

This repository contains examples of how to access the Windows clipboard using different Python libraries.

## Scripts

1. **pyperclip_example.py**: Uses the `pyperclip` library (cross-platform, simple API)
2. **win32clipboard_example.py**: Uses the `win32clipboard` module from `pywin32` (Windows-specific, more powerful)
3. **tkinter_clipboard_example.py**: Uses the built-in `tkinter` library (no additional installations)

## Requirements

- Python 3.6+
- For `pyperclip_example.py`: `pip install pyperclip`
- For `win32clipboard_example.py`: `pip install pywin32`
- For `tkinter_clipboard_example.py`: No additional installations required

## Usage

Each script demonstrates:
- Reading text from the clipboard
- Writing text to the clipboard
- A simple clipboard monitor that detects changes

Run any script with:

```
python script_name.py
```

## Features Comparison

| Feature | pyperclip | win32clipboard | tkinter |
|---------|-----------|---------------|---------|
| Installation | Simple pip install | Larger package | Built-in |
| Platform | Cross-platform | Windows only | Cross-platform |
| Text handling | Simple | Advanced | Simple |
| Non-text formats | No | Yes | Limited |
| API Complexity | Low | Medium | Low |

## Which one to use?

- **pyperclip**: Best for simple cross-platform clipboard text operations
- **win32clipboard**: Best for Windows-specific applications or when you need advanced clipboard format handling
- **tkinter**: Best when you already use tkinter in your application or want to avoid additional dependencies 