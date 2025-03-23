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

## Setting Up Aliases

Create aliases to run the scripts more easily:

### Windows

#### PowerShell

Add to your PowerShell profile (`$PROFILE`):

```powershell
function Get-Clipboard-Py { python path\to\pyperclip_example.py }
function Get-Clipboard-Win32 { python path\to\win32clipboard_example.py }
function Get-Clipboard-Tk { python path\to\tkinter_clipboard_example.py }

Set-Alias -Name pyclip -Value Get-Clipboard-Py
Set-Alias -Name win32clip -Value Get-Clipboard-Win32
Set-Alias -Name tkclip -Value Get-Clipboard-Tk
```

#### Command Prompt

Create a batch file (e.g., `clipboard_aliases.bat`):

```batch
@echo off
doskey pyclip=python path\to\pyperclip_example.py $*
doskey win32clip=python path\to\win32clipboard_example.py $*
doskey tkclip=python path\to\tkinter_clipboard_example.py $*
```

Add to registry to run at startup or call the batch file when opening CMD.

### macOS/Linux

Add to your `.bashrc`, `.zshrc`, or equivalent:

```bash
# Clipboard aliases
alias pyclip="python /path/to/pyperclip_example.py"
alias win32clip="python /path/to/win32clipboard_example.py"
alias tkclip="python /path/to/tkinter_clipboard_example.py"
```

After editing, run `source ~/.bashrc` or restart your terminal to apply changes.

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