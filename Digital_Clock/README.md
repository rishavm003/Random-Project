1: # Digital Clock
2: 
3: A real-time digital clock with both a native Win32 GUI and a modern web interface.
4: 
5: ## Versions
6: 
7: ### 1. Modern Web Version (Recommended)
8: A premium, glassmorphism-inspired web application with dynamic backgrounds and interactive effects.
9: - **Location**: `web/index.html`
10: - **Features**: Glassmorphism, 12/24h toggle, theme switching, parallax effects.
11: 
12: ### 2. Native Win32 Version
13: A lightweight C-based application for Windows.
14: - **Location**: `DigitalClock.exe`
15: - **Features**: Dark theme, real-time updates, minimal footprint.
16: 
17: ## Modern Web Features
18: 
19: - **Glassmorphism UI** - Frosted glass effect for a sleek look.
20: - **Dynamic Backgrounds** - Custom mesh gradient background.
21: - **Responsive Design** - Works on all screen sizes.
22: - **Interactivity** - Mouse-tracking parallax and format toggling.
23: 
24: ## Native Compilation
25: 
26: ### Using MinGW (GCC)
27: 
28: ```bash
29: gcc main.c -o DigitalClock.exe -mwindows
30: ```
31: 
32: ### Using MSVC
33: 
34: ```cmd
35: cl main.c user32.lib gdi32.lib kernel32.lib
36: ```
37: 
38: ## Running
39: 
40: - **Web**: Open `web/index.html` in your browser.
41: - **Native**: Run `DigitalClock.exe`.
42: 
43: ## Color Scheme (Web)
44: 
45: - Background: Mesh Gradient (Purples/Blues)
46: - Card: Semi-transparent glass
47: - Accent: `#818cf8` (Indigo)
48: - Text: `#f8fafc` (Slate white)

