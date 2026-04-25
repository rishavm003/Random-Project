# Digital Clock

A real-time digital clock with GUI built in C using Win32 API.

## Features

- **Real-time display** - Updates every 100ms for smooth seconds display
- **Time display** - Shows current time in HH:MM:SS format (24-hour)
- **Date display** - Shows full date with day, month, and year
- **Modern dark theme** - Catppuccin-inspired color scheme
- **Centered window** - Opens in the center of the screen

## Compilation

### Using MinGW (GCC)

```bash
cd Digital_Clock
gcc main.c -o DigitalClock.exe -mwindows
```

### Using MSVC

```cmd
cd Digital_Clock
cl main.c user32.lib gdi32.lib kernel32.lib
```

## Running

After compilation, run the executable:

```bash
DigitalClock.exe
```

## Controls

- **Minimize** - Minimize to taskbar
- **Close (X)** - Exit the application

## Color Scheme

- Background: `#1e1e2e` (dark)
- Display background: `#181825` (darker)
- Time text: `#cdd6f4` (white)
- Date text: `#a6adc8` (gray)
- Title: `#cba6f7` (purple accent)
