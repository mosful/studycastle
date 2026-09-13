/**
 * 6年級國語全題目「情境插畫、部首象形與思維導圖」視覺化引擎（旗艦升級版）
 * 專為文字理解能力較弱學童設計，題題配圖、看圖懂題意！
 * 涵蓋：L1~L12 課文情境、全冊核心成語、字形字音部首拆解、易混淆字族！
 */

function getChineseVisualBadge(q, lessonTitle = '') {
  if (!q) return '';
  const text = (q.q || '') + ' ' + (q.type || '') + ' ' + (q.steps || '') + ' ' + (q.options ? q.options.join(' ') : '');
  const title = lessonTitle || '';

  // ================= 1. 課文核心故事漫畫卡 =================
  // L8: 晏子使楚（狗門、南橘北枳、晏子反擊）
  if (title.includes('晏子') || text.includes('晏子') || text.includes('楚王') || text.includes('狗國') || text.includes('橘化為枳')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
        <text x="35" y="45" font-size="28">⛩️</text>
        <text x="75" y="45" font-size="28">🐕</text>
        <text x="115" y="45" font-size="28">🍊</text>
        <text x="180" y="38" font-size="15" fill="#991B1B" font-weight="900" text-anchor="middle">《晏子使楚》</text>
        <text x="180" y="58" font-size="11" fill="#B91C1C" text-anchor="middle">狗國才開狗門！</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#FECACA" stroke-width="1.5"/>
        <text x="130" y="94" font-size="11.5" fill="#7F1D1D" font-weight="bold" text-anchor="middle">💡 機智外交：不卑不亢反擊楚王侮辱，維護國格！</text>
      </svg>
    `;
  }

  // L9: 三國演義·空城計（撫琴、城門大開、司馬懿退兵）
  if (title.includes('空城') || text.includes('空城') || text.includes('諸葛亮') || text.includes('司馬懿') || text.includes('撫琴')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#F8FAFC" stroke="#475569" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🏯</text>
        <text x="75" y="45" font-size="28">🪕</text>
        <text x="115" y="45" font-size="28">🐎</text>
        <text x="180" y="38" font-size="15" fill="#1E293B" font-weight="900" text-anchor="middle">《三國演義·空城計》</text>
        <text x="180" y="58" font-size="11" fill="#475569" text-anchor="middle">城門大開，焚香撫琴</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#CBD5E1" stroke-width="1.5"/>
        <text x="130" y="94" font-size="11.5" fill="#0F172A" font-weight="bold" text-anchor="middle">💡 心理戰術：算準敵將疑心過重，大智化險為夷！</text>
      </svg>
    `;
  }

  // L4: 客家擂茶（擂缽、花生芝麻茶葉）
  if (title.includes('擂茶') || text.includes('擂茶') || text.includes('客家') || text.includes('擂缽') || text.includes('芝麻')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#F0FDF4" stroke="#16A34A" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🥣</text>
        <text x="75" y="45" font-size="28">🪵</text>
        <text x="115" y="45" font-size="28">🍵</text>
        <text x="180" y="38" font-size="15" fill="#15803D" font-weight="900" text-anchor="middle">《客家擂茶》</text>
        <text x="180" y="58" font-size="11" fill="#166534" text-anchor="middle">茶葉花生，細細擂碎</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#BBF7D0" stroke-width="1.5"/>
        <text x="130" y="94" font-size="11.5" fill="#14532D" font-weight="bold" text-anchor="middle">💡 傳統茶道：象徵客家族群勤勞樸實與熱情待客！</text>
      </svg>
    `;
  }

  // L12: 橋（風雪中的木橋、人間溫暖）
  if (title.includes('橋') || text.includes('橋') || text.includes('小木橋') || text.includes('山溪')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🌉</text>
        <text x="75" y="45" font-size="28">🌊</text>
        <text x="115" y="45" font-size="28">🤝</text>
        <text x="180" y="38" font-size="16" fill="#1E40AF" font-weight="900" text-anchor="middle">《橋》· 心靈相通</text>
        <text x="180" y="58" font-size="11" fill="#2563EB" text-anchor="middle">連接兩岸，溝通心靈</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#BFDBFE" stroke-width="1.5"/>
        <text x="130" y="94" font-size="11.5" fill="#1E3A8A" font-weight="bold" text-anchor="middle">💡 象徵意涵：不僅跨越水流，更搭起人與人間的理解！</text>
      </svg>
    `;
  }

  // L10: 節日與習俗（端午、中秋、春節）
  if (title.includes('節日') || text.includes('節日') || text.includes('端午') || text.includes('中秋') || text.includes('春節') || text.includes('元宵')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🚣</text>
        <text x="75" y="45" font-size="28">🥮</text>
        <text x="115" y="45" font-size="28">🏮</text>
        <text x="180" y="38" font-size="15" fill="#B45309" font-weight="900" text-anchor="middle">傳統節日與習俗</text>
        <text x="180" y="58" font-size="11" fill="#D97706" text-anchor="middle">文化傳承，團聚祈福</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#FDE68A" stroke-width="1.5"/>
        <text x="130" y="94" font-size="11.5" fill="#92400E" font-weight="bold" text-anchor="middle">💡 歲時民俗：承載中華文化對天地感恩與家庭和諧！</text>
      </svg>
    `;
  }

  // L2: 朱子治家格言選
  if (title.includes('朱子') || text.includes('朱子') || text.includes('黎明即起') || text.includes('一粥一飯')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FEFCE8" stroke="#CA8A04" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🌅</text>
        <text x="75" y="45" font-size="28">🧹</text>
        <text x="115" y="45" font-size="28">🥣</text>
        <text x="180" y="38" font-size="15" fill="#854D0E" font-weight="900" text-anchor="middle">朱子治家格言</text>
        <text x="180" y="58" font-size="11.5" fill="#A16207" text-anchor="middle">黎明即起，灑掃庭除</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#FEF08A" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#713F12" font-weight="bold" text-anchor="middle">💡 一粥一飯當思來處不易，勤儉持家修身之道！</text>
      </svg>
    `;
  }

  // L1: 夢想（藍絲帶/跑道/運動員精神）
  if (title.includes('夢想') || title.includes('藍絲帶') || text.includes('藍絲帶') || text.includes('跑道')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
        <text x="40" y="50" font-size="34">🎗️</text>
        <text x="85" y="38" font-size="16" fill="#1E40AF" font-weight="900">神奇的藍絲帶</text>
        <text x="85" y="58" font-size="11.5" fill="#2563EB">「你是重要而有價值的！」</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#BFDBFE" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#1E3A8A" font-weight="bold" text-anchor="middle">💡 傳遞讚美與肯定，化解冷漠挽救心靈！</text>
      </svg>
    `;
  }

  // L3: 遇見美麗的自己（自嘲、幽默）
  if (title.includes('美麗') || title.includes('幽默') || text.includes('自嘲') || text.includes('幽默')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FDF4FF" stroke="#C026D3" stroke-width="2"/>
        <text x="40" y="50" font-size="32">🎭</text>
        <text x="85" y="38" font-size="16" fill="#86198F" font-weight="900">自嘲是幽默的最高境界</text>
        <text x="85" y="58" font-size="11.5" fill="#A21CAF">先笑自己，再笑世界</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#F5D0FE" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#701A75" font-weight="bold" text-anchor="middle">💡 展現寬宏氣度，化解社交尷尬與衝突！</text>
      </svg>
    `;
  }

  // ================= 2. 祝賀成語專題（L6 等常用題） =================
  if (text.includes('新婚') || text.includes('百年好合') || text.includes('琴瑟和鳴')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="115" viewBox="0 0 260 115">
        <rect x="10" y="8" width="240" height="99" rx="14" fill="#FFF1F2" stroke="#F43F5E" stroke-width="2"/>
        <text x="40" y="48" font-size="28">💍</text>
        <text x="85" y="48" font-size="28">🕊️</text>
        <text x="175" y="38" font-size="15" fill="#9F1239" font-weight="900" text-anchor="middle">賀新婚題辭</text>
        <text x="175" y="58" font-size="11.5" fill="#BE123C" text-anchor="middle">百年好合·琴瑟和鳴</text>
        <line x1="20" y1="70" x2="240" y2="70" stroke="#FECDD3" stroke-width="1.5"/>
        <text x="130" y="90" font-size="11.5" fill="#881337" font-weight="bold" text-anchor="middle">💡 祝賀新郎新娘白頭偕老、恩愛和睦！</text>
      </svg>
    `;
  }

  if (text.includes('祝壽') || text.includes('壽比南山') || text.includes('福如東海')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="115" viewBox="0 0 260 115">
        <rect x="10" y="8" width="240" height="99" rx="14" fill="#FEFCE8" stroke="#EAB308" stroke-width="2"/>
        <text x="40" y="48" font-size="28">🎂</text>
        <text x="85" y="48" font-size="28">🌲</text>
        <text x="175" y="38" font-size="15" fill="#854D0E" font-weight="900" text-anchor="middle">祝壽題辭</text>
        <text x="175" y="58" font-size="11.5" fill="#A16207" text-anchor="middle">福如東海·壽比南山</text>
        <line x1="20" y1="70" x2="240" y2="70" stroke="#FEF08A" stroke-width="1.5"/>
        <text x="130" y="90" font-size="11.5" fill="#713F12" font-weight="bold" text-anchor="middle">💡 祝賀長輩福澤綿長、健康長壽如松柏！</text>
      </svg>
    `;
  }

  if (text.includes('喬遷') || text.includes('美輪美奐') || text.includes('金玉滿堂')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="115" viewBox="0 0 260 115">
        <rect x="10" y="8" width="240" height="99" rx="14" fill="#F0FDF4" stroke="#22C55E" stroke-width="2"/>
        <text x="40" y="48" font-size="28">🏠</text>
        <text x="85" y="48" font-size="28">✨</text>
        <text x="175" y="38" font-size="15" fill="#15803D" font-weight="900" text-anchor="middle">賀喬遷新居</text>
        <text x="175" y="58" font-size="11.5" fill="#16A34A" text-anchor="middle">喬遷之喜·美輪美奐</text>
        <line x1="20" y1="70" x2="240" y2="70" stroke="#BBF7D0" stroke-width="1.5"/>
        <text x="130" y="90" font-size="11.5" fill="#14532D" font-weight="bold" text-anchor="middle">💡 讚美新屋高大壯麗、富麗堂皇！</text>
      </svg>
    `;
  }

  if (text.includes('開業') || text.includes('生意') || text.includes('大展鴻圖')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="115" viewBox="0 0 260 115">
        <rect x="10" y="8" width="240" height="99" rx="14" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
        <text x="40" y="48" font-size="28">🎊</text>
        <text x="85" y="48" font-size="28">📈</text>
        <text x="175" y="38" font-size="15" fill="#B45309" font-weight="900" text-anchor="middle">賀開業誌慶</text>
        <text x="175" y="58" font-size="11.5" fill="#D97706" text-anchor="middle">大展鴻圖·生意興隆</text>
        <line x1="20" y1="70" x2="240" y2="70" stroke="#FDE68A" stroke-width="1.5"/>
        <text x="130" y="90" font-size="11.5" fill="#92400E" font-weight="bold" text-anchor="middle">💡 祝賀新店或企業蒸蒸日上、財源廣進！</text>
      </svg>
    `;
  }

  // ================= 3. 易混淆字族部首拆解卡 =================
  // 辨 / 辯 / 辮 / 瓣
  if (text.includes('辯') || text.includes('辨') || text.includes('辮') || text.includes('瓣')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#F8FAFC" stroke="#64748B" stroke-width="2"/>
        <g transform="translate(20, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#1D4ED8" text-anchor="middle">辯</text>
          <text x="24" y="38" font-size="9.5" fill="#2563EB" text-anchor="middle">言部·爭辯</text>
        </g>
        <g transform="translate(75, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#ECFDF5" stroke="#10B981"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#047857" text-anchor="middle">辨</text>
          <text x="24" y="38" font-size="9.5" fill="#059669" text-anchor="middle">刀部·分辨</text>
        </g>
        <g transform="translate(130, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#FEF3C7" stroke="#F59E0B"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#B45309" text-anchor="middle">辮</text>
          <text x="24" y="38" font-size="9.5" fill="#D97706" text-anchor="middle">糸部·辮子</text>
        </g>
        <g transform="translate(185, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#FDF4FF" stroke="#C026D3"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#86198F" text-anchor="middle">瓣</text>
          <text x="24" y="38" font-size="9.5" fill="#A21CAF" text-anchor="middle">瓜部·花瓣</text>
        </g>
        <text x="130" y="98" font-size="11.5" fill="#334155" font-weight="bold" text-anchor="middle">中間部首是關鍵：言說、刀分、糸髮、瓜瓣！</text>
      </svg>
    `;
  }

  // 燥 / 噪 / 躁 / 操
  if (text.includes('燥') || text.includes('噪') || text.includes('躁') || text.includes('操')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
        <g transform="translate(20, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#FEE2E2" stroke="#EF4444"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#B91C1C" text-anchor="middle">燥</text>
          <text x="24" y="38" font-size="9.5" fill="#DC2626" text-anchor="middle">火部·乾燥</text>
        </g>
        <g transform="translate(75, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#EFF6FF" stroke="#3B82F6"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#1D4ED8" text-anchor="middle">噪</text>
          <text x="24" y="38" font-size="9.5" fill="#2563EB" text-anchor="middle">口部·噪音</text>
        </g>
        <g transform="translate(130, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#FEF3C7" stroke="#F59E0B"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#B45309" text-anchor="middle">躁</text>
          <text x="24" y="38" font-size="9.5" fill="#D97706" text-anchor="middle">足部·急躁</text>
        </g>
        <g transform="translate(185, 20)">
          <rect x="0" y="0" width="48" height="42" rx="6" fill="#ECFDF5" stroke="#10B981"/>
          <text x="24" y="24" font-size="14" font-weight="900" fill="#047857" text-anchor="middle">操</text>
          <text x="24" y="38" font-size="9.5" fill="#059669" text-anchor="middle">手部·操縱</text>
        </g>
        <text x="130" y="98" font-size="11.5" fill="#78350F" font-weight="bold" text-anchor="middle">火乾、口鬧、足跳躁、動手來操持！</text>
      </svg>
    `;
  }

  // ================= 4. 常用重點成語 =================
  if (text.includes('臨渴掘井')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
        <text x="35" y="45" font-size="28">☀️</text>
        <text x="75" y="45" font-size="28">🏜️</text>
        <text x="115" y="45" font-size="28">⛏️</text>
        <text x="180" y="38" font-size="16" fill="#B45309" font-weight="900" text-anchor="middle">臨渴掘井</text>
        <text x="180" y="58" font-size="11.5" fill="#D97706" text-anchor="middle">口渴才去挖井！</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#FDE68A" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#92400E" font-weight="bold" text-anchor="middle">💡 意思：平時沒準備，事到臨頭才想辦法！</text>
      </svg>
    `;
  }

  if (text.includes('未雨綢繆')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
        <text x="35" y="45" font-size="28">🌧️</text>
        <text x="75" y="45" font-size="28">🐦</text>
        <text x="115" y="45" font-size="28">🪹</text>
        <text x="180" y="38" font-size="16" fill="#0369A1" font-weight="900" text-anchor="middle">未雨綢繆</text>
        <text x="180" y="58" font-size="11.5" fill="#0284C7" text-anchor="middle">下雨前修補鳥巢</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#BAE6FD" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#075985" font-weight="bold" text-anchor="middle">💡 意思：事情發生前先做好萬全準備！</text>
      </svg>
    `;
  }

  if (text.includes('勢均力敵')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
        <text x="40" y="45" font-size="26">🤼‍♂️</text>
        <line x1="75" y1="40" x2="185" y2="40" stroke="#DC2626" stroke-width="4"/>
        <circle cx="130" cy="40" r="7" fill="#B91C1C"/>
        <text x="130" y="26" font-size="11" fill="#B91C1C" font-weight="bold" text-anchor="middle">繩結不動</text>
        <text x="215" y="45" font-size="26">🤼‍♀️</text>
        <line x1="20" y1="70" x2="240" y2="70" stroke="#FECACA" stroke-width="1.5"/>
        <text x="130" y="92" font-size="14" fill="#991B1B" font-weight="900" text-anchor="middle">勢均力敵 ➜ 力量旗鼓相當！</text>
      </svg>
    `;
  }

  if (text.includes('胸有成竹')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
        <text x="40" y="45" font-size="28">🎍</text>
        <text x="80" y="45" font-size="28">🖌️</text>
        <text x="175" y="38" font-size="16" fill="#047857" font-weight="900" text-anchor="middle">胸有成竹</text>
        <text x="175" y="58" font-size="11.5" fill="#059669" text-anchor="middle">畫畫前心中已有翠竹</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#A7F3D0" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#065F46" font-weight="bold" text-anchor="middle">💡 意思：計畫周詳，做事前充滿自信！</text>
      </svg>
    `;
  }

  if (text.includes('雪中送炭')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#F1F5F9" stroke="#64748B" stroke-width="2"/>
        <text x="35" y="45" font-size="28">❄️</text>
        <text x="75" y="45" font-size="28">🪵</text>
        <text x="115" y="45" font-size="28">🔥</text>
        <text x="180" y="38" font-size="16" fill="#334155" font-weight="900" text-anchor="middle">雪中送炭</text>
        <text x="180" y="58" font-size="11.5" fill="#475569" text-anchor="middle">大雪中送來暖炭</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#CBD5E1" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#1E293B" font-weight="bold" text-anchor="middle">💡 意思：在他人最困苦急難時給予實質幫助！</text>
      </svg>
    `;
  }

  if (text.includes('負荊請罪')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
        <text x="40" y="45" font-size="28">🙇‍♂️</text>
        <text x="85" y="45" font-size="28">🎋</text>
        <text x="175" y="38" font-size="16" fill="#B45309" font-weight="900" text-anchor="middle">負荊請罪</text>
        <text x="175" y="58" font-size="11.5" fill="#D97706" text-anchor="middle">背著荊條登門道歉</text>
        <line x1="20" y1="72" x2="240" y2="72" stroke="#FDE68A" stroke-width="1.5"/>
        <text x="130" y="94" font-size="12" fill="#78350F" font-weight="bold" text-anchor="middle">💡 意思：真誠向對方認錯道歉，請求原諒！</text>
      </svg>
    `;
  }

  // ================= 5. 重點生字拆解 =================
  if (text.includes('尷尬')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#FDF4FF" stroke="#C026D3" stroke-width="2"/>
        <rect x="25" y="20" width="45" height="45" rx="8" fill="#FAE8FF" stroke="#A21CAF" stroke-width="2"/>
        <text x="47" y="52" font-size="24" fill="#86198F" font-weight="900" text-anchor="middle">尢</text>
        <text x="47" y="80" font-size="11" fill="#A21CAF" text-anchor="middle">跛足難行</text>
        <text x="85" y="50" font-size="20" fill="#64748B">＋</text>
        <rect x="105" y="20" width="60" height="45" rx="8" fill="#FAE8FF" stroke="#A21CAF" stroke-width="2"/>
        <text x="135" y="48" font-size="15" fill="#86198F" font-weight="900" text-anchor="middle">兼 / 介</text>
        <text x="135" y="80" font-size="11" fill="#A21CAF" text-anchor="middle">進退兩難</text>
        <text x="205" y="50" font-size="28">😅</text>
        <text x="130" y="104" font-size="12.5" fill="#701A75" font-weight="900" text-anchor="middle">「尷尬」皆從「尢」部！處境窘迫難堪！</text>
      </svg>
    `;
  }

  if (text.includes('芥蒂')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="125" viewBox="0 0 260 125">
        <rect x="10" y="8" width="240" height="109" rx="14" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
        <rect x="25" y="20" width="50" height="45" rx="8" fill="#D1FAE5" stroke="#047857" stroke-width="2"/>
        <text x="50" y="52" font-size="26" fill="#065F46" font-weight="900" text-anchor="middle">艸</text>
        <text x="50" y="80" font-size="11" fill="#047857" text-anchor="middle">草木細刺</text>
        <text x="90" y="50" font-size="20" fill="#64748B">＋</text>
        <rect x="110" y="20" width="60" height="45" rx="8" fill="#D1FAE5" stroke="#047857" stroke-width="2"/>
        <text x="140" y="48" font-size="15" fill="#065F46" font-weight="900" text-anchor="middle">介 / 帝</text>
        <text x="140" y="80" font-size="11" fill="#047857" text-anchor="middle">微小梗阻</text>
        <text x="205" y="50" font-size="28">🌱</text>
        <text x="130" y="104" font-size="12.5" fill="#064E3B" font-weight="900" text-anchor="middle">「芥蒂」皆從「艸」部！指微小的心結！</text>
      </svg>
    `;
  }

  if (text.includes('勝券')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="120" viewBox="0 0 260 120">
        <rect x="10" y="8" width="240" height="104" rx="14" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
        <rect x="25" y="20" width="55" height="45" rx="8" fill="#FDE68A" stroke="#B45309" stroke-width="2"/>
        <text x="52" y="52" font-size="26" fill="#92400E" font-weight="900" text-anchor="middle">刀</text>
        <text x="52" y="80" font-size="11" fill="#B45309" text-anchor="middle">刀契憑證</text>
        <text x="95" y="50" font-size="20" fill="#64748B">➜</text>
        <rect x="120" y="20" width="65" height="45" rx="8" fill="#FDE68A" stroke="#B45309" stroke-width="2"/>
        <text x="152" y="50" font-size="20" fill="#92400E" font-weight="900" text-anchor="middle">券</text>
        <text x="152" y="80" font-size="11" fill="#B45309" text-anchor="middle">下為「刀」</text>
        <text x="215" y="50" font-size="28">🏆</text>
        <text x="130" y="102" font-size="12.5" fill="#78350F" font-weight="900" text-anchor="middle">「勝券在握」是刀部的券（契據），非手捲！</text>
      </svg>
    `;
  }

  // ================= 6. 修辭手法 =================
  if (text.includes('譬喻') || (q.type && q.type.includes('修辭') && text.includes('像'))) {
    return `
      <svg class="chinese-visual-svg" width="260" height="110" viewBox="0 0 260 110">
        <rect x="10" y="8" width="240" height="94" rx="14" fill="#FDF4FF" stroke="#A855F7" stroke-width="2"/>
        <circle cx="50" cy="40" r="18" fill="#F3E8FF" stroke="#9333EA" stroke-width="2"/>
        <text x="50" y="45" font-size="11" fill="#7E22CE" font-weight="bold" text-anchor="middle">本體 A</text>
        <text x="95" y="45" font-size="14" fill="#9333EA" font-weight="bold">好像 ➜</text>
        <circle cx="150" cy="40" r="18" fill="#F3E8FF" stroke="#9333EA" stroke-width="2"/>
        <text x="150" y="45" font-size="11" fill="#7E22CE" font-weight="bold" text-anchor="middle">喻體 B</text>
        <text x="210" y="48" font-size="28">⚖️</text>
        <text x="130" y="88" font-size="12" fill="#6B21A8" font-weight="bold" text-anchor="middle">【譬喻法】利用相似特點，讓描寫更加生動！</text>
      </svg>
    `;
  }

  if (text.includes('擬人')) {
    return `
      <svg class="chinese-visual-svg" width="260" height="110" viewBox="0 0 260 110">
        <rect x="10" y="8" width="240" height="94" rx="14" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
        <text x="40" y="48" font-size="28">🌸</text>
        <text x="80" y="48" font-size="28">💃</text>
        <text x="120" y="48" font-size="28">🍃</text>
        <text x="180" y="38" font-size="15" fill="#047857" font-weight="900" text-anchor="middle">【擬人法】</text>
        <text x="180" y="58" font-size="11.5" fill="#059669" text-anchor="middle">賦予事物人的情感與動作</text>
        <text x="130" y="88" font-size="12" fill="#065F46" font-weight="bold" text-anchor="middle">例如：微風在林梢輕輕歌唱、花兒展開笑臉！</text>
      </svg>
    `;
  }

  // ================= 7. 通用國語閱讀與推論卡 =================
  return `
    <svg class="chinese-visual-svg" width="260" height="90" viewBox="0 0 260 90">
      <rect x="10" y="8" width="240" height="74" rx="12" fill="#F8FAFC" stroke="#6366F1" stroke-width="2"/>
      <text x="38" y="48" font-size="26">📖</text>
      <text x="80" y="35" font-size="14" fill="#312E81" font-weight="900">課文核心閱讀與字詞推論</text>
      <text x="80" y="54" font-size="11.5" fill="#4338CA">仔細觀察上下文脈絡、部首結構與情感轉折！</text>
      <text x="80" y="70" font-size="11" fill="#6366F1" font-weight="bold">💡 看清關鍵字詞，排除陷阱選項！</text>
    </svg>
  `;
}

/**
 * 生字部首象形意象小標章
 */
function getVocabRadicalBadge(word) {
  if (!word) return '';
  if (word.includes('心') || word.includes('情') || word.includes('意') || word.includes('悵') || word.includes('忌') || word.includes('懍')) {
    return `<span class="radical-badge" title="心部：與情感、內心想法相關">❤️ 心部·內心情思</span>`;
  }
  if (word.includes('草') || word.includes('芥') || word.includes('蒂') || word.includes('落') || word.includes('萌') || word.includes('茫')) {
    return `<span class="radical-badge" title="艸部：與草木植物相關">🌱 艸部·植物生長</span>`;
  }
  if (word.includes('水') || word.includes('海') || word.includes('澎') || word.includes('湃') || word.includes('湧') || word.includes('洋') || word.includes('淋')) {
    return `<span class="radical-badge" title="水部：與水流波濤相關">🌊 水部·波濤流動</span>`;
  }
  if (word.includes('刀') || word.includes('券') || word.includes('切') || word.includes('刻') || word.includes('劍') || word.includes('利')) {
    return `<span class="radical-badge" title="刀部：與利器切削、契約相關">🗡️ 刀部·利器契約</span>`;
  }
  if (word.includes('手') || word.includes('持') || word.includes('操') || word.includes('挽') || word.includes('推') || word.includes('擬')) {
    return `<span class="radical-badge" title="手部：與動作操作相關">✋ 手部·動作舉止</span>`;
  }
  if (word.includes('足') || word.includes('踏') || word.includes('蹈') || word.includes('蹣') || word.includes('跚') || word.includes('跑')) {
    return `<span class="radical-badge" title="足部：與雙腳步伐相關">👣 足部·步伐行動</span>`;
  }
  if (word.includes('目') || word.includes('瞻') || word.includes('仰') || word.includes('瞪') || word.includes('眺') || word.includes('視')) {
    return `<span class="radical-badge" title="目部：與眼睛注視相關">👁️ 目部·觀察凝視</span>`;
  }
  if (word.includes('口') || word.includes('喊') || word.includes('囂') || word.includes('嘆') || word.includes('咽') || word.includes('嘲')) {
    return `<span class="radical-badge" title="口部：與言語聲音相關">🗣️ 口部·言語聲響</span>`;
  }
  if (word.includes('虫') || word.includes('蜿') || word.includes('蜒') || word.includes('蛇') || word.includes('蝶')) {
    return `<span class="radical-badge" title="虫部：與爬蟲曲折盤旋相關">🐛 虫部·曲折盤旋</span>`;
  }
  if (word.includes('羽') || word.includes('翼') || word.includes('翔') || word.includes('翱')) {
    return `<span class="radical-badge" title="羽部：與鳥羽飛翔相關">🪶 羽部·展翅高飛</span>`;
  }
  if (word.includes('玉') || word.includes('璀') || word.includes('璨') || word.includes('琢')) {
    return `<span class="radical-badge" title="玉部：與美玉光彩相關">💎 玉部·美玉星芒</span>`;
  }
  return `<span class="radical-badge">📝 字形意象</span>`;
}
