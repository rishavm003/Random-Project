# Snake Game (Modern Edition)

A classic arcade experience reimagined with a premium, neon-inspired web GUI and a classic lightweight console version.

## 🛠 Technology Stack
### Modern Web GUI
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Visuals**: Neon Glow Effects, Glassmorphism, CSS Animations

### Classic Console Version
- **Language**: C
- **Platform**: Windows (conio.h)

## 📐 System Design
- **Game Engine**: Uses a requestAnimationFrame-based loop for the web and a millisecond-sleep loop for the console.
- **Collision Logic**: Handles wall-wrapping, self-collision, and food ingestion.
- **State Management**: 
  - Web: Tracks score and high score using `localStorage`.
  - Console: Uses real-time coordinate tracking on the terminal buffer.

## 🚀 How to Run

### Web GUI (Recommended)
1. Navigate to the `gui/` folder.
2. Open `index.html` in any modern browser.

### Console Version
1. Run `.\SnakeGame.exe` in your terminal.
2. Or compile from source:
   ```bash
   gcc main.c -o SnakeGame.exe
   ```

## 🎮 Controls
- **Arrow Keys / WASD**: Change direction.
- **P**: Pause/Resume (Web).
- **Space / Enter**: Start/Restart game (Web).
- **X**: Exit (Console).
