#include <windows.h>
#include <time.h>
#include <string.h>

#define ID_TIMER 1
#define WINDOW_WIDTH 500
#define WINDOW_HEIGHT 280

// Color scheme matching the dark theme
#define COLOR_BG        RGB(30, 30, 46)      // #1e1e2e
#define COLOR_DISPLAY   RGB(24, 24, 37)      // #181825
#define COLOR_TEXT      RGB(205, 214, 244)   // #cdd6f4
#define COLOR_ACCENT    RGB(203, 166, 247)   // #cba6f7
#define COLOR_DATE      RGB(166, 173, 200)   // #a6adc8

// Global variables
HWND hwndTitleLabel;
HWND hwndTimeLabel;
HWND hwndDateLabel;
HFONT hTimeFont;
HFONT hDateFont;
HFONT hTitleFont;

// Window procedure
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE: {
            // Create title label
            hwndTitleLabel = CreateWindow(
                "STATIC", "DIGITAL CLOCK",
                WS_VISIBLE | WS_CHILD | SS_CENTER,
                0, 20, WINDOW_WIDTH, 40,
                hwnd, NULL, NULL, NULL
            );
            
            // Create time display label
            hwndTimeLabel = CreateWindow(
                "STATIC", "00:00:00",
                WS_VISIBLE | WS_CHILD | SS_CENTER,
                50, 70, 400, 100,
                hwnd, NULL, NULL, NULL
            );
            
            // Create date display label
            hwndDateLabel = CreateWindow(
                "STATIC", "Loading...",
                WS_VISIBLE | WS_CHILD | SS_CENTER,
                0, 180, WINDOW_WIDTH, 35,
                hwnd, NULL, NULL, NULL
            );
            
            // Create fonts
            hTimeFont = CreateFont(
                72, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, FF_MODERN, "Consolas"
            );
            
            hDateFont = CreateFont(
                22, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, FF_SWISS, "Segoe UI"
            );
            
            hTitleFont = CreateFont(
                18, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
                CLEARTYPE_QUALITY, FF_SWISS, "Segoe UI"
            );
            
            // Apply fonts
            SendMessage(hwndTimeLabel, WM_SETFONT, (WPARAM)hTimeFont, TRUE);
            SendMessage(hwndDateLabel, WM_SETFONT, (WPARAM)hDateFont, TRUE);
            SendMessage(hwndTitleLabel, WM_SETFONT, (WPARAM)hTitleFont, TRUE);
            
            // Start timer (updates every 100ms for smooth seconds)
            SetTimer(hwnd, ID_TIMER, 100, NULL);
            
            return 0;
        }
        
        case WM_TIMER: {
            // Get current time
            time_t now = time(NULL);
            struct tm* localTime = localtime(&now);
            
            // Format time string HH:MM:SS
            char timeStr[16];
            strftime(timeStr, sizeof(timeStr), "%H:%M:%S", localTime);
            
            // Format date string
            char dateStr[64];
            strftime(dateStr, sizeof(dateStr), "%A, %B %d, %Y", localTime);
            
            // Update labels
            SetWindowText(hwndTimeLabel, timeStr);
            SetWindowText(hwndDateLabel, dateStr);
            
            return 0;
        }
        
        case WM_CTLCOLORSTATIC: {
            HDC hdc = (HDC)wParam;
            HWND hwndControl = (HWND)lParam;
            
            // Set text color
            if (hwndControl == hwndTimeLabel) {
                SetTextColor(hdc, COLOR_TEXT);
            } else if (hwndControl == hwndDateLabel) {
                SetTextColor(hdc, COLOR_DATE);
            } else {
                SetTextColor(hdc, COLOR_ACCENT);
            }
            
            // Set background to transparent
            SetBkMode(hdc, TRANSPARENT);
            
            // Return background brush
            static HBRUSH hBrush = NULL;
            if (hBrush == NULL) {
                hBrush = CreateSolidBrush(COLOR_DISPLAY);
            }
            return (LRESULT)hBrush;
        }
        
        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);
            
            // Fill background
            RECT rect;
            GetClientRect(hwnd, &rect);
            FillRect(hdc, &rect, CreateSolidBrush(COLOR_BG));
            
            // Draw display frame background
            RECT displayRect = { 25, 60, 475, 180 };
            HBRUSH hDisplayBrush = CreateSolidBrush(COLOR_DISPLAY);
            FillRect(hdc, &displayRect, hDisplayBrush);
            DeleteObject(hDisplayBrush);
            
            // Draw subtle border
            HPEN hPen = CreatePen(PS_SOLID, 2, RGB(69, 71, 90));
            SelectObject(hdc, hPen);
            RoundRect(hdc, 25, 60, 475, 180, 8, 8);
            DeleteObject(hPen);
            
            EndPaint(hwnd, &ps);
            return 0;
        }
        
        case WM_ERASEBKGND: {
            // Custom erase to prevent flicker
            HDC hdc = (HDC)wParam;
            RECT rect;
            GetClientRect(hwnd, &rect);
            FillRect(hdc, &rect, CreateSolidBrush(COLOR_BG));
            return 1;
        }
        
        case WM_DESTROY: {
            // Cleanup
            KillTimer(hwnd, ID_TIMER);
            DeleteObject(hTimeFont);
            DeleteObject(hDateFont);
            DeleteObject(hTitleFont);
            PostQuitMessage(0);
            return 0;
        }
        
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
                   LPSTR lpCmdLine, int nCmdShow) {
    // Register window class
    WNDCLASS wc = {0};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "DigitalClockClass";
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    
    RegisterClass(&wc);
    
    // Calculate center position
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);
    int xPos = (screenWidth - WINDOW_WIDTH) / 2;
    int yPos = (screenHeight - WINDOW_HEIGHT) / 2;
    
    // Create window
    HWND hwnd = CreateWindowEx(
        0,
        "DigitalClockClass",
        "Digital Clock",
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX,
        xPos, yPos,
        WINDOW_WIDTH, WINDOW_HEIGHT,
        NULL, NULL, hInstance, NULL
    );
    
    if (hwnd == NULL) {
        return 0;
    }
    
    ShowWindow(hwnd, nCmdShow);
    
    // Message loop
    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    
    return 0;
}
