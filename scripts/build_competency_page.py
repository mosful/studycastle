# -*- coding: utf-8 -*-
"""
生成 math6_competency.html - 國小六年級數學「Follow Me 學素養」全冊旗艦互動學習頁面
"""

import os

html_content = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>6上數學 Follow Me 素養魔法冒險王 🌟 全冊素養旗艦 | 學習城堡</title>
<!-- Favicon 網站圖示 -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="apple-touch-icon" href="favicon.svg">
<meta name="description" content="國小 6 年級上學期數學「Follow Me 學素養」全冊跨領域主題探究：畢業旅行大分組、BMI健康體位、蛋糕披薩CP值、半月湖環湖步道、低碳鐵馬行速率、建築積木規律！">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Fredoka:wght@600;700&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="study-castle-ui.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js"></script>

<style>
  :root {
    --primary: #059669;
    --primary-light: #34D399;
    --primary-dark: #065F46;
    --accent: #F59E0B;
    --accent-gold: #D97706;
    --bg-gradient: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 50%, #FEF3C7 100%);
    --card-bg: rgba(255, 255, 255, 0.96);
    --card-shadow: 0 10px 25px -5px rgba(5, 150, 105, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
    --border-color: #A7F3D0;
    --text-main: #0F172A;
    --text-muted: #475569;
    --radius-lg: 20px;
    --radius-md: 12px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Noto Sans TC', sans-serif;
    background: var(--bg-gradient);
    color: var(--text-main);
    line-height: 1.6;
    min-height: 100vh;
    padding-bottom: 60px;
  }

  .top-navbar {
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(12px);
    border-bottom: 2px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .nav-left {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .back-btn {
    text-decoration: none;
    background: #F1F5F9;
    color: var(--text-main);
    padding: 8px 14px;
    border-radius: var(--radius-md);
    font-weight: 700;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 6px;
    border: 1px solid #E2E8F0;
  }
  .back-btn:hover {
    background: #E2E8F0;
    transform: translateX(-2px);
  }
  .nav-brand {
    font-family: 'Fredoka', 'Noto Sans TC', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--primary-dark);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .badge-tag {
    background: #D1FAE5;
    color: var(--primary-dark);
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 800;
    border: 1px solid #6EE7B7;
  }
  .nav-right {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .stat-pill {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    color: #92400E;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 800;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .btn-icon {
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-radius: 50%;
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.1rem;
    transition: all 0.2s ease;
  }
  .btn-icon:hover {
    background: #E2E8F0;
    transform: scale(1.05);
  }

  .hero-container {
    max-width: 1040px;
    margin: 24px auto 16px;
    padding: 0 16px;
  }
  .hero-banner {
    background: linear-gradient(135deg, #065F46 0%, #059669 60%, #10B981 100%);
    color: #FFFFFF;
    border-radius: var(--radius-lg);
    padding: 32px 28px;
    box-shadow: 0 12px 30px rgba(5, 150, 105, 0.25);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    position: relative;
    overflow: hidden;
  }
  .hero-banner::after {
    content: "🌟🌍🎒";
    position: absolute;
    right: -10px;
    bottom: -15px;
    font-size: 5rem;
    opacity: 0.15;
    pointer-events: none;
  }
  .hero-content h1 {
    font-size: 2.1rem;
    font-weight: 900;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
  }
  .hero-content p {
    font-size: 1.05rem;
    color: #D1FAE5;
    max-width: 620px;
    line-height: 1.5;
  }
  .hero-mascot {
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(6px);
    padding: 12px 18px;
    border-radius: var(--radius-md);
    border: 1px solid rgba(255, 255, 255, 0.25);
  }
  .mascot-avatar {
    font-size: 2.8rem;
    animation: floatMascot 3s ease-in-out infinite;
  }
  @keyframes floatMascot {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
  .mascot-bubble {
    font-size: 0.95rem;
    font-weight: 700;
    color: #FFF;
  }

  .stage-nav {
    max-width: 1040px;
    margin: 16px auto;
    padding: 0 16px;
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding-bottom: 8px;
  }
  .stage-tab {
    flex: 1;
    min-width: 120px;
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--radius-md);
    padding: 10px 8px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    user-select: none;
  }
  .stage-tab:hover {
    border-color: var(--primary-light);
    transform: translateY(-2px);
  }
  .stage-tab.active {
    background: #ECFDF5;
    border-color: var(--primary);
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.15);
  }
  .stage-tab-num {
    font-size: 0.72rem;
    font-weight: 800;
    color: var(--primary-dark);
    text-transform: uppercase;
    display: block;
    margin-bottom: 2px;
  }
  .stage-tab-title {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-main);
    white-space: nowrap;
  }

  .main-container {
    max-width: 1040px;
    margin: 0 auto;
    padding: 0 16px;
  }
  .section-card {
    background: var(--card-bg);
    border-radius: var(--radius-lg);
    box-shadow: var(--card-shadow);
    border: 1px solid var(--border-color);
    padding: 28px;
    margin-bottom: 24px;
    animation: fadeIn 0.3s ease;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .card-header {
    border-bottom: 2px solid #F1F5F9;
    padding-bottom: 14px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .card-title {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--primary-dark);
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .concept-box {
    background: #F8FAFC;
    border-left: 5px solid var(--primary);
    padding: 16px 20px;
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    margin-bottom: 20px;
    line-height: 1.7;
    font-size: 1.05rem;
  }
  .concept-box strong {
    color: var(--primary-dark);
  }
  .concept-highlight {
    background: #FEF3C7;
    color: #92400E;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
  }

  .lab-widget {
    background: #FFFFFF;
    border: 2px dashed #6EE7B7;
    border-radius: var(--radius-lg);
    padding: 24px;
    margin: 20px 0;
  }
  .slider-row {
    margin-bottom: 14px;
  }
  .slider-row label {
    display: flex;
    justify-content: space-between;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .slider-row input[type="range"] {
    width: 100%;
    accent-color: var(--primary);
  }
  .lab-metrics {
    background: #ECFDF5;
    border-radius: var(--radius-md);
    padding: 14px 18px;
    margin-top: 14px;
    border: 1px solid #A7F3D0;
  }
  .metrics-line {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 4px;
    color: var(--primary-dark);
  }

  .quiz-list {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 16px;
  }
  .quiz-item {
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--radius-md);
    padding: 20px;
    transition: all 0.2s ease;
  }
  .quiz-item.correct-item {
    border-color: #10B981;
    background: #F0FDF4;
  }
  .quiz-item.wrong-item {
    border-color: #F87171;
    background: #FEF2F2;
  }
  .quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 12px;
  }
  .quiz-qnum {
    background: #E2E8F0;
    color: #334155;
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 800;
  }
  .quiz-text {
    font-size: 1.05rem;
    font-weight: 700;
    color: #1E293B;
    flex: 1;
    line-height: 1.6;
  }
  .quiz-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 10px;
    margin-top: 14px;
  }
  .quiz-opt-btn {
    background: #F8FAFC;
    border: 2px solid #CBD5E1;
    border-radius: 10px;
    padding: 12px 14px;
    text-align: left;
    font-size: 1rem;
    font-weight: 600;
    color: #334155;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .quiz-opt-btn:hover:not(:disabled) {
    background: #F1F5F9;
    border-color: var(--primary-light);
    transform: translateY(-1px);
  }
  .quiz-opt-btn.correct-opt {
    background: #10B981 !important;
    border-color: #059669 !important;
    color: #FFF !important;
  }
  .quiz-opt-btn.wrong-opt {
    background: #EF4444 !important;
    border-color: #DC2626 !important;
    color: #FFF !important;
  }
  .quiz-explain {
    background: #EFF6FF;
    border-left: 4px solid #3B82F6;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin-top: 14px;
    font-size: 0.95rem;
    color: #1E3A8A;
    display: none;
    line-height: 1.6;
  }

  .card-footer {
    margin-top: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 2px solid #F1F5F9;
    padding-top: 18px;
  }
  .btn-next-stage {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: #FFF;
    border: none;
    padding: 12px 26px;
    border-radius: var(--radius-md);
    font-size: 1.05rem;
    font-weight: 800;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);
  }
  .btn-next-stage:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(5, 150, 105, 0.3);
  }

  .badge-showcase {
    text-align: center;
    padding: 30px 10px;
  }
  .medal-icon {
    font-size: 5rem;
    margin-bottom: 16px;
    animation: medalBounce 1.5s infinite alternate ease-in-out;
  }
  @keyframes medalBounce {
    from { transform: scale(1); }
    to { transform: scale(1.1) rotate(5deg); }
  }

  .modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 999;
    padding: 16px;
  }
  .modal-overlay.open {
    display: flex;
  }
  .modal-content {
    background: #FFFFFF;
    border-radius: var(--radius-lg);
    max-width: 540px;
    width: 100%;
    padding: 28px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
    animation: modalPop 0.25s ease-out;
    position: relative;
  }
  @keyframes modalPop {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
  }
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
  }
  .modal-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--primary-dark);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .modal-close {
    background: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #94A3B8;
  }
  .modal-close:hover { color: #334155; }
  .modal-body {
    font-size: 1rem;
    color: #334155;
    line-height: 1.7;
    max-height: 70vh;
    overflow-y: auto;
  }

  @media (max-width: 768px) {
    .hero-content h1 { font-size: 1.6rem; }
    .hero-banner { padding: 22px 18px; }
    .section-card { padding: 18px; }
    .quiz-options { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<header class="top-navbar">
  <div class="nav-left">
    <a href="portal.html" class="back-btn">
      <span>🏰 返回傳送門</span>
    </a>
    <div class="nav-brand">
      <span>🌟 數學素養冒險王</span>
      <span class="badge-tag">6上・全冊素養旗艦</span>
    </div>
  </div>
  <div class="nav-right">
    <div class="stat-pill">
      <span>⭐ 能量:</span>
      <span id="scoreText">0</span>
    </div>
    <div class="stat-pill" style="background:#ECFDF5; border-color:#A7F3D0; color:#065F46;">
      <span>🔥 連擊:</span>
      <span id="comboText">0</span>
    </div>
    <button class="btn-icon" onclick="openGlossary()" title="素養寶典">📖</button>
    <button class="btn-icon" id="soundBtn" onclick="toggleSound()" title="音效切換">🔊</button>
  </div>
</header>

<section class="hero-container">
  <div class="hero-banner">
    <div class="hero-content">
      <h1>6上數學 Follow Me 素養魔法冒險王</h1>
      <p>解鎖全冊 8 大生活跨領域素養任務！從畢旅分組、健康 BMI、披薩 CP 值到低碳減碳鐵馬行，用數學思維解決生活中的真實問題！</p>
    </div>
    <div class="hero-mascot">
      <div class="mascot-avatar">🎒</div>
      <div class="mascot-bubble" id="mascotMessage">歡迎來到素養大冒險！數學不只是課本公式，更是解決生活問題的超能力！</div>
    </div>
  </div>
</section>

<nav class="stage-nav" id="stageTabs">
  <div class="stage-tab active" onclick="gotoStage(0)">
    <span class="stage-tab-num">Quest 1</span>
    <span class="stage-tab-title">畢旅大分組</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(1)">
    <span class="stage-tab-num">Quest 2</span>
    <span class="stage-tab-title">烘焙果汁分裝</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(2)">
    <span class="stage-tab-num">Quest 3</span>
    <span class="stage-tab-title">BMI健康體位</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(3)">
    <span class="stage-tab-num">Quest 4</span>
    <span class="stage-tab-title">披薩哪個划算</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(4)">
    <span class="stage-tab-num">Quest 5</span>
    <span class="stage-tab-title">全校通勤比率</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(5)">
    <span class="stage-tab-num">Quest 6</span>
    <span class="stage-tab-title">半月湖步道</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(6)">
    <span class="stage-tab-num">Quest 7</span>
    <span class="stage-tab-title">低碳減碳行</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(7)">
    <span class="stage-tab-num">Quest 8</span>
    <span class="stage-tab-title">建築立體積木</span>
  </div>
</nav>

<main class="main-container" id="stageContainer">
</main>

<div class="modal-overlay" id="castleModalOverlay" onclick="closeCastleModalOnBackdrop(event)">
  <div class="modal-content">
    <div class="modal-header">
      <div class="modal-title">
        <span id="castleModalIcon">💡</span>
        <span id="castleModalTitle">系統提示</span>
      </div>
      <button class="modal-close" onclick="closeCastleModal()">✕</button>
    </div>
    <div class="modal-body" id="castleModalBody">
    </div>
  </div>
</div>

<script>
let audioCtx = null;
let soundEnabled = true;

function initAudio() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) audioCtx = new AudioContext();
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

function playTone(freq, type = 'sine', duration = 0.15, vol = 0.25) {
  if (!soundEnabled) return;
  try {
    initAudio();
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(vol, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch(e) {}
}

function playSound(name) {
  if (!soundEnabled) return;
  if (name === 'correct') {
    playTone(523.25, 'triangle', 0.1, 0.2);
    setTimeout(() => playTone(659.25, 'triangle', 0.1, 0.2), 80);
    setTimeout(() => playTone(783.99, 'triangle', 0.2, 0.25), 160);
  } else if (name === 'wrong') {
    playTone(260, 'sawtooth', 0.15, 0.25);
    setTimeout(() => playTone(196, 'sawtooth', 0.25, 0.3), 120);
  } else if (name === 'level_clear') {
    const notes = [523.25, 659.25, 783.99, 1046.5];
    notes.forEach((f, idx) => {
      setTimeout(() => playTone(f, 'sine', 0.2, 0.3), idx * 100);
    });
  } else if (name === 'click') {
    playTone(400, 'sine', 0.05, 0.1);
  }
}

function toggleSound() {
  soundEnabled = !soundEnabled;
  const btn = document.getElementById('soundBtn');
  btn.textContent = soundEnabled ? '🔊' : '🔇';
  showCastleModal('音效設定', soundEnabled ? '音效已開啟 🔊' : '音效已靜音 🔇', '🎵');
}

function showCastleModal(title, bodyHtml, icon = '💡', onClose = null) {
  const overlay = document.getElementById('castleModalOverlay');
  if (!overlay) return;
  document.getElementById('castleModalTitle').textContent = title;
  document.getElementById('castleModalBody').innerHTML = bodyHtml;
  document.getElementById('castleModalIcon').textContent = icon;
  overlay.classList.add('open');
  window._castleModalOnClose = onClose;
}

function closeCastleModal() {
  const overlay = document.getElementById('castleModalOverlay');
  if (overlay) overlay.classList.remove('open');
  if (typeof window._castleModalOnClose === 'function') {
    const cb = window._castleModalOnClose;
    window._castleModalOnClose = null;
    cb();
  }
}

function closeCastleModalOnBackdrop(e) {
  if (e.target && e.target.id === 'castleModalOverlay') {
    closeCastleModal();
  }
}

window.alert = function(msg) {
  showCastleModal('系統提示', `<div style="text-align:left; white-space:pre-line;">${msg}</div>`, '💡');
};

let userScore = 0;
let userCombo = 0;
let currentStage = 0;

function addScore(pts = 10) {
  userCombo++;
  const bonus = Math.floor(userCombo / 3) * 5;
  userScore += (pts + bonus);
  document.getElementById('scoreText').textContent = userScore;
  document.getElementById('comboText').textContent = userCombo;
  if (userCombo >= 3) {
    updateMascot(`🔥 素養大爆發！達成 ${userCombo} 連擊！額外加 ${bonus} 分！`);
  }
}

function resetCombo() {
  userCombo = 0;
  document.getElementById('comboText').textContent = userCombo;
}

function updateMascot(msg) {
  const el = document.getElementById('mascotMessage');
  if (el) el.textContent = msg;
}

function shuffleArray(arr) {
  const newArr = [...arr];
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]];
  }
  return newArr;
}

const stageData = [
  // Quest 1: 畢業旅行大分組 (第1單元)
  {
    title: "Quest 1：畢業旅行大分組 (最大公因數)",
    icon: "🎒",
    concept: `
      <strong>生活情境探究・畢業旅行分組（課本素養 P1）：</strong><br>
      友枝國小六年級舉辦畢業旅行，參加活動的男學生有 <strong>90 人</strong>，女學生有 <strong>126 人</strong>，共計 216 人。<br>
      • <strong>挑戰 1：</strong>老師想將這 216 人分組進行闖關，每組男生人數一樣多，每組女生人數也一樣多，全部分完，<strong>最多可以分成幾組？</strong><br>
        求 90 與 126 的最大公因數：<br>
        90 ＝ 2 × 3 × 3 × 5，126 ＝ 2 × 3 × 3 × 7 ➔ <strong>GCD ＝ 2 × 3 × 3 ＝ 18 組</strong>！<br>
      • <strong>每組人數：</strong>男生 90 ÷ 18 ＝ 5 人，女生 126 ÷ 18 ＝ 7 人，每組共 5 ＋ 7 ＝ <strong>12 人</strong>！
    `,
    quizzes: [
      {
        q: "男學生 90 人，女學生 126 人，每組男女生人數皆相同且全部分完，最多可分成幾組？每組有幾人？",
        options: ["最多分成 18 組，每組 12 人", "最多分成 9 組，每組 24 人", "最多分成 6 組，每組 36 人", "最多分成 12 組，每組 18 人"],
        ans: "最多分成 18 組，每組 12 人",
        explain: "求 GCD(90, 126) = 18 組。每組男生 90÷18 = 5 人，女生 126÷18 = 7 人，每組共 5 + 7 = 12 人。"
      },
      {
        q: "承上題，如果旅館有「4人房」與「6人房」，90 位男生要全部住滿且不男女混住，最少需要幾間房間？",
        options: ["15 間（全部住 6 人房）", "16 間", "18 間", "20 間"],
        ans: "15 間（全部住 6 人房）",
        explain: "90 ÷ 6 = 15 間（若全住 6 人房剛好住滿，房間數最少）。"
      }
    ]
  },

  // Quest 2: 烘焙果汁分裝 (第2單元)
  {
    title: "Quest 2：魔法烘焙果汁分裝師 (分數除法)",
    icon: "🍹",
    concept: `
      <strong>生活情境探究・果汁與布丁分裝（課本素養 P2）：</strong><br>
      廚房裡有 18 公升的特調綜合果汁，要分裝成每瓶 1又1/3 公升的玻璃瓶：<br>
      • <strong>計算瓶數：</strong>18 ÷ 1又1/3 ＝ 18 ÷ (4/3) ＝ 18 × (3/4) ＝ 27/2 ＝ <strong>13又1/2 瓶</strong>。<br>
      • <strong>解讀商數：</strong>可以裝滿 <strong>13 瓶</strong>，剩下 1/2 瓶（即 1又1/3 公升的 1/2 ＝ <strong>2/3 公升</strong>）！
    `,
    quizzes: [
      {
        q: "將 18 公升的果汁分裝成每瓶 1又1/3 公升，最多可以裝滿幾瓶？還剩下幾公升果汁？",
        options: ["裝滿 13 瓶，剩下 2/3 公升", "裝滿 13 瓶，剩下 1/2 公升", "裝滿 14 瓶，剩下 1/3 公升", "裝滿 12 瓶，剩下 1 公升"],
        ans: "裝滿 13 瓶，剩下 2/3 公升",
        explain: "18 ÷ (4/3) = 13 餘 1/2（瓶）。剩下的果汁容量 = 4/3 × (1/2) = 2/3 公升。"
      }
    ]
  },

  // Quest 3: BMI 健康體位密碼 (第3單元)
  {
    title: "Quest 3：體適能 BMI 健康體位密碼 (小數除法與概數)",
    icon: "🏃",
    concept: `
      <strong>生活情境探究・身體質量指數 BMI（課本素養 P3）：</strong><br>
      世界衛生組織 (WHO) 與我國衛福部成人健康體位標準：<br>
      • BMI ＜ 18.5（過輕）<br>
      • 18.5 ≤ BMI ＜ 24（<strong>健康體位</strong>）<br>
      • BMI ≥ 24（過重或肥胖）<br>
      <div class="concept-highlight" style="display:inline-block; margin:6px 0; font-size:1.05rem;">
        BMI ＝ 體重 (公斤) ÷ [身高 (公尺) × 身高 (公尺)]
      </div><br>
      • <strong>例題：</strong>芳熏身高 150 公分（1.5 公尺），體重 55 公斤：<br>
        1.5 × 1.5 ＝ 2.25。<br>
        55 ÷ 2.25 ＝ 24.444... ➔ 用四捨五入取概數到小數第一位為 <strong>24.4</strong>（屬於輕微過重）。
    `,
    hasBmiLab: true,
    quizzes: [
      {
        q: "芳熏身高 150 公分，體重 55 公斤。用四捨五入法取到小數第一位，她的 BMI 大約是多少？體位屬於哪一範圍？",
        options: ["24.4；過重", "24.4；健康體位", "22.5；健康體位", "25.0；過重"],
        ans: "24.4；過重",
        explain: "55 ÷ (1.5 × 1.5) = 55 ÷ 2.25 ≈ 24.44 ≈ 24.4。因 24.4 > 24，屬於過重範圍。"
      },
      {
        q: "小豪身高 160 公分（1.6m），若想讓 BMI 保持在 20（健康體位），他的體重應該是多少公斤？",
        options: ["51.2 公斤", "50 公斤", "48.5 公斤", "54 公斤"],
        ans: "51.2 公斤",
        explain: "體重 = BMI × 身高² = 20 × (1.6 × 1.6) = 20 × 2.56 = 51.2 公斤。"
      }
    ]
  },

  // Quest 4: 買哪個才划算 (第4單元)
  {
    title: "Quest 4：買哪個才划算？(圓面積與性價比 CP 值)",
    icon: "🍕",
    concept: `
      <strong>生活情境探究・披薩與蛋糕的面積秘密（課本素養 P4）：</strong><br>
      • <strong>半徑放大，面積倍數平方暴增：</strong><br>
        圓面積 ＝ 半徑 × 半徑 × 3.14。<br>
        當直徑從 12cm（半徑 6cm）變成 24cm（半徑 12cm），半徑變為 2 倍，<strong>面積會變成 2 × 2 ＝ 4 倍</strong>！<br>
      • <strong>性價比 (CP值) 計算：</strong>每平方公分花費多少元（價格 ÷ 面積）。每平方公分單價越低越划算！
    `,
    quizzes: [
      {
        q: "直徑 24 公分的大披薩售價 400 元，直徑 12 公分的小披薩售價 150 元。買哪一種在面積上比較划算（每平方公分單價較低）？",
        options: ["直徑 24 公分的大披薩比較划算", "直徑 12 公分的小披薩比較划算", "兩種一樣划算", "無法比較"],
        ans: "直徑 24 公分的大披薩比較划算",
        explain: "大披薩半徑是小披薩的 2 倍，面積是 4 倍（大披薩面積相當於 4 個小披薩）。4 個小披薩要 150×4 = 600 元，而大披薩只要 400 元，因此大披薩划算得多！"
      }
    ]
  },

  // Quest 5: 全校通勤比率 (第5單元)
  {
    title: "Quest 5：全校學生通勤方式大調查 (比和比值)",
    icon: "🚌",
    concept: `
      <strong>生活情境探究・星海高中通勤統計（課本素養 P5）：</strong><br>
      全校調查：搭乘校車 240 人、走路 180 人、家長接送 300 人、騎腳踏車 80 人，合計 800 人。<br>
      • <strong>走路人數對搭校車人數的比：</strong>180：240 ＝ (180÷60)：(240÷60) ＝ <strong>3：4</strong>，比值是 <strong>3/4 (0.75)</strong>。<br>
      • <strong>搭校車人數對全校人數的比值：</strong>240 ÷ 800 ＝ 24/80 ＝ <strong>3/10 (0.3)</strong>，代表佔全校 30%！
    `,
    quizzes: [
      {
        q: "走路學生有 180 人，搭校車學生有 240 人。「走路人數對搭校車人數」的最簡整數比與比值為何？",
        options: ["最簡整數比 3：4，比值 3/4", "最簡整數比 4：3，比值 4/3", "最簡整數比 9：12，比值 0.75", "最簡整數比 3：4，比值 4/3"],
        ans: "最簡整數比 3：4，比值 3/4",
        explain: "180：240 同除以 60 得到最簡整數比 3：4，比值 = 3 ÷ 4 = 3/4。"
      }
    ]
  },

  // Quest 6: 半月湖步道 (第6單元)
  {
    title: "Quest 6：半月湖運動手環跑道 (扇形周長與弧長)",
    icon: "⌚",
    concept: `
      <strong>生活情境探究・半月形水岸步道（課本素養 P6）：</strong><br>
      半月湖呈現半圓形（1/2 圓），直徑為 1000 公尺（半徑 500 公尺）：<br>
      • <strong>半圓圓弧步道長度：</strong>1000 × 3.14 ÷ 2 ＝ <strong>1570 公尺</strong>。<br>
      • <strong>慢跑環繞半月湖一圈總長度（周長）：</strong><br>
        半圓弧長 ＋ 直徑 ＝ 1570 ＋ 1000 ＝ <strong>2570 公尺（約 2.57 公里）</strong>！
    `,
    quizzes: [
      {
        q: "半月湖是半徑 500 公尺（直徑 1000 公尺）的半圓形。沿著半月湖外圍完整慢跑一圈，總跑步距離大約是多少公尺？",
        options: ["2570 公尺", "1570 公尺", "3140 公尺", "2070 公尺"],
        ans: "2570 公尺",
        explain: "半圓弧長 = 1000 × 3.14 ÷ 2 = 1570 公尺。周長 = 弧長 + 直徑 = 1570 + 1000 = 2570 公尺。"
      }
    ]
  },

  // Quest 7: 低碳減碳行 (第7單元)
  {
    title: "Quest 7：節能減碳綠活鐵馬行 (速率與通勤)",
    icon: "🚲",
    concept: `
      <strong>生活情境探究・綠色單車通勤（課本素養 P7）：</strong><br>
      尤白可公司離家 5 公里，每天騎腳踏車通勤健身，花費 20 分鐘抵達：<br>
      • <strong>平均分速：</strong>5 公里 ＝ 5000 公尺。分速 ＝ 5000 ÷ 20 ＝ <strong>250 公尺/分</strong>。<br>
      • <strong>平均時速：</strong>250 × 60 ＝ 15000 公尺/時 ＝ <strong>15 公里/時</strong>。<br>
      • <strong>前往 9 公里外的景點：</strong>9 公里 ＝ 9000 公尺。時間 ＝ 9000 ÷ 250 ＝ <strong>36 分鐘</strong>！
    `,
    quizzes: [
      {
        q: "尤白可騎腳踏車 20 分鐘騎了 5 公里。按照相同速率，他要騎到 9 公里外的目的地，最少需要幾分鐘？",
        options: ["36 分鐘", "30 分鐘", "45 分鐘", "40 分鐘"],
        ans: "36 分鐘",
        explain: "分速 = 5000 ÷ 20 = 250 公尺/分。9000 ÷ 250 = 36 分鐘。"
      }
    ]
  },

  // Quest 8: 建築立體積木 (第8單元)
  {
    title: "Quest 8：建築大師的立體積木塔 (數量關係規律)",
    icon: "🧱",
    concept: `
      <strong>生活情境探究・積木幾何規律（課本素養 P8）：</strong><br>
      建築師搭建積木立體模型：<br>
      • 第 1 層有 1 個積木<br>
      • 第 2 層有 1 ＋ 3 ＝ 4 個積木<br>
      • 第 3 層有 4 ＋ 5 ＝ 9 個積木<br>
      • <strong>發現規律：</strong>第 n 層的積木總塊數等於 <strong>n × n (n²)</strong>！<br>
      如果搭到第 10 層，第 10 層共有 10 × 10 ＝ <strong>100 個積木</strong>！
    `,
    quizzes: [
      {
        q: "觀察積木排列規律：第 1 層 1 塊、第 2 層 4 塊、第 3 層 9 塊...如果依此規律搭到第 10 層，第 10 層共有幾塊積木？",
        options: ["100 塊", "81 塊", "121 塊", "55 塊"],
        ans: "100 塊",
        explain: "每層積木數為平方數：1²=1, 2²=4, 3²=9...因此第 10 層 = 10² = 100 塊。"
      }
    ]
  }
];

const glossaryTerms = [
  { term: "數學素養 (Mathematical Literacy)", def: "運用數學知識、思維與技能，在日常生活、科技與科學等真實情境中提出、分析並解決問題的能力。" },
  { term: "身體質量指數 BMI", def: "國際衡量健康體位標準。公式：體重 (kg) ÷ 身高 (m)²。健康範圍為 18.5 至 24。" },
  { term: "性價比 CP 值", def: "單位成本所能獲得的效能或面積。在食品選購時為「面積 ÷ 售價」或「售價 ÷ 面積」。" },
  { term: "低碳通勤減碳量", def: "利用步行或自行車替代機動車輛，依里程與速率計算出行時間與綠色效益。" }
];

function renderStage(stageIdx) {
  currentStage = stageIdx;
  const container = document.getElementById('stageContainer');
  const tabs = document.querySelectorAll('.stage-tab');
  tabs.forEach((tab, i) => {
    tab.classList.toggle('active', i === stageIdx);
  });

  const data = stageData[stageIdx];
  if (!data) return;

  let html = `
    <div class="section-card">
      <div class="card-header">
        <h2 class="card-title">
          <span>${data.icon}</span>
          <span>${data.title}</span>
        </h2>
        <span class="badge-tag">Quest ${stageIdx + 1} / 8</span>
      </div>

      <div class="concept-box">
        ${data.concept}
      </div>
  `;

  if (data.hasBmiLab) {
    html += `
      <div class="lab-widget">
        <h3 style="margin-bottom:12px; color:var(--primary-dark); display:flex; align-items:center; gap:8px;">
          <span>🏃</span><span>即時健康 BMI 計算儀 (小數除法探究)</span>
        </h3>
        <div class="slider-row">
          <label>
            <span>身高 (公分)</span>
            <span id="bmiHeightVal" style="color:var(--primary); font-weight:800;">150 公分 (1.50 公尺)</span>
          </label>
          <input type="range" id="bmiHeightSlider" min="120" max="185" value="150" oninput="updateBmiLab()">
        </div>
        <div class="slider-row">
          <label>
            <span>體重 (公斤)</span>
            <span id="bmiWeightVal" style="color:#D97706; font-weight:800;">55 公斤</span>
          </label>
          <input type="range" id="bmiWeightSlider" min="30" max="90" value="55" oninput="updateBmiLab()">
        </div>
        <div class="lab-metrics">
          <div class="metrics-line" id="metricBmiResult">BMI ＝ 55 ÷ (1.5 × 1.5) ＝ 24.4 (四捨五入)</div>
          <div style="font-size:0.95rem; font-weight:700;" id="metricBmiStatus">
            體位判定：⚠️ 輕度過重（衛福部建議健康體位 18.5 ~ 24）
          </div>
        </div>
      </div>
    `;
  }

  html += `
      <h3 style="margin:24px 0 10px; color:var(--text-main); display:flex; align-items:center; gap:8px;">
        <span>✏️</span><span>素養探究測驗 (選項自動隨機化)</span>
      </h3>
      <div class="quiz-list" id="stageQuizList">
  `;

  data.quizzes.forEach((quiz, qIdx) => {
    const shuffledOptions = shuffleArray(quiz.options);
    html += `
      <div class="quiz-item" id="quizCard_${stageIdx}_${qIdx}">
        <div class="quiz-header">
          <span class="quiz-qnum">題目 ${qIdx + 1}</span>
          <div class="quiz-text">${quiz.q}</div>
        </div>
        <div class="quiz-options">
          ${shuffledOptions.map(opt => `
            <button class="quiz-opt-btn" onclick="checkAnswer(${stageIdx}, ${qIdx}, this, '${encodeURIComponent(opt)}', '${encodeURIComponent(quiz.ans)}')">
              ${opt}
            </button>
          `).join('')}
        </div>
        <div class="quiz-explain" id="explain_${stageIdx}_${qIdx}">
          <strong>💡 詳解分析：</strong> ${quiz.explain}
        </div>
      </div>
    `;
  });

  html += `
      </div>
      <div class="card-footer">
        <button class="back-btn" onclick="prevStage()">⬅️ 上一關</button>
        <button class="btn-next-stage" onclick="nextStage()">
          ${stageIdx === 7 ? '領取素養冒險王認證 🌟' : '挑戰下個素養任務 ➡️'}
        </button>
      </div>
    </div>
  `;

  container.innerHTML = html;
  window.scrollTo({ top: 180, behavior: 'smooth' });

  if (data.hasBmiLab) {
    updateBmiLab();
  }
}

function updateBmiLab() {
  const hCm = parseFloat(document.getElementById('bmiHeightSlider').value);
  const wKg = parseFloat(document.getElementById('bmiWeightSlider').value);
  const hM = hCm / 100;

  document.getElementById('bmiHeightVal').textContent = `${hCm} 公分 (${hM.toFixed(2)} 公尺)`;
  document.getElementById('bmiWeightVal').textContent = `${wKg} 公斤`;

  const bmi = wKg / (hM * hM);
  const bmiRound = bmi.toFixed(1);

  let status = '🌟 健康體位 (標準)';
  let color = '#059669';
  if (bmi < 18.5) {
    status = '⚠️ 體重過輕，多補充均衡營養';
    color = '#2563EB';
  } else if (bmi >= 24 && bmi < 27) {
    status = '⚠️ 輕度過重，增加戶外運動';
    color = '#D97706';
  } else if (bmi >= 27) {
    status = '⚠️ 中度或重度肥胖，需健康管理';
    color = '#DC2626';
  }

  document.getElementById('metricBmiResult').textContent = 
    `BMI ＝ ${wKg} ÷ (${hM.toFixed(2)} × ${hM.toFixed(2)}) ＝ ${bmiRound}`;
  const statusEl = document.getElementById('metricBmiStatus');
  statusEl.textContent = `體位判定：${status}（衛福部標準：18.5 ≤ 健康體位 ＜ 24）`;
  statusEl.style.color = color;
}

function checkAnswer(stageIdx, qIdx, btn, encodedSelected, encodedCorrect) {
  const selected = decodeURIComponent(encodedSelected);
  const correct = decodeURIComponent(encodedCorrect);
  const card = document.getElementById(`quizCard_${stageIdx}_${qIdx}`);
  const explain = document.getElementById(`explain_${stageIdx}_${qIdx}`);
  const allBtns = card.querySelectorAll('.quiz-opt-btn');

  allBtns.forEach(b => {
    b.disabled = true;
    if (decodeURIComponent(b.getAttribute('onclick').split("'")[7]) === correct) {
      b.classList.add('correct-opt');
    }
  });

  if (selected === correct) {
    btn.classList.add('correct-opt');
    card.classList.add('correct-item');
    playSound('correct');
    addScore(10);
    updateMascot('🎯 太棒了！素養思維完全到位！');
  } else {
    btn.classList.add('wrong-opt');
    card.classList.add('wrong-item');
    playSound('wrong');
    resetCombo();
    updateMascot('💡 沒關係，仔細看看生活詳解，馬上融會貫通！');
  }

  explain.style.display = 'block';
}

function gotoStage(idx) {
  playSound('click');
  renderStage(idx);
}

function nextStage() {
  if (currentStage < 7) {
    playSound('level_clear');
    if (typeof confetti === 'function') {
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.8 } });
    }
    renderStage(currentStage + 1);
  } else {
    renderFinal();
  }
}

function prevStage() {
  if (currentStage > 0) {
    playSound('click');
    renderStage(currentStage - 1);
  } else {
    showCastleModal('提示', '已經是第一個任務囉！', '🏰');
  }
}

function renderFinal() {
  playSound('level_clear');
  if (typeof confetti === 'function') {
    confetti({ particleCount: 160, spread: 100, origin: { y: 0.6 } });
  }
  const container = document.getElementById('stageContainer');
  const tabs = document.querySelectorAll('.stage-tab');
  tabs.forEach(t => t.classList.remove('active'));

  container.innerHTML = `
    <div class="section-card badge-showcase">
      <div class="medal-icon">🌟</div>
      <h2 style="font-size:2rem; font-weight:900; color:var(--primary-dark); margin-bottom:12px;">
        恭喜榮獲【6上全能數學素養冒險王】榮譽認證！
      </h2>
      <p style="font-size:1.15rem; color:var(--text-muted); max-width:620px; margin:0 auto 24px;">
        你已成功破譯畢業旅行分組、烘焙配方、BMI 健康體位、披薩性價比、全校通勤統計、半月湖水岸步道、低碳減碳與建築積木規律！真正做到了學以致用、用數學改變生活！
      </p>
      <div style="display:flex; justify-content:center; gap:16px; margin-bottom:28px;">
        <div class="stat-pill" style="font-size:1.1rem; padding:8px 20px;">
          <span>⭐ 最終總得分：</span><strong style="color:#B45309;">${userScore} 分</strong>
        </div>
      </div>
      <div style="display:flex; justify-content:center; gap:16px;">
        <button class="btn-next-stage" onclick="gotoStage(0)">🔄 再次挑戰複習</button>
        <a href="portal.html" class="back-btn" style="padding:10px 24px; font-size:1.05rem;">🏰 返回傳送門</a>
      </div>
    </div>
  `;
  window.scrollTo({ top: 180, behavior: 'smooth' });
}

function openGlossary() {
  playSound('click');
  let body = '<div style="display:flex; flex-direction:column; gap:14px;">';
  glossaryTerms.forEach(t => {
    body += `
      <div style="background:#ECFDF5; border-left:4px solid var(--primary); padding:10px 14px; border-radius:0 8px 8px 0;">
        <div style="font-weight:800; color:var(--primary-dark); margin-bottom:4px;">${t.term}</div>
        <div style="font-size:0.95rem; color:#334155;">${t.def}</div>
      </div>
    `;
  });
  body += '</div>';
  showCastleModal('跨領域素養・核心知識寶典', body, '📖');
}

document.addEventListener('DOMContentLoaded', () => {
  renderStage(0);
});
</script>
</body>
</html>
'''

with open('math6_competency.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated math6_competency.html (size: {len(html_content)} chars)")

