let canvas = document.getElementById('fireworksCanvas');
const ctx = canvas.getContext('2d');
const particles = [];

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// 控制整个烟花的缩放比例
const scale = 0.25; // 0.25表示烟花效果缩小到原来的四分之一

function getRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r},${g},${b})`;
}

function createParticle(x, y) {
    const particlesCount = 100;
    const radius = 25 * scale; // 圆形轨迹的半径

    for (let i = 0; i < particlesCount; i++) {
        const angle = Math.random() * 2 * Math.PI;
        const speed = Math.random() * 10 * scale;

        particles.push({
            x: x,
            y: y,
            vx: Math.cos(angle) * speed, // 圆形扩散的速度分量
            vy: Math.sin(angle) * speed, // 圆形扩散的速度分量
            life: Math.random() * 2 + 1,
            color: getRandomColor(),
            radius: (Math.random() * 5 + 1) * scale // 缩放初始半径
        });
    }
}

function updateParticles() {
    for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.life -= 0.05;

        if (p.life <= 0) {
            particles.splice(i, 1);
        }
    }
}

function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
    });
}

function animate() {
    updateParticles();
    drawParticles();
    requestAnimationFrame(animate);
}

canvas.addEventListener('click', (e) => {
    createParticle(e.clientX, e.clientY);
});

animate();