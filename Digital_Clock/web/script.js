const timeDisplay = document.getElementById('time-display');
const dateDisplay = document.getElementById('date-display');
const formatToggle = document.getElementById('format-toggle');
const themeToggle = document.getElementById('theme-toggle');
const clockCard = document.getElementById('clock-card');

let is24Hour = true;
let glassLevel = 1;

function updateClock() {
    const now = new Date();
    
    // Time
    let hours = now.getHours();
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    if (!is24Hour) {
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12 || 12;
        timeDisplay.textContent = `${hours}:${minutes}:${seconds} ${ampm}`;
    } else {
        timeDisplay.textContent = `${String(hours).padStart(2, '0')}:${minutes}:${seconds}`;
    }
    
    // Date
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    dateDisplay.textContent = now.toLocaleDateString(undefined, options);
}

formatToggle.addEventListener('click', () => {
    is24Hour = !is24Hour;
    formatToggle.textContent = is24Hour ? '24H' : '12H';
    updateClock();
});

themeToggle.addEventListener('click', () => {
    glassLevel = (glassLevel + 1) % 3;
    const blurs = ['blur(0px)', 'blur(12px)', 'blur(40px)'];
    const names = ['FLAT', 'GLASS', 'FROSTED'];
    
    clockCard.style.backdropFilter = blurs[glassLevel];
    clockCard.style.webkitBackdropFilter = blurs[glassLevel];
    themeToggle.textContent = names[glassLevel];
});

// Update every second
setInterval(updateClock, 1000);
updateClock();

// Subtle parallax effect on mouse move
document.addEventListener('mousemove', (e) => {
    const x = (window.innerWidth / 2 - e.pageX) / 25;
    const y = (window.innerHeight / 2 - e.pageY) / 25;
    clockCard.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
});
