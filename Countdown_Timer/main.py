import time
import sys

def parse_time(time_str):
    """Parse HH:MM:SS or MM:SS or just seconds into total seconds."""
    parts = time_str.strip().split(":")
    try:
        if len(parts) == 3:
            h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
        elif len(parts) == 2:
            h, m, s = 0, int(parts[0]), int(parts[1])
        elif len(parts) == 1:
            h, m, s = 0, 0, int(parts[0])
        else:
            raise ValueError
        return h * 3600 + m * 60 + s
    except ValueError:
        return None

def format_time(total_seconds):
    """Convert total seconds to HH:MM:SS string."""
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def countdown(total_seconds):
    """Run the countdown loop."""
    print()
    while total_seconds >= 0:
        display = format_time(total_seconds)
        # Print timer on same line using carriage return
        print(f"\r  ⏱  {display}  ", end="", flush=True)
        if total_seconds == 0:
            break
        time.sleep(1)
        total_seconds -= 1
    
    print("\n\n  🔔 TIME IS UP!\n")

def main():
    print("\n--- COUNTDOWN TIMER ---")
    print("Enter time in HH:MM:SS, MM:SS, or just seconds\n")
    
    time_input = input("  Enter countdown time: ")
    total_seconds = parse_time(time_input)
    
    if total_seconds is None or total_seconds <= 0:
        print("  Invalid input! Please enter a valid time (e.g. 1:30 or 90).")
        return
    
    print(f"\n  Starting countdown from {format_time(total_seconds)}...")
    print("  Press Ctrl+C to stop.\n")
    
    try:
        countdown(total_seconds)
    except KeyboardInterrupt:
        print("\n\n  Timer stopped by user.")

if __name__ == "__main__":
    main()
