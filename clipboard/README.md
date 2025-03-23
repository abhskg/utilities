# Python Clipboard Access Examples

This repository contains examples of how to access and manage the clipboard using different Python libraries.

## Scripts

1. **pyperclip.py**: Uses the `pyperclip` library (cross-platform, simple API)
2. **win32clipboard.py**: Uses the `win32clipboard` module from `pywin32` (Windows-specific, more powerful)
3. **tkinter_clipboard.py**: Uses the built-in `tkinter` library (no additional installations)
4. **tkinter_clibboard_gui.py**: A complete GUI clipboard manager with history and monitoring capabilities

## Requirements

- Python 3.6+
- For `pyperclip.py`: `pip install pyperclip`
- For `win32clipboard.py`: `pip install pywin32`
- For `tkinter_clipboard.py` and `tkinter_clibboard_gui.py`: No additional installations required (uses built-in tkinter)

## Usage

Each script demonstrates different clipboard management capabilities:

### Basic Scripts
- Reading text from the clipboard
- Writing text to the clipboard
- Simple clipboard monitoring

Run any script with:
```
python script_name.py
```

### GUI Clipboard Manager
The `tkinter_clibboard_gui.py` script provides a complete clipboard management solution with:
- Visual interface to view clipboard content
- Clipboard history (stores last 10 clipboard items)
- Ability to select any history item and set it as the current clipboard content
- Real-time clipboard monitoring that detects and logs changes
- Status updates with timestamps

Run the GUI manager with:
```
python tkinter_clibboard_gui.py
```

## Setting Up Aliases

Create aliases to run the scripts more easily:

### Windows

#### PowerShell

Add to your PowerShell profile (`$PROFILE`):

```powershell
function Get-Clipboard-Py { python path\to\pyperclip.py }
function Get-Clipboard-Win32 { python path\to\win32clipboard.py }
function Get-Clipboard-Tk { python path\to\tkinter_clipboard.py }
function Launch-Clipboard-Manager { python path\to\tkinter_clibboard_gui.py }

Set-Alias -Name pyclip -Value Get-Clipboard-Py
Set-Alias -Name win32clip -Value Get-Clipboard-Win32
Set-Alias -Name tkclip -Value Get-Clipboard-Tk
Set-Alias -Name clipmanager -Value Launch-Clipboard-Manager
```

#### Command Prompt

Create a batch file (e.g., `clipboard_aliases.bat`):

```batch
@echo off
doskey pyclip=python path\to\pyperclip.py $*
doskey win32clip=python path\to\win32clipboard.py $*
doskey tkclip=python path\to\tkinter_clipboard.py $*
doskey clipmanager=python path\to\tkinter_clibboard_gui.py $*
```

Add to registry to run at startup or call the batch file when opening CMD.

### macOS/Linux

Add to your `.bashrc`, `.zshrc`, or equivalent:

```bash
# Clipboard aliases
alias pyclip="python /path/to/pyperclip.py"
alias win32clip="python /path/to/win32clipboard.py"
alias tkclip="python /path/to/tkinter_clipboard.py"
alias clipmanager="python /path/to/tkinter_clibboard_gui.py"
```

After editing, run `source ~/.bashrc` or restart your terminal to apply changes.

## Features Comparison

| Feature | pyperclip | win32clipboard | tkinter | GUI Clipboard Manager |
|---------|-----------|---------------|---------|----------------------|
| Installation | Simple pip install | Larger package | Built-in | Built-in |
| Platform | Cross-platform | Windows only | Cross-platform | Cross-platform |
| Text handling | Simple | Advanced | Simple | Advanced |
| Non-text formats | No | Yes | Limited | Limited to text |
| API Complexity | Low | Medium | Low | N/A (GUI based) |
| Clipboard History | No | No | No | Yes (10 items) |
| Visual Interface | No | No | No | Yes |
| Monitoring | No | No | No | Yes |

## Which one to use?

- **pyperclip**: Best for simple cross-platform clipboard text operations
- **win32clipboard**: Best for Windows-specific applications or when you need advanced clipboard format handling
- **tkinter_clipboard**: Best when you already use tkinter in your application or want to avoid additional dependencies
- **tkinter_clibboard_gui**: Best for a complete clipboard management solution with history and monitoring features 