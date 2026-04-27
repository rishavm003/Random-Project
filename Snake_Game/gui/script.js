const canvas = document.getElementById('snakeGame');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const highScoreEl = document.getElementById('high-score');
const overlay = document.getElementById('overlay');
const startBtn = document.getElementById('start-btn');
const statusTitle = document.getElementById('status-title');
const statusMsg = document.getElementById('status-msg');

const gridSize = 20;
const tileCount = canvas.width / gridSize;
const pauseBtn = document.getElementById('pause-btn');
const stopBtn = document.getElementById('stop-btn');

let score = 0;
let highScore = localStorage.getItem('snakeHighScore') || 0;
highScoreEl.textContent = String(highScore).padStart(3, '0');

let snake = [{ x: 10, y: 10 }];
let food = { x: 5, y: 5 };
let dx = 0;
let dy = 0;
let nextDx = 0;
let nextDy = 0;
let gameRunning = false;
let isPaused = false;
let gameSpeed = 100;
let lastRenderTime = 0;

function main(currentTime) {
    if (!gameRunning) return;
    if (isPaused) {
        window.requestAnimationFrame(main);
        return;
    }

    window.requestAnimationFrame(main);
    const secondsSinceLastRender = (currentTime - lastRenderTime);
    if (secondsSinceLastRender < gameSpeed) return;

    lastRenderTime = currentTime;
    update();
    draw();
}

function update() {
    dx = nextDx;
    dy = nextDy;

    const head = { x: snake[0].x + dx, y: snake[0].y + dy };

    // Wall collision (wrap around)
    if (head.x < 0) head.x = tileCount - 1;
    if (head.x >= tileCount) head.x = 0;
    if (head.y < 0) head.y = tileCount - 1;
    if (head.y >= tileCount) head.y = 0;

    // Self collision
    if (snake.some((segment, index) => index !== 0 && segment.x === head.x && segment.y === head.y)) {
        gameOver();
        return;
    }

    snake.unshift(head);

    // Food collision
    if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreEl.textContent = String(score).padStart(3, '0');
        if (score > highScore) {
            highScore = score;
            highScoreEl.textContent = String(highScore).padStart(3, '0');
            localStorage.setItem('snakeHighScore', highScore);
        }
        generateFood();
        // Slightly increase speed
        if (gameSpeed > 60) gameSpeed -= 1;
    } else {
        snake.pop();
    }
}

function draw() {
    // Clear canvas
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw grid lines (subtle)
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 1;
    for (let i = 0; i < tileCount; i++) {
        ctx.beginPath();
        ctx.moveTo(i * gridSize, 0);
        ctx.lineTo(i * gridSize, canvas.height);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(0, i * gridSize);
        ctx.lineTo(canvas.width, i * gridSize);
        ctx.stroke();
    }

    // Draw food
    ctx.fillStyle = '#ef4444';
    ctx.shadowBlur = 15;
    ctx.shadowColor = '#ef4444';
    ctx.beginPath();
    ctx.arc(food.x * gridSize + gridSize/2, food.y * gridSize + gridSize/2, gridSize/2 - 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // Draw snake
    snake.forEach((segment, index) => {
        const isHead = index === 0;
        ctx.fillStyle = isHead ? '#4ade80' : '#22c55e';
        
        // Add glow to head
        if (isHead) {
            ctx.shadowBlur = 15;
            ctx.shadowColor = '#4ade80';
        }

        ctx.fillRect(segment.x * gridSize + 1, segment.y * gridSize + 1, gridSize - 2, gridSize - 2);
        ctx.shadowBlur = 0;
    });
}

function generateFood() {
    food = {
        x: Math.floor(Math.random() * tileCount),
        y: Math.floor(Math.random() * tileCount)
    };
    // Don't spawn food on snake
    if (snake.some(segment => segment.x === food.x && segment.y === food.y)) {
        generateFood();
    }
}

function startGame() {
    score = 0;
    scoreEl.textContent = '000';
    snake = [{ x: 10, y: 10 }];
    nextDx = 1;
    nextDy = 0;
    gameSpeed = 100;
    gameRunning = true;
    isPaused = false;
    
    pauseBtn.disabled = false;
    stopBtn.disabled = false;
    pauseBtn.textContent = 'PAUSE';
    pauseBtn.classList.remove('paused');
    
    overlay.classList.add('hidden');
    generateFood();
    window.requestAnimationFrame(main);
}

function togglePause() {
    if (!gameRunning) return;
    isPaused = !isPaused;
    pauseBtn.textContent = isPaused ? 'RESUME' : 'PAUSE';
    pauseBtn.classList.toggle('paused');
}

function stopGame() {
    if (!gameRunning) return;
    gameOver('GAME STOPPED');
}

function gameOver(title = 'GAME OVER') {
    gameRunning = false;
    isPaused = false;
    pauseBtn.disabled = true;
    stopBtn.disabled = true;
    overlay.classList.remove('hidden');
    statusTitle.textContent = title;
    statusMsg.textContent = `Your Score: ${score}`;
    startBtn.textContent = 'TRY AGAIN';
}

window.addEventListener('keydown', e => {
    switch (e.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
            if (dy !== 1) { nextDx = 0; nextDy = -1; }
            break;
        case 'ArrowDown':
        case 's':
        case 'S':
            if (dy !== -1) { nextDx = 0; nextDy = 1; }
            break;
        case 'ArrowLeft':
        case 'a':
        case 'A':
            if (dx !== 1) { nextDx = -1; nextDy = 0; }
            break;
        case 'ArrowRight':
        case 'd':
        case 'D':
            if (dx !== -1) { nextDx = 1; nextDy = 0; }
            break;
        case 'p':
        case 'P':
            togglePause();
            break;
    }
    
    if (!gameRunning && (e.key === ' ' || e.key === 'Enter')) {
        startGame();
    }
});

pauseBtn.addEventListener('click', togglePause);
stopBtn.addEventListener('click', stopGame);

startBtn.addEventListener('click', startGame);

// Initial draw
draw();
