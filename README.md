# System Utilities Collection

A comprehensive collection of cross-platform system utilities built with Python to enhance productivity and automate common tasks.

## Current Utilities

### Clipboard Utilities
Tools for accessing and manipulating clipboard content across different operating systems:

- **PyPerClip**: Simple cross-platform clipboard access
- **Win32Clipboard**: Advanced Windows clipboard manipulation
- **Tkinter Clipboard**: Framework-based clipboard operations
- **Clipboard GUI Manager**: Full-featured clipboard management application with:
  - Clipboard history (last 10 items)
  - Content monitoring with timestamps
  - One-click clipboard restoration from history

*See the [clipboard documentation](clipboard/README.md) for detailed information.*

## Features Overview

### Clipboard Manager GUI
![Clipboard Manager Screenshot](clipboard\images\tkinter_clipboard.png)

The Clipboard Manager provides a user-friendly interface for:
- Viewing clipboard history (last 10 unique items)
- Setting any historical item as the current clipboard content
- Monitoring clipboard changes in real-time
- Status updates with timestamps

Run it with:
```bash
python clipboard/tkinter_clibboard_gui.py
```

## Planned Utilities

The following utilities are planned for future releases:

### File Management
- File synchronization tools
- Duplicate file finder
- Batch file renaming utility
- Directory comparison tool

### System Monitoring
- CPU/Memory usage monitor
- Disk space analyzer
- Network traffic monitor
- Process manager

### Automation Tools
- Task scheduler
- Keyboard/mouse macro recorder
- Batch file processor
- System backup utility

### Text Processing
- Text format converter
- Regex search and replace tool
- Code snippet manager
- Markdown processor

## Installation

Each utility has its own installation requirements. Please refer to the specific utility's documentation for detailed installation instructions.

Global requirements:
- Python 3.6+
- pip (Python package manager)

## Usage

Utilities are organized in separate directories with their own documentation and examples. Navigate to the specific utility directory to learn more about its usage.

```bash
cd [utility-directory]
python [utility-script].py
```

## Contributing

Contributions are welcome! If you'd like to add a new utility or improve an existing one:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-utility`)
3. Commit your changes (`git commit -m 'Add amazing utility'`)
4. Push to the branch (`git push origin feature/amazing-utility`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 