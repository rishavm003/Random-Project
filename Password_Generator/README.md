# Secure Password Generator

A tool to generate strong, randomized passwords with customizable complexity (length, symbols, numbers, and case).

## 🛠 Technology Stack
- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Security**: Python `secrets` and `string` modules

## 📐 System Design
- **Character Pool**: Dynamically builds a pool of characters based on user preferences.
- **Random Selection**: Uses cryptographically secure random numbers to pick characters from the pool.
- **Clipboard Integration**: Allows users to copy generated passwords with one click.

## 🚀 How to Start

### GUI Version
```bash
python gui.py
```

### CLI Version
```bash
python main.py
```
