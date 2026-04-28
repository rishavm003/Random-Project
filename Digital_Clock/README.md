# Digital Clock

A real-time digital clock project featuring both a native Windows (C/Win32) implementation and a premium modern web interface.

## 🛠 Technology Stack
### Web Version
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Design**: Glassmorphism, CSS Gradients, Parallax Effects

### Native Version
- **Language**: C
- **API**: Win32 API
- **Compiler**: GCC (MinGW) or MSVC

## 📐 System Design
- **Time Sync**: Both versions utilize the system clock to ensure millisecond accuracy.
- **Rendering Engine**: 
  - The Web version uses CSS Flexbox and Backdrop Filters for a glass effect.
  - The Native version uses a standard Windows message loop and GDI for drawing.
- **Toggle Logic**: Implements internal state tracking for 12/24-hour time formatting.

## 🚀 How to Start

### Modern Web Version (Recommended)
1. Navigate to the `web/` folder.
2. Open `index.html` in any modern browser.

### Native Win32 Version
1. Run `DigitalClock.exe` directly.
2. Or compile from source:
   ```bash
   gcc main.c -o DigitalClock.exe -mwindows
   ```

## 🎮 Controls
- **Web**: Click the time to toggle 12/24h format.
- **Native**: Click anywhere on the window to cycle themes.
