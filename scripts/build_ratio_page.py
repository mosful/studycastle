# -*- coding: utf-8 -*-
"""
生成 ratio.html - 國小六年級數學第 5 單元「比和比值」現代化互動學習頁面
"""

import os
import json

html_content = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>土耳其棉堡奇境：比與比值大冒險 ⑤ 6上數學 第5單元 | 學習城堡</title>
<!-- Favicon 網站圖示 -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="apple-touch-icon" href="favicon.svg">
<meta name="description" content="國小 6 年級上學期數學第 5 單元：比和比值。從土耳其棉堡與道地紅茶調配出發，精通比的意義、前項後項、比值計算、相等的比、最簡單整數比、按比分配生活應用與資優挑戰題！">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Fredoka:wght@600;700&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="study-castle-ui.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/canvas-confetti/1.9.2/confetti.browser.min.js"></script>

<style>
  :root {
    --primary: #0D9488;
    --primary-light: #14B8A6;
    --primary-dark: #0F766E;
    --accent: #F59E0B;
    --accent-gold: #D97706;
    --bg-gradient: linear-gradient(135deg, #F0FDFA 0%, #E0F2FE 50%, #EFF6FF 100%);
    --card-bg: rgba(255, 255, 255, 0.95);
    --card-shadow: 0 10px 25px -5px rgba(13, 148, 136, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
    --border-color: #CCFBF1;
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

  /* 頂部導覽列 */
  .top-navbar {
    background: rgba(255, 255, 255, 0.92);
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
    background: #CCFBF1;
    color: var(--primary-dark);
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 800;
    border: 1px solid #99F6E4;
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

  /* 英雄主視覺 */
  .hero-container {
    max-width: 1040px;
    margin: 24px auto 16px;
    padding: 0 16px;
  }
  .hero-banner {
    background: linear-gradient(135deg, #0F766E 0%, #0D9488 60%, #14B8A6 100%);
    color: #FFFFFF;
    border-radius: var(--radius-lg);
    padding: 32px 28px;
    box-shadow: 0 12px 30px rgba(13, 148, 136, 0.25);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    position: relative;
    overflow: hidden;
  }
  .hero-banner::after {
    content: "☕🇹🇷⚖️";
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
    color: #CCFBF1;
    max-width: 600px;
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

  /* 關卡選單 Tabs */
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
    min-width: 140px;
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--radius-md);
    padding: 12px 10px;
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
    background: #F0FDFA;
    border-color: var(--primary);
    box-shadow: 0 4px 12px rgba(13, 148, 136, 0.15);
  }
  .stage-tab-num {
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--primary-dark);
    text-transform: uppercase;
    display: block;
    margin-bottom: 2px;
  }
  .stage-tab-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-main);
  }

  /* 主內容容器 */
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

  /* 互動茶飲實驗室 */
  .lab-widget {
    background: #FFFFFF;
    border: 2px dashed #99F6E4;
    border-radius: var(--radius-lg);
    padding: 24px;
    margin: 20px 0;
  }
  .tea-sim-container {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    align-items: center;
    justify-content: center;
  }
  .cup-visual-wrap {
    width: 140px;
    height: 200px;
    position: relative;
    border-bottom: 8px solid #94A3B8;
    border-left: 5px solid #CBD5E1;
    border-right: 5px solid #CBD5E1;
    border-radius: 0 0 35px 35px;
    overflow: hidden;
    background: rgba(248, 250, 252, 0.6);
    box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
  }
  .tea-liquid {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    transition: all 0.4s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFF;
    font-weight: 800;
    font-size: 0.9rem;
    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
  }
  .tea-controls {
    flex: 1;
    min-width: 280px;
  }
  .slider-row {
    margin-bottom: 16px;
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
  .tea-metrics {
    background: #F0FDFA;
    border-radius: var(--radius-md);
    padding: 14px 18px;
    margin-top: 14px;
    border: 1px solid #CCFBF1;
  }
  .metrics-line {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 4px;
    color: var(--primary-dark);
  }

  /* 最簡比天平工具 */
  .balance-widget {
    background: #F8FAFC;
    border-radius: var(--radius-lg);
    padding: 22px;
    border: 1px solid #E2E8F0;
    margin: 20px 0;
  }
  .balance-inputs {
    display: flex;
    gap: 12px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 16px;
  }
  .balance-input {
    width: 120px;
    padding: 10px 14px;
    border: 2px solid #CBD5E1;
    border-radius: var(--radius-md);
    font-size: 1.1rem;
    font-weight: 700;
    text-align: center;
    outline: none;
    transition: all 0.2s;
  }
  .balance-input:focus {
    border-color: var(--primary);
    background: #FFF;
    box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.15);
  }
  .balance-colon {
    font-size: 1.8rem;
    font-weight: 900;
    color: var(--primary-dark);
  }
  .btn-calc {
    background: var(--primary);
    color: #FFF;
    border: none;
    padding: 10px 22px;
    border-radius: var(--radius-md);
    font-weight: 800;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-calc:hover {
    background: var(--primary-dark);
    transform: translateY(-2px);
  }
  .balance-result {
    background: #FFF;
    border: 2px solid #CCFBF1;
    border-radius: var(--radius-md);
    padding: 16px;
    font-size: 1.05rem;
    line-height: 1.7;
    display: none;
  }

  /* 測驗題目卡片 */
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

  /* 底部按鈕區 */
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
    box-shadow: 0 4px 12px rgba(13, 148, 136, 0.2);
  }
  .btn-next-stage:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(13, 148, 136, 0.3);
  }

  /* 榮譽殿堂 Final 頁 */
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

  /* 彈窗樣式 */
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

  /* 響應式優化 */
  @media (max-width: 768px) {
    .hero-content h1 { font-size: 1.6rem; }
    .hero-banner { padding: 22px 18px; }
    .section-card { padding: 18px; }
    .quiz-options { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<!-- 頂部導覽列 -->
<header class="top-navbar">
  <div class="nav-left">
    <a href="portal.html" class="back-btn">
      <span>🏰 返回傳送門</span>
    </a>
    <div class="nav-brand">
      <span>🇹🇷 比和比值奇境</span>
      <span class="badge-tag">6上 第⑤單元</span>
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
    <button class="btn-icon" onclick="openGlossary()" title="知識辭典">📖</button>
    <button class="btn-icon" id="soundBtn" onclick="toggleSound()" title="音效切換">🔊</button>
  </div>
</header>

<!-- 主視覺橫幅 -->
<section class="hero-container">
  <div class="hero-banner">
    <div class="hero-content">
      <h1>土耳其棉堡奇境：比與比值大冒險</h1>
      <p>跟著探險家穿越白色石灰岩古城與土耳其茶坊，掌握比的意義、前項後項、比值計算、最簡整數比、比例式與按比分配！</p>
    </div>
    <div class="hero-mascot">
      <div class="mascot-avatar">🦉</div>
      <div class="mascot-bubble" id="mascotMessage">歡迎來到比和比值的國度！準備好接受挑戰了嗎？</div>
    </div>
  </div>
</section>

<!-- 關卡導航 Tabs -->
<nav class="stage-nav" id="stageTabs">
  <div class="stage-tab active" onclick="gotoStage(0)">
    <span class="stage-tab-num">Stage 0</span>
    <span class="stage-tab-title">棉堡前哨站</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(1)">
    <span class="stage-tab-num">Stage 1</span>
    <span class="stage-tab-title">比的奧秘</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(2)">
    <span class="stage-tab-num">Stage 2</span>
    <span class="stage-tab-title">比值的神力</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(3)">
    <span class="stage-tab-num">Stage 3</span>
    <span class="stage-tab-title">相等的比與最簡比</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(4)">
    <span class="stage-tab-num">Stage 4</span>
    <span class="stage-tab-title">比例應用與分配</span>
  </div>
  <div class="stage-tab" onclick="gotoStage(5)">
    <span class="stage-tab-num">Stage 5</span>
    <span class="stage-tab-title">大會考與資優殿堂</span>
  </div>
</nav>

<!-- 主內容卡片區域 -->
<main class="main-container" id="stageContainer">
  <!-- 動態渲染各關卡內容 -->
</main>

<!-- 現代通用彈窗 Modal -->
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
      <!-- 內容動態填充 -->
    </div>
  </div>
</div>

<script>
// ── Web Audio API 音效引擎 ──
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

// ── 現代彈窗控制 (CastleModal) ──
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

// 防禦性覆蓋原生 alert
window.alert = function(msg) {
  showCastleModal('系統提示', `<div style="text-align:left; white-space:pre-line;">${msg}</div>`, '💡');
};

// ── 連擊與分數狀態 ──
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
    updateMascot(`🔥 哇！太強了！達成 ${userCombo} 連擊！額外加 ${bonus} 分！`);
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

// ── 題庫資料結構與洗牌演算法 (Fisher-Yates) ──
function shuffleArray(arr) {
  const newArr = [...arr];
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]];
  }
  return newArr;
}

// ── 各關卡資料結構 ──
const stageData = [
  // Stage 0: 暖身與世界遺產
  {
    title: "棉堡奇境前哨站：世界遺產與最簡分數",
    icon: "🇹🇷",
    concept: `
      <strong>從數學看世界・土耳其棉堡 (Pamukkale)：</strong><br>
      棉堡位於土耳其西南代尼茲利省，以如雪白城堡般的石灰岩階梯溶洞聞名，山頂坐落著希拉波利斯古城 (Hierapolis)，西元1988年被列為世界遺產！<br>
      溫泉水富含碳酸鹽礦物，源頭溫泉水每公升含有 <strong>12/10 公克</strong> 的二氧化碳。以前學過的最簡分數：<br>
      • <strong>約分</strong>：分子與分母同除以最大公因數 2，得到最簡分數 <strong>6/5</strong>（或 1又1/5）。<br>
      • <strong>擴分</strong>：分子與分母同乘以相同數，分數值不變。<br>
      • <strong>通分</strong>：化成相同分母，方便比較大小與加減計算。
    `,
    quizzes: [
      {
        q: "棉堡溫泉水每公升含二氧化碳 12/10 公克，化為「最簡分數」是多少？",
        options: ["6/5 (或 1又1/5)", "3/2", "12/10", "24/20"],
        ans: "6/5 (或 1又1/5)",
        explain: "12 與 10 的最大公因數是 2，分子分母同除以 2：(12÷2)/(10÷2) = 6/5。"
      },
      {
        q: "將分數 48/72 化為最簡分數是多少？",
        options: ["2/3", "4/6", "12/18", "3/4"],
        ans: "2/3",
        explain: "48 與 72 的最大公因數是 24：(48÷24)/(72÷24) = 2/3。"
      },
      {
        q: "比較 6/15 與 14/30 的大小，正確結果為何？",
        options: ["6/15 < 14/30", "6/15 > 14/30", "6/15 = 14/30", "無法比較"],
        ans: "6/15 < 14/30",
        explain: "通分分母為 30：6/15 = 12/30。因為 12/30 < 14/30，所以 6/15 < 14/30。"
      }
    ]
  },

  // Stage 1: 比的意義 (5-1)
  {
    title: "第一關：比的奧秘與生活記法 (5-1 比)",
    icon: "☕",
    concept: `
      <strong>1. 比的意義：</strong>在數學中，用來表示<strong>兩個數量的倍數關係</strong>稱為「比」。<br>
      <strong>2. 比的記法與讀法：</strong>以符號「<strong>：</strong>」記錄，讀作「比」。例如 1 杯濃茶對 2 杯開水，記作 <strong>1：2</strong>，讀作「一比二」。<br>
      <strong>3. 前項與後項：</strong>在 <strong>a：b</strong> 中，符號前面的 a 稱為「<strong>前項</strong>」，後面的 b 稱為「<strong>後項</strong>」。<br>
      ⚠️ <strong>重要提醒：</strong>比的前後順序代表不同的關係，不能隨便顛倒！濃茶對開水是 1：2，開水對濃茶則是 2：1。
    `,
    hasTeaLab: true,
    quizzes: [
      {
        q: "道地的土耳其紅茶是用 1 杯濃茶和 2 杯開水調配而成。「濃茶杯數對開水杯數」的比記作什麼？",
        options: ["1：2", "2：1", "1/2", "3：1"],
        ans: "1：2",
        explain: "濃茶是 1 杯（前項），開水是 2 杯（後項），比記作 1：2。"
      },
      {
        q: "花瓶裡有 5 朵百合花和 8 朵康乃馨，請問「百合花數量對康乃馨數量」的比，前項與後項分別是多少？",
        options: ["前項是 5，後項是 8", "前項是 8，後項是 5", "前項是 5，後項是 13", "前項是 13，後項是 8"],
        ans: "前項是 5，後項是 8",
        explain: "百合花對康乃馨的比記為 5：8，冒號前面的 5 是前項，後面的 8 是後項。"
      },
      {
        q: "承上題，若改問「康乃馨數量對百合花數量」的比，應該怎麼記？",
        options: ["8：5", "5：8", "8：13", "5：13"],
        ans: "8：5",
        explain: "題目問的是「康乃馨對百合」，因此康乃馨數量 8 為前項，百合數量 5 為後項，記作 8：5。"
      },
      {
        q: "正方形甲邊長 6 公分，正方形乙邊長 4 公分，甲邊長對乙邊長的比怎麼記？讀作什麼？",
        options: ["6：4，讀作六比四", "4：6，讀作四比六", "6：4，讀作六除以四", "36：16，讀作三十六比十六"],
        ans: "6：4，讀作六比四",
        explain: "邊長比直接記錄為 6：4，讀作「六比四」。"
      }
    ]
  },

  // Stage 2: 比值 (5-2)
  {
    title: "第二關：比值的神力 (5-2 比值)",
    icon: "🧮",
    concept: `
      <strong>1. 什麼是比值？</strong><br>
      比的前項除以後項所得的商，稱為「<strong>比值</strong>」。<br>
      <div class="concept-highlight" style="display:inline-block; margin: 6px 0; font-size:1.1rem;">比值 ＝ 前項 ÷ 後項 ＝ 前項 / 後項</div><br>
      <strong>2. 比值的表示形式：</strong>比值可以是<strong>整數</strong>、<strong>最簡分數</strong>或<strong>小數</strong>。<br>
      • 4：1 的比值 ＝ 4 ÷ 1 ＝ 4（整數）<br>
      • 5：8 的比值 ＝ 5 ÷ 8 ＝ 5/8 或 0.625（分數或小數）<br>
      • 39 元買 5 包泡麵，價錢對包數的比值 ＝ 39 ÷ 5 ＝ 7.8（代表每包 7.8 元）<br>
      ⚠️ <strong>關鍵規則：</strong>在比 a：b 中，後項 b 不可以是 0，因為 0 不能當除數！
    `,
    quizzes: [
      {
        q: "一盒原子筆有 4 枝藍筆和 1 枝紅筆，藍筆枝數對紅筆枝數的比是 4：1，比值是多少？",
        options: ["4", "1/4", "0.25", "5"],
        ans: "4",
        explain: "比值 = 前項 ÷ 後項 = 4 ÷ 1 = 4。"
      },
      {
        q: "超商特價活動，5 包泡麵賣 39 元。「泡麵價錢對包數」的比值是多少？代表什麼意思？",
        options: ["7.8（代表平均每包 7.8 元）", "5/39（代表每元買幾包）", "34", "195"],
        ans: "7.8（代表平均每包 7.8 元）",
        explain: "價錢對包數比為 39：5，比值 = 39 ÷ 5 = 39/5 = 7.8，單位是元/包。"
      },
      {
        q: "每 2 公斤的廢電池可以換 32 元購物抵用金。「廢電池重量對購物金」的比值是多少？",
        options: ["1/16", "16", "2/30", "64"],
        ans: "1/16",
        explain: "重量對購物金比為 2：32，比值 = 2 ÷ 32 = 2/32 = 1/16。"
      },
      {
        q: "全校共有 1200 人，女生有 720 人。請問「女生人數對全校人數」的比值化為最簡分數是多少？",
        options: ["3/5", "5/3", "6/10", "0.6 人"],
        ans: "3/5",
        explain: "比為 720：1200，比值 = 720/1200 = 72/120 = 3/5（或小數 0.6）。比值是倍數關係，不帶單位。"
      }
    ]
  },

  // Stage 3: 相等的比與最簡單整數比 (5-3)
  {
    title: "第三關：相等的比與最簡單整數比 (5-3)",
    icon: "⚖️",
    concept: `
      <strong>1. 相等的比：</strong>當兩個比的<strong>比值相等</strong>時，這兩個比就是「相等的比」，記作 <strong>a：b ＝ c：d</strong>。<br>
      • <strong>重要性質：</strong>比的前項與後項「同乘以」或「同除以」一個<strong>不等於 0</strong> 的數，其比值不變！<br>
      • 例如檸檬水 1：3（1杯原汁加3杯水），若調 2 杯原汁加 6 杯水（2：6），酸度完全一樣（比值皆為 1/3）！<br>
      <strong>2. 最簡單整數比：</strong><br>
      前項和後項都是<strong>整數</strong>，且<strong>前項與後項互質</strong>（最大公因數為 1）的比，稱為「最簡單整數比」。<br>
      <strong>3. 三種化簡秘笈：</strong><br>
      • <strong>整數比：</strong>同除以最大公因數。例：12：18 ＝ (12÷6)：(18÷6) ＝ 2：3。<br>
      • <strong>小數比：</strong>同乘 10、100...變成整數後約分。例：0.8：1.2 ＝ 8：12 ＝ 2：3。<br>
      • <strong>分數比：</strong>同乘分母最小公倍數 (LCM)。例：2/3：4/5 ＝ (2/3×15)：(4/5×15) ＝ 10：12 ＝ 5：6。
    `,
    hasBalanceTool: true,
    quizzes: [
      {
        q: "將比「12：18」化為最簡單整數比，結果為何？",
        options: ["2：3", "4：6", "6：9", "1：1.5"],
        ans: "2：3",
        explain: "12 與 18 的最大公因數是 6，兩項同除以 6 得到最簡單整數比 2：3。"
      },
      {
        q: "將小數比「9.6：8.4」化為最簡單整數比是多少？",
        options: ["8：7", "16：14", "96：84", "4：3"],
        ans: "8：7",
        explain: "先同乘 10 化為整數 96：84，兩數最大公因數是 12，(96÷12)：(84÷12) = 8：7。"
      },
      {
        q: "將帶分數比「1又3/7：2又5/8」化為最簡單整數比是多少？",
        options: ["80：147", "10：21", "24：35", "56：80"],
        ans: "80：147",
        explain: "化為假分數 10/7：21/8，分母 7 與 8 的最小公倍數是 56。同乘 56：(10/7×56)：(21/8×56) = 80：147。"
      },
      {
        q: "下面哪一組比與「48：60」是相等的比，且屬於「最簡單整數比」？",
        options: ["4：5", "24：30", "4.8：6", "12：15"],
        ans: "4：5",
        explain: "48 與 60 最大公因數是 12，(48÷12)：(60÷12) = 4：5。4 和 5 互質，是最簡單整數比。"
      }
    ]
  },

  // Stage 4: 比的應用 (5-4)
  {
    title: "第四關：比的應用與按比分配 (5-4)",
    icon: "🎯",
    concept: `
      <strong>1. 比例式求未知數：</strong>利用「比值相等」或「前後項同乘同除的倍數」來解題。<br>
      • 例如：3：5 ＝ 12：□。<br>
      前項 3 變成 12 是乘以 4（12 ÷ 3 ＝ 4），所以後項 □ ＝ 5 × 4 ＝ 20。<br>
      <strong>2. 按比分配（總量分配問題）：</strong><br>
      若把總量依 <strong>a：b</strong> 的比例分配給甲和乙：<br>
      • 總份數 ＝ a ＋ b<br>
      • 甲所佔部分 ＝ 總量 × a / (a + b)<br>
      • 乙所佔部分 ＝ 總量 × b / (a + b)<br>
      • <strong>例題：</strong>養蝦池有草蝦和大白蝦共 1600 隻，數量比是 5：11。<br>
        總份數 ＝ 5 ＋ 11 ＝ 16 份。草蝦 ＝ 1600 × 5/16 ＝ 500 隻；大白蝦 ＝ 1600 × 11/16 ＝ 1100 隻。
    `,
    quizzes: [
      {
        q: "比例式計算：□：800 ＝ 5：20，請問 □ 是多少？",
        options: ["200", "160", "400", "250"],
        ans: "200",
        explain: "後項 800 ÷ 20 = 40 倍，因此前項 □ = 5 × 40 = 200。"
      },
      {
        q: "國旗的寬對長的比是 (2/3)：1。如果國旗的寬是 60 公分，長是幾公分？",
        options: ["90 公分", "40 公分", "80 公分", "100 公分"],
        ans: "90 公分",
        explain: "(2/3)：1 = 60：長。長 = 60 ÷ (2/3) × 1 = 60 × (3/2) = 90 公分。"
      },
      {
        q: "柳丁和蘋果共有 54 個，全部個數對蘋果個數的比是 9：7。請問柳丁和蘋果各有幾個？",
        options: ["柳丁 12 個，蘋果 42 個", "柳丁 14 個，蘋果 40 個", "柳丁 7 個，蘋果 47 個", "柳丁 18 個，蘋果 36 個"],
        ans: "柳丁 12 個，蘋果 42 個",
        explain: "全部 54 個，9：7 = 54：蘋果，54 ÷ 9 = 6 倍，蘋果 = 7 × 6 = 42 個。柳丁 = 54 - 42 = 12 個。"
      },
      {
        q: "繩子一條長 35 公分，按照 3：4 的比剪成兩段，較長的那一段繩子長幾公分？",
        options: ["20 公分", "15 公分", "25 公分", "18 公分"],
        ans: "20 公分",
        explain: "總份數 = 3 + 4 = 7 份。每份 = 35 ÷ 7 = 5 公分。較長一段為 4 份：5 × 4 = 20 公分（較短為 15 公分）。"
      }
    ]
  },

  // Stage 5: 大會考與資優挑戰 (課本練習 5 + 學力檢測 + 資優題)
  {
    title: "第五關：城堡大會考與資優殿堂 (練習 5 全攻略)",
    icon: "🏆",
    concept: `
      <strong>本關整合課本 P80~P81 練習 5 精選考題、學力檢測題與資優思維挑戰：</strong><br>
      • <strong>幾何倍數概念：</strong>邊長比為 a：b 時，周長比亦為 a：b，而面積比為 a²：b²！<br>
      • <strong>學力檢測關鍵：</strong>圓周長 ＝ 直徑 × 3.14 ＝ 半徑 × 2 × 3.14。因此「圓周長：半徑」的比值恆為 2 × 3.14 ＝ <strong>6.28</strong>！<br>
      • <strong>資優邏輯推理：</strong>透過聯立比例關係，找出大人與小孩食量的倍數轉換，迎刃而解！
    `,
    quizzes: [
      {
        q: "【幾何觀念】正方形甲邊長 6m，正方形乙邊長 4m。請問「甲面積對乙面積」的比化為最簡單整數比是多少？",
        options: ["9：4", "3：2", "6：4", "36：16"],
        ans: "9：4",
        explain: "甲面積 = 6×6 = 36；乙面積 = 4×4 = 16。面積比 36：16 = (36÷4)：(16÷4) = 9：4。"
      },
      {
        q: "【113 學力檢測】六年甲班有 24 位學生，有 7/8 的學生數學考試及格。請問「及格人數對不及格人數」的最簡整數比為何？",
        options: ["7：1", "7：8", "8：1", "8：7"],
        ans: "7：1",
        explain: "及格佔 7 份，則不及格佔 1 - 7/8 = 1/8 份（1 份）。及格人數對不及格人數比直接為 7：1。"
      },
      {
        q: "【113 學力檢測】有一個半徑 50 公分的圓，圓周長對半徑的比值是多少？（圓周率以 3.14 計算）",
        options: ["6.28", "3.14", "2", "1.57"],
        ans: "6.28",
        explain: "圓周長 = 半徑 × 2 × 3.14。圓周長 ÷ 半徑 = 2 × 3.14 = 6.28。"
      },
      {
        q: "【資優挑戰題】煮 1 桶麵可供 8 大 6 小吃；煮 2 桶麵可供 12 大 20 小吃。請問煮 3 桶麵可供 20 個大人和幾個小孩吃？",
        options: ["26 個", "24 個", "28 個", "30 個"],
        ans: "26 個",
        explain: "2 桶麵 = 1 桶×2 = 16 大 12 小。與 12 大 20 小相比：省下 4 個大人食量 = 多供 8 個小孩，因此 1 大 = 2 小！3 桶麵 = 24 大 18 小。供 20 個大人時多出 4 大 = 8 小，故小孩可供 18 + 8 = 26 個！"
      }
    ]
  }
];

// 詞彙寶典資料
const glossaryTerms = [
  { term: "比 (Ratio)", def: "數學中表示兩個數量的倍數或對應關係，以符號「：」記錄，讀作「比」。例如 1：2。" },
  { term: "前項與後項 (Terms of Ratio)", def: "在比 a：b 中，符號前面的 a 稱為前項，後面的 b 稱為後項。順序不可任意調換。" },
  { term: "比值 (Value of Ratio)", def: "前項除以後項所得到的商（前項 ÷ 後項）。可以用整數、最簡分數或小數表示。後項不得為 0。" },
  { term: "相等的比 (Equivalent Ratio)", def: "當兩個比的比值相等時，稱為相等的比。比的前項與後項同乘以或同除以不為 0 的數，比值保持不變。" },
  { term: "最簡單整數比 (Simplest Form)", def: "比的前項與後項都是整數，且兩數互質（最大公因數為 1）的比。" },
  { term: "按比分配 (Proportional Division)", def: "把一個總數量依照指定的比（如 a：b）分給各個對象的數學解題方法。" }
];

// ── 渲染關卡內容 ──
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
        <span class="badge-tag">Stage ${stageIdx} / 5</span>
      </div>

      <div class="concept-box">
        ${data.concept}
      </div>
  `;

  // 若為 Stage 1 加入紅茶模擬器
  if (data.hasTeaLab) {
    html += `
      <div class="lab-widget">
        <h3 style="margin-bottom:12px; color:var(--primary-dark); display:flex; align-items:center; gap:8px;">
          <span>☕</span><span>土耳其特調紅茶實驗室 (動態比值體驗)</span>
        </h3>
        <p style="color:var(--text-muted); margin-bottom:16px;">
          調整濃茶與開水杯數，即時觀察茶湯顏色與比值變化！課本推薦黃金比例為 <strong>1：2</strong>。
        </p>
        <div class="tea-sim-container">
          <div class="cup-visual-wrap">
            <div id="teaLiquid" class="tea-liquid" style="height:60%; background:#B45309;">
              <span id="teaLiquidText">紅茶</span>
            </div>
          </div>
          <div class="tea-controls">
            <div class="slider-row">
              <label>
                <span>濃茶杯數 (前項)</span>
                <span id="teaConcentrateVal" style="color:#B45309; font-weight:800;">1 杯</span>
              </label>
              <input type="range" id="teaConcentrateSlider" min="1" max="10" value="1" oninput="updateTeaSim()">
            </div>
            <div class="slider-row">
              <label>
                <span>開水杯數 (後項)</span>
                <span id="teaWaterVal" style="color:#0284C7; font-weight:800;">2 杯</span>
              </label>
              <input type="range" id="teaWaterSlider" min="1" max="10" value="2" oninput="updateTeaSim()">
            </div>
            <div class="tea-metrics">
              <div class="metrics-line" id="teaRatioDisplay">比 ＝ 1：2</div>
              <div class="metrics-line" id="teaValueDisplay" style="color:#0284C7;">比值 ＝ 1 ÷ 2 ＝ 1/2 (0.5)</div>
              <div style="font-size:0.95rem; color:#475569; margin-top:4px;" id="teaComment">
                ✨ 口感：道地土耳其紅茶香！甜醇回甘！
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  // 若為 Stage 3 加入最簡比天平工具
  if (data.hasBalanceTool) {
    html += `
      <div class="balance-widget">
        <h3 style="margin-bottom:12px; color:var(--primary-dark); display:flex; align-items:center; gap:8px;">
          <span>⚖️</span><span>最簡單整數比魔法天平 (逐步化簡器)</span>
        </h3>
        <p style="color:var(--text-muted); margin-bottom:14px;">
          輸入任意兩個數（支援整數或小數），天平將為你施展化簡魔法，展現最大公因數約分歷程！
        </p>
        <div class="balance-inputs">
          <input type="number" id="balanceA" class="balance-input" value="12" placeholder="前項">
          <span class="balance-colon">：</span>
          <input type="number" id="balanceB" class="balance-input" value="18" placeholder="後項">
          <button class="btn-calc" onclick="calculateSimplestRatio()">✨ 魔法化簡</button>
        </div>
        <div id="balanceResult" class="balance-result"></div>
      </div>
    `;
  }

  // 測驗題庫卡片
  html += `
      <h3 style="margin:24px 0 10px; color:var(--text-main); display:flex; align-items:center; gap:8px;">
        <span>✏️</span><span>闖關即時測驗 (選項自動隨機化)</span>
      </h3>
      <div class="quiz-list" id="stageQuizList">
  `;

  data.quizzes.forEach((quiz, qIdx) => {
    // 選項隨機打亂
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
          ${stageIdx === 5 ? '前往榮譽殿堂 🏆' : '前往下一關 ➡️'}
        </button>
      </div>
    </div>
  `;

  container.innerHTML = html;
  window.scrollTo({ top: 180, behavior: 'smooth' });

  // 若有紅茶實驗室，初始化滑桿
  if (data.hasTeaLab) {
    updateTeaSim();
  }
}

// ── 紅茶模擬器即時更新 ──
function updateTeaSim() {
  const c = parseInt(document.getElementById('teaConcentrateSlider').value, 10);
  const w = parseInt(document.getElementById('teaWaterSlider').value, 10);
  document.getElementById('teaConcentrateVal').textContent = `${c} 杯`;
  document.getElementById('teaWaterVal').textContent = `${w} 杯`;

  const total = c + w;
  const liquid = document.getElementById('teaLiquid');
  const ratioDisplay = document.getElementById('teaRatioDisplay');
  const valueDisplay = document.getElementById('teaValueDisplay');
  const comment = document.getElementById('teaComment');

  // 計算比值
  const val = c / w;
  const valFixed = val.toFixed(2).replace(/\\.00$/, '');
  
  // 最大公因數簡化分數
  function getGcd(x, y) { return y === 0 ? x : getGcd(y, x % y); }
  const g = getGcd(c, w);
  const simC = c / g;
  const simW = w / g;
  const fracStr = simW === 1 ? `${simC}` : `${simC}/${simW}`;

  ratioDisplay.textContent = `比 ＝ ${c}：${w}（最簡整數比 ${simC}：${simW}）`;
  valueDisplay.textContent = `比值 ＝ 前項 ÷ 後項 ＝ ${c} ÷ ${w} ＝ ${fracStr} (${valFixed})`;

  // 視覺顏色深度計算 (濃茶比例)
  const concRatio = c / total;
  let bgCol = '#B45309';
  let taste = '道地土耳其紅茶香！甜醇回甘！';

  if (concRatio > 0.6) {
    bgCol = '#451A03';
    taste = '濃烈無比！需要來一顆土耳其軟糖配著喝！☕🍬';
  } else if (concRatio >= 0.3 && concRatio <= 0.4) {
    bgCol = '#92400E';
    taste = '🌟 完美黃金比例（約 1：2）！醇厚順口！';
  } else if (concRatio < 0.25) {
    bgCol = '#FBBF24';
    taste = '清爽微茶香，開水稍微多了一點點！';
  }

  const heightPercent = Math.min(95, Math.max(30, (total / 20) * 100));
  liquid.style.height = `${heightPercent}%`;
  liquid.style.background = bgCol;
  comment.textContent = `✨ 口感評語：${taste}`;
}

// ── 最簡單整數比魔法天平運算 ──
function calculateSimplestRatio() {
  const inA = document.getElementById('balanceA').value.trim();
  const inB = document.getElementById('balanceB').value.trim();
  const resDiv = document.getElementById('balanceResult');

  if (!inA || !inB) {
    resDiv.style.display = 'block';
    resDiv.innerHTML = '<span style="color:#EF4444;">⚠️ 請在前後項皆輸入數值！</span>';
    return;
  }

  let numA = parseFloat(inA);
  let numB = parseFloat(inB);

  if (isNaN(numA) || isNaN(numB) || numA <= 0 || numB <= 0) {
    resDiv.style.display = 'block';
    resDiv.innerHTML = '<span style="color:#EF4444;">⚠️ 請輸入大於 0 的正數！</span>';
    return;
  }

  let log = [];
  log.push(`📌 原始比：<strong>${inA} ： ${inB}</strong>`);

  // 處理小數情況
  const decA = (inA.split('.')[1] || '').length;
  const decB = (inB.split('.')[1] || '').length;
  const maxDec = Math.max(decA, decB);

  let intA = Math.round(numA * Math.pow(10, maxDec));
  let intB = Math.round(numB * Math.pow(10, maxDec));

  if (maxDec > 0) {
    const factor = Math.pow(10, maxDec);
    log.push(`🔹 步驟一（化為整數）：前後項同乘以 <strong>${factor}</strong> ➔ <strong>${intA} ： ${intB}</strong>`);
  }

  // 輾轉相除求 GCD
  function gcd(a, b) { return b === 0 ? a : gcd(b, a % b); }
  const g = gcd(intA, intB);

  log.push(`🔹 步驟二（找最大公因數）：${intA} 與 ${intB} 的最大公因數為 <strong>${g}</strong>`);
  const finalA = intA / g;
  const finalB = intB / g;
  log.push(`🔹 步驟三（同除以最大公因數）：(${intA}÷${g}) ： (${intB}÷${g}) ➔ <strong>${finalA} ： ${finalB}</strong>`);
  log.push(`🎉 <strong>最簡單整數比：${finalA} ： ${finalB}</strong>（比值為 ${finalA}/${finalB} 或 ${(finalA/finalB).toFixed(3).replace(/\\.000$/, '')}）`);

  resDiv.style.display = 'block';
  resDiv.innerHTML = log.join('<br>');
  playSound('correct');
}

// ── 檢查測驗答案 ──
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
    updateMascot('🎯 答對了！概念掌握得非常清楚！');
  } else {
    btn.classList.add('wrong-opt');
    card.classList.add('wrong-item');
    playSound('wrong');
    resetCombo();
    updateMascot('💪 沒關係，看看下方的解題步驟，馬上就能學會！');
  }

  explain.style.display = 'block';
}

// ── 關卡跳轉與榮譽殿堂 ──
function gotoStage(idx) {
  playSound('click');
  renderStage(idx);
}

function nextStage() {
  if (currentStage < 5) {
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
    showCastleModal('提示', '已經是第一關囉！', '🏰');
  }
}

function renderFinal() {
  playSound('level_clear');
  if (typeof confetti === 'function') {
    confetti({ particleCount: 150, spread: 100, origin: { y: 0.6 } });
  }
  const container = document.getElementById('stageContainer');
  const tabs = document.querySelectorAll('.stage-tab');
  tabs.forEach(t => t.classList.remove('active'));

  container.innerHTML = `
    <div class="section-card badge-showcase">
      <div class="medal-icon">🏅</div>
      <h2 style="font-size:2rem; font-weight:900; color:var(--primary-dark); margin-bottom:12px;">
        恭喜完成【比和比值奇境】全部挑戰！
      </h2>
      <p style="font-size:1.15rem; color:var(--text-muted); max-width:600px; margin:0 auto 24px;">
        你已完全掌握比的符號、前項後項、比值計算、相等的比、最簡整數比、按比分配與資優思考！獲頒「<strong>比與比值大宗師</strong>」榮譽勳章！
      </p>
      <div style="display:flex; justify-content:center; gap:16px; margin-bottom:28px;">
        <div class="stat-pill" style="font-size:1.1rem; padding:8px 20px;">
          <span>⭐ 最終總得分：</span><strong style="color:#B45309;">${userScore} 分</strong>
        </div>
      </div>
      <div style="display:flex; justify-content:center; gap:16px;">
        <button class="btn-calc" onclick="gotoStage(0)">🔄 再次挑戰複習</button>
        <a href="portal.html" class="back-btn" style="padding:10px 24px; font-size:1.05rem;">🏰 返回傳送門</a>
      </div>
    </div>
  `;
  window.scrollTo({ top: 180, behavior: 'smooth' });
}

// ── 辭典彈窗 ──
function openGlossary() {
  playSound('click');
  let body = '<div style="display:flex; flex-direction:column; gap:14px;">';
  glossaryTerms.forEach(t => {
    body += `
      <div style="background:#F0FDFA; border-left:4px solid var(--primary); padding:10px 14px; border-radius:0 8px 8px 0;">
        <div style="font-weight:800; color:var(--primary-dark); margin-bottom:4px;">${t.term}</div>
        <div style="font-size:0.95rem; color:#334155;">${t.def}</div>
      </div>
    `;
  });
  body += '</div>';
  showCastleModal('比和比值・核心知識寶典', body, '📖');
}

// ── 頁面初始化 ──
document.addEventListener('DOMContentLoaded', () => {
  renderStage(0);
});
</script>
</body>
</html>
'''

with open('ratio.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated ratio.html (size: {len(html_content)} chars)")

