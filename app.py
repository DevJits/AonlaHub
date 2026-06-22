import streamlit as s
import streamlit.components.v1 as c

# ── CONFIG ──

s.set_page_config(
    page_title="Aonla Hub – Everything You Need",
    page_icon="https://i.ibb.co/gX2W1qx/aonla-hub.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

s.markdown("""
<style>

/* Top header hide */
header[data-testid="stHeader"] {
    display: none;
}

/* Footer hide */
footer {
    display: none;
}

/* Hamburger menu hide */
#MainMenu {
    visibility: hidden;
}

/* Top blank space remove */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

/* Main app container full width */
[data-testid="stAppViewContainer"] {
    padding: 0 !important;
    margin: 0 !important;
}

/* Remove iframe margins */
iframe {
    margin: 0 !important;
    padding: 0 !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="google-site-verification" content="Fx12Y3Ko_4CK4aFg-0wgYq7iyMH-36H5LhfdUH0g28E" />
<title>Aonla Hub – Everything You Need</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600;700&display=swap');
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --gold: #D4AF37;
    --gold-light: #F0D060;
    --gold-dim: #A88A3A;
    --gold-border: rgba(212,175,55,0.22);
    --bg: #050505;
    --card-bg: #111111;
    --text-muted: #A88A3A;
    --faint: #634E17;
  }
  html, body { background: var(--bg); color: var(--gold); font-family: 'Inter', sans-serif; min-height: 100vh; }

  @media (min-width: 769px) {
    html, body { overflow-x: hidden; overflow-y: auto; }
  }
  @media (max-width: 768px) {
    html, body { overflow: hidden; height: 100vh; }
  }

  /* ═══════════════════════════════════════
     DESKTOP LAYOUT  (≥ 769px)
  ═══════════════════════════════════════ */
  @media (min-width: 769px) {

    .mobile-only { display: none !important; }
    .desktop-only { display: flex; flex-direction: column; min-height: 100vh; }

    .desktop-header {
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 60px; height: 72px; background: #0a0a0a;
      border-bottom: 1px solid var(--gold-border);
      position: sticky; top: 0; z-index: 100; backdrop-filter: blur(12px);
    }
    .logo-name {
      font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 900;
      background: linear-gradient(to right, var(--gold), var(--gold-light), var(--gold));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }
    .logo-tag { font-size: 9px; letter-spacing: 0.2em; color: #C9A84C; font-weight: 700; text-transform: uppercase; margin-top: 2px; }

    .desktop-nav { display: flex; align-items: center; gap: 6px; }
    .desktop-nav-btn {
      display: flex; align-items: center; gap: 7px; padding: 8px 18px; border-radius: 10px;
      font-size: 12px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
      cursor: pointer; border: 1px solid transparent; background: none; color: var(--text-muted);
      transition: all 0.18s; text-decoration: none;
    }
    .desktop-nav-btn:hover { color: var(--gold); border-color: var(--gold-border); background: #111; }
    .desktop-nav-btn.active { color: #050505; background: var(--gold); border-color: var(--gold); }
    .desktop-nav-btn svg { width: 15px; height: 15px; }

    .desktop-hero {
      display: flex; align-items: center; justify-content: center; text-align: center; flex-direction: column;
      padding: 80px 40px 60px;
      background: radial-gradient(ellipse at center, rgba(212,175,55,0.06) 0%, transparent 70%);
      border-bottom: 1px solid var(--gold-border);
    }
    .hero-icon-d { font-size: 32px; margin-bottom: 14px; display: block; animation: bounce-d 2s infinite; }
    @keyframes bounce-d { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
    .desktop-hero h1 {
      font-family: 'Playfair Display', serif; font-size: clamp(36px, 4vw, 56px); font-weight: 900;
      background: linear-gradient(to right, var(--gold), var(--gold-light), var(--gold));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
      line-height: 1.15; margin-bottom: 16px;
    }
    .desktop-hero p { font-size: 16px; color: var(--text-muted); max-width: 520px; line-height: 1.7; margin-bottom: 28px; }
    .hero-badge-d {
      display: inline-flex; align-items: center; gap: 6px; background: #111; border: 1px solid var(--gold-dim);
      padding: 8px 20px; border-radius: 99px; font-size: 11px; font-weight: 700; text-transform: uppercase;
      letter-spacing: 0.12em; color: var(--gold);
    }

    .desktop-main { flex: 1; max-width: 1200px; margin: 0 auto; padding: 48px 40px 80px; width: 100%; }

    .desktop-section-title {
      font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: var(--gold-light);
      margin-bottom: 24px; padding-bottom: 12px; border-bottom: 1px solid var(--gold-border);
      display: flex; align-items: center; gap: 10px;
    }

    .pills-wrap-d { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 32px; }
    .pill-d {
      display: flex; align-items: center; gap: 6px; padding: 9px 18px; border-radius: 99px;
      font-size: 12px; font-weight: 700; border: 1px solid var(--gold-border); background: #111;
      color: var(--text-muted); cursor: pointer; white-space: nowrap; transition: all 0.18s; user-select: none;
    }
    .pill-d:hover { border-color: var(--gold); color: var(--gold); }
    .pill-d.active { background: var(--gold); color: #050505; border-color: var(--gold); box-shadow: 0 0 14px rgba(212,175,55,0.3); }

    .default-hint-d { text-align: center; padding: 60px 20px; border: 1px dashed var(--gold-border); border-radius: 20px; }
    .default-hint-d p { font-size: 14px; color: var(--faint); line-height: 1.8; }

    .cat-panel-d { display: none; }
    .cat-panel-d.visible { display: block; animation: fadeIn 0.22s ease; }
    @keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }

    .cat-banner-d {
      background: linear-gradient(135deg, #171305, #2D230B, #171305);
      border: 1px solid var(--gold-border); border-radius: 24px; padding: 60px 40px;
      display: flex; flex-direction: column; align-items: center; text-align: center;
    }
    .cat-big-emoji-d { font-size: 64px; margin-bottom: 16px; display: block; }
    .cat-banner-d h2 { font-family: 'Playfair Display', serif; font-size: 28px; color: var(--gold-light); margin-bottom: 10px; }
    .cat-banner-d p { font-size: 14px; color: var(--text-muted); line-height: 1.7; max-width: 420px; margin-bottom: 28px; }
    .dl-btn-d {
      display: inline-flex; align-items: center; gap: 9px; background: var(--gold); color: #050505;
      font-weight: 700; font-size: 13px; padding: 14px 32px; border-radius: 14px; text-decoration: none;
      text-transform: uppercase; letter-spacing: 0.08em; transition: background 0.15s, transform 0.1s;
      border: none; cursor: pointer;
    }
    .dl-btn-d:hover { background: var(--gold-light); }
    .dl-btn-d:active { transform: scale(0.97); }
    .dl-btn-d svg { width: 16px; height: 16px; }
    .cat-hint-d { font-size: 10px; color: var(--faint); margin-top: 14px; }

    .locked-d {
      background: var(--card-bg); border: 1px solid var(--gold-border); border-radius: 24px;
      padding: 60px 40px; text-align: center; display: flex; flex-direction: column; align-items: center;
    }
    .locked-d .lock-icon { font-size: 52px; margin-bottom: 16px; }
    .locked-d h2 { font-family: 'Playfair Display', serif; font-size: 26px; color: var(--gold-light); margin-bottom: 10px; }
    .locked-d p { font-size: 14px; color: var(--text-muted); line-height: 1.7; max-width: 400px; margin-bottom: 28px; }

    .desktop-footer {
      border-top: 1px solid var(--gold-border); padding: 24px 60px;
      display: flex; align-items: center; justify-content: space-between; font-size: 11px; color: var(--faint);
    }
  }

  /* ═══════════════════════════════════════
     MOBILE LAYOUT  (≤ 768px)
  ═══════════════════════════════════════ */
  @media (max-width: 768px) {

    .desktop-only { display: none !important; }
    .mobile-only { display: flex; }

    .shell-wrap { display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 0; }

    .phone {
      width: 100%; max-width: 420px; margin: 0 auto; background: #090909;
      display: flex; flex-direction: column; height: 100vh; position: relative; overflow: hidden;
    }

    .notch { height: 28px; background: #000; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .notch-pill { width: 80px; height: 16px; background: #141414; border-radius: 99px; border: 1px solid #2e2507; display: flex; align-items: center; justify-content: center; gap: 4px; }
    .notch-dot { width: 6px; height: 6px; background: #38bdf8; border-radius: 50%; animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.4} }

    .app-header { padding: 10px 20px 12px; background: linear-gradient(to bottom, #0e0e0e, #080808); border-bottom: 1px solid var(--gold-border); display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
    .app-name { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 900; background: linear-gradient(to right, var(--gold), var(--gold-light), var(--gold)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.1; }
    .app-tagline { font-size: 9px; letter-spacing: 0.22em; color: #C9A84C; font-weight: 700; text-transform: uppercase; margin-top: 2px; }
    .header-right { font-size: 9px; color: #C9A84C; }

    .body { flex: 1; overflow-y: auto; background: var(--bg); padding: 16px 16px 100px; scrollbar-width: none; }
    .body::-webkit-scrollbar { display: none; }

    .hero { background: linear-gradient(135deg, #171305, #2D230B, #171305); border: 1px solid var(--gold-border); border-radius: 18px; padding: 20px 16px; text-align: center; margin-bottom: 20px; }
    .hero-icon { font-size: 22px; margin-bottom: 6px; display: block; animation: bounce 2s infinite; }
    @keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
    .hero h2 { font-family: 'Playfair Display', serif; font-size: 17px; color: var(--gold-light); margin-bottom: 4px; }
    .hero p { font-size: 11px; color: var(--text-muted); line-height: 1.5; }
    .hero-badge { display: inline-flex; align-items: center; gap: 4px; margin-top: 12px; background: var(--bg); border: 1px solid var(--gold-dim); padding: 4px 12px; border-radius: 99px; font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--gold); }

    .section-label { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; padding: 0 2px; }
    .section-label h3 { font-family: 'Playfair Display', serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; background: linear-gradient(to right, var(--gold-light), var(--gold)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .section-label span { font-size: 10px; color: var(--text-muted); font-family: monospace; }

    .pills-wrap { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 8px; margin-bottom: 0; scrollbar-width: none; }
    .pills-wrap::-webkit-scrollbar { display: none; }
    .pill { flex-shrink: 0; padding: 6px 14px; border-radius: 99px; font-size: 10px; font-weight: 700; border: 1px solid var(--gold-border); background: #111; color: var(--text-muted); cursor: pointer; white-space: nowrap; transition: all 0.18s; user-select: none; }
    .pill:active { transform: scale(0.96); }
    .pill.active { background: var(--gold); color: #050505; border-color: var(--gold); box-shadow: 0 0 10px rgba(212,175,55,0.3); }

    .cat-panel { display: none; margin-top: 14px; }
    .cat-panel.visible { display: block; animation: fadeIn 0.22s ease; }
    @keyframes fadeIn { from{opacity:0;transform:translateY(6px)} to{opacity:1;transform:translateY(0)} }

    .cat-banner {
      background: linear-gradient(135deg, #171305, #2D230B, #171305);
      border: 1px solid var(--gold-border); border-radius: 18px; padding: 22px 16px 20px; text-align: center;
    }
    .cat-banner .cat-big-emoji { font-size: 38px; margin-bottom: 8px; display: block; }
    .cat-banner h3 { font-family: 'Playfair Display', serif; font-size: 16px; color: var(--gold-light); margin-bottom: 6px; }
    .cat-banner p { font-size: 11px; color: var(--text-muted); line-height: 1.5; margin-bottom: 16px; max-width: 240px; margin-left: auto; margin-right: auto; }
    .cat-banner .download-btn { display: inline-flex; align-items: center; gap: 7px; background: var(--gold); color: #050505; font-weight: 700; font-size: 11px; padding: 11px 24px; border-radius: 12px; text-decoration: none; text-transform: uppercase; letter-spacing: 0.08em; transition: background 0.15s, transform 0.1s; cursor: pointer; border: none; }
    .cat-banner .download-btn:active { transform: scale(0.97); }
    .cat-banner .download-btn svg { width: 14px; height: 14px; flex-shrink: 0; }
    .cat-banner .hint { font-size: 9px; color: #634E17; margin-top: 10px; }

    .default-hint { text-align: center; padding: 28px 16px; border: 1px dashed var(--gold-border); border-radius: 18px; margin-top: 14px; }
    .default-hint p { font-size: 11px; color: #634E17; line-height: 1.6; }

    .bottom-nav { position: absolute; bottom: 0; left: 0; right: 0; height: 88px; background: #070707; border-top: 1px solid var(--gold-border); display: flex; align-items: center; justify-content: space-around; padding: 0 12px 26px; z-index: 30; }
    .nav-btn { display: flex; flex-direction: column; align-items: center; gap: 4px; width: 80px; background: none; border: none; cursor: pointer; color: #8A6A1D; padding: 0; transition: color 0.15s; position: relative; text-decoration: none; }
    .nav-btn.active { color: var(--gold); }
    .nav-btn.active::before { content: ''; position: absolute; top: -4px; width: 32px; height: 3px; background: linear-gradient(to right, var(--gold), var(--gold-light)); border-radius: 2px; }
    .nav-btn svg { width: 18px; height: 18px; }
    .nav-label { font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }

    .modal-overlay { display: none; position: absolute; inset: 0; background: rgba(0,0,0,0.65); z-index: 50; align-items: flex-end; justify-content: center; }
    .modal-overlay.open { display: flex; animation: fadeOverlay 0.2s ease; }
    @keyframes fadeOverlay { from{opacity:0} to{opacity:1} }

    .modal-sheet { width: 100%; background: #0c0c0c; border-top: 2px solid var(--gold-dim); border-radius: 28px 28px 0 0; padding: 10px 20px 36px; animation: slideUp 0.28s cubic-bezier(0.32,0.72,0,1); text-align: center; }
    @keyframes slideUp { from{transform:translateY(100%)} to{transform:translateY(0)} }

    .modal-handle { width: 44px; height: 5px; background: #40310e; border-radius: 99px; margin: 0 auto 18px; }
    .modal-icon { font-size: 36px; margin-bottom: 10px; display: block; }
    .modal-sheet h4 { font-family: 'Playfair Display', serif; font-size: 17px; color: var(--gold-light); margin-bottom: 8px; }
    .modal-sheet p { font-size: 11px; color: var(--text-muted); line-height: 1.65; max-width: 260px; margin: 0 auto 20px; }
    .modal-dl-btn { display: flex; align-items: center; justify-content: center; gap: 8px; background: var(--gold); color: #050505; font-weight: 700; font-size: 12px; padding: 13px 0; border-radius: 13px; text-decoration: none; text-transform: uppercase; letter-spacing: 0.08em; width: 100%; border: none; cursor: pointer; transition: background 0.15s; margin-bottom: 10px; }
    .modal-dl-btn:active { background: var(--gold-light); }
    .modal-dl-btn svg { width: 15px; height: 15px; }
    .modal-close { font-size: 10px; color: #634E17; cursor: pointer; padding: 6px; display: block; }
    .modal-close:hover { color: var(--text-muted); }

    .home-indicator { position: absolute; bottom: 5px; left: 50%; transform: translateX(-50%); width: 100px; height: 3px; background: rgba(40,34,15,0.5); border-radius: 99px; pointer-events: none; z-index: 31; }
  }
</style>
</head>
<body>

<!-- ════════════════════════════════════
     DESKTOP VERSION
════════════════════════════════════ -->
<div class="desktop-only">

  <header class="desktop-header">
    <div>
      <div class="logo-name">Aonla Hub</div>
      <div class="logo-tag">Everything You Need</div>
    </div>
    <nav class="desktop-nav">
      <button class="desktop-nav-btn active" id="d-nav-collection" onclick="dTab('collection')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6z"/></svg>
        Collection
      </button>
      <button class="desktop-nav-btn" id="d-nav-basket" onclick="dOpenLocked()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>
        Basket 🔒
      </button>
      <a class="desktop-nav-btn" href="https://github.com/DevJits/AonlaHub/releases/download/1.0/AonlaHubv1.apk" target="_blank" rel="noopener" style="background:var(--gold);color:#050505;border-color:var(--gold);">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        Download App
      </a>
    </nav>
  </header>

  <section class="desktop-hero">
    <span class="hero-icon-d">✨</span>
    <h1>Your Orders are our<br>First Priority</h1>
    <p>Aonla Hub: Your All-In-One Aonla Store for Every Product — Food, Grocery, Pharmacy, Gifts, Fashion &amp; Electronics.</p>
    <div class="hero-badge-d">⚡ Best Aonla's Online Store</div>
  </section>


  <main class="desktop-main">

    <div id="d-tab-collection">
      <div class="desktop-section-title"><span>✨</span> Browse Categories</div>
      <div class="pills-wrap-d">
        <div class="pill-d" onclick="dSelectCat('food',this)">🍱 Food</div>
        <div class="pill-d" onclick="dSelectCat('grocery',this)">🛒 Grocery &amp; Daily Essentials</div>
        <div class="pill-d" onclick="dSelectCat('pharmacy',this)">💊 Pharmacy &amp; Healthcare</div>
        <div class="pill-d" onclick="dSelectCat('gifts',this)">🎁 Gifts &amp; Lifestyle</div>
        <div class="pill-d" onclick="dSelectCat('fashion',this)">👕 Fashion &amp; Clothing</div>
        <div class="pill-d" onclick="dSelectCat('electronics',this)">🔌 Electronics &amp; Home</div>
      </div>

      <div class="default-hint-d" id="d-default-hint">
        <p>👆 Select any category above to explore products<br>and get the download link to order</p>
      </div>

      <div class="cat-panel-d" id="d-panel-food">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">🍱</span>
          <h2>Food</h2>
          <p>Fresh meals, snacks &amp; local kitchen delights delivered hot to your door.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
      <div class="cat-panel-d" id="d-panel-grocery">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">🛒</span>
          <h2>Grocery &amp; Daily Essentials</h2>
          <p>Rice, dal, oil, and everything you need for daily life — all in one place.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
      <div class="cat-panel-d" id="d-panel-pharmacy">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">💊</span>
          <h2>Pharmacy &amp; Healthcare</h2>
          <p>Medicines, supplements, and healthcare products from trusted local stores.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
      <div class="cat-panel-d" id="d-panel-gifts">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">🎁</span>
          <h2>Gifts &amp; Lifestyle</h2>
          <p>Unique gifts and lifestyle products perfect for every occasion.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
      <div class="cat-panel-d" id="d-panel-fashion">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">👕</span>
          <h2>Fashion &amp; Clothing</h2>
          <p>Trendy clothes, kurtas, and accessories for men, women, and kids.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
      <div class="cat-panel-d" id="d-panel-electronics">
        <div class="cat-banner-d">
          <span class="cat-big-emoji-d">🔌</span>
          <h2>Electronics &amp; Home Appliances</h2>
          <p>Gadgets, cables, fans, bulbs and home appliances at the best prices.</p>
          <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to See Items &amp; Order
          </a>
          <p class="cat-hint-d">App mein poori list aur WhatsApp order available hai</p>
        </div>
      </div>
    </div>

    <div id="d-tab-basket" style="display:none;">
      <div class="locked-d">
        <div class="lock-icon">🛒🔒</div>
        <h2>Basket is Locked</h2>
        <p>Download the Aonla Hub app to add items, manage your basket, and place orders directly on WhatsApp!</p>
        <a class="dl-btn-d" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
          Download Now to Access Basket
        </a>
      </div>
    </div>

  </main>

  <footer class="desktop-footer">
    <span>© 2025 Aonla Hub — Everything You Need</span>
    <span>Created with ❤️ for Aonla</span>
  </footer>

</div>


<!-- ════════════════════════════════════
     MOBILE VERSION
════════════════════════════════════ -->
<div class="mobile-only">
  <div class="shell-wrap">
    <div class="phone">

      <div class="notch">
        <div class="notch-pill"><div class="notch-dot"></div></div>
      </div>

      <div class="app-header">
        <div>
          <div class="app-name">Aonla Hub</div>
          <div class="app-tagline">Everything You Need</div>
        </div>
        <div class="header-right">Created with ❤️</div>
      </div>

      <div class="body">

        <div class="hero">
          <span class="hero-icon">✨</span>
          <h2>Your Orders are our First Priority</h2>
          <p>Aonla Hub: Your All-In-One Aonla Store for Every Product!</p>
          <div class="hero-badge">⚡ Best Aonla's Online Store</div>
        </div>

        <div class="section-label">
          <h3>✨ Collection</h3>
          <span>Tap a category</span>
        </div>

        <div class="pills-wrap">
          <div class="pill" onclick="selectCat('food',this)">🍱 Food</div>
          <div class="pill" onclick="selectCat('grocery',this)">🛒 Grocery</div>
          <div class="pill" onclick="selectCat('pharmacy',this)">💊 Pharmacy</div>
          <div class="pill" onclick="selectCat('gifts',this)">🎁 Gifts</div>
          <div class="pill" onclick="selectCat('fashion',this)">👕 Fashion</div>
          <div class="pill" onclick="selectCat('electronics',this)">🔌 Electronics</div>
        </div>

        <div class="default-hint" id="default-hint">
          <p>👆 Tap any category above<br>to explore products and order</p>
        </div>

        <div class="cat-panel" id="panel-food">
          <div class="cat-banner">
            <span class="cat-big-emoji">🍱</span>
            <h3>Food</h3>
            <p>Fresh meals, snacks &amp; local kitchen delights delivered hot to your door.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

        <div class="cat-panel" id="panel-grocery">
          <div class="cat-banner">
            <span class="cat-big-emoji">🛒</span>
            <h3>Grocery &amp; Daily Essentials</h3>
            <p>Rice, dal, oil, and everything you need for daily life — all in one place.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

        <div class="cat-panel" id="panel-pharmacy">
          <div class="cat-banner">
            <span class="cat-big-emoji">💊</span>
            <h3>Pharmacy &amp; Healthcare</h3>
            <p>Medicines, supplements, and healthcare products from trusted local stores.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

        <div class="cat-panel" id="panel-gifts">
          <div class="cat-banner">
            <span class="cat-big-emoji">🎁</span>
            <h3>Gifts &amp; Lifestyle</h3>
            <p>Unique gifts and lifestyle products perfect for every occasion.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

        <div class="cat-panel" id="panel-fashion">
          <div class="cat-banner">
            <span class="cat-big-emoji">👕</span>
            <h3>Fashion &amp; Clothing</h3>
            <p>Trendy clothes, kurtas, and accessories for men, women, and kids.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

        <div class="cat-panel" id="panel-electronics">
          <div class="cat-banner">
            <span class="cat-big-emoji">🔌</span>
            <h3>Electronics &amp; Home Appliances</h3>
            <p>Gadgets, cables, fans, bulbs and home appliances at the best prices.</p>
            <a class="download-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
              Download Now to See Items &amp; Order
            </a>
            <p class="hint">App mein poori list aur WhatsApp order available hai</p>
          </div>
        </div>

      </div>
      <!-- end body -->

      <div class="modal-overlay" id="basket-modal" onclick="closeModal('basket-modal')">
        <div class="modal-sheet" onclick="event.stopPropagation()">
          <div class="modal-handle"></div>
          <span class="modal-icon">🛒🔒</span>
          <h4>Basket is Locked</h4>
          <p>Download the Aonla Hub app to add items, manage your basket, and place orders directly on WhatsApp!</p>
          <a class="modal-dl-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Now to Access Basket
          </a>
          <span class="modal-close" onclick="closeModal('basket-modal')">✕ Close</span>
        </div>
      </div>

      <div class="modal-overlay" id="getapp-modal" onclick="closeModal('getapp-modal')">
        <div class="modal-sheet" onclick="event.stopPropagation()">
          <div class="modal-handle"></div>
          <span class="modal-icon">📲</span>
          <h4>Download Aonla Hub</h4>
          <p>Get the full Aonla Hub app — browse all products, add to basket, and order instantly via WhatsApp!</p>
          <a class="modal-dl-btn" href="YOUR_APK_LINK_HERE" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
            Download Aonla Hub Now
          </a>
          <span class="modal-close" onclick="closeModal('getapp-modal')">✕ Close</span>
        </div>
      </div>

      <div class="bottom-nav">
        <div class="nav-btn active" id="nav-collection" onclick="showCollection()">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6z"/>
          </svg>
          <span class="nav-label">Collection</span>
        </div>

        <div class="nav-btn" id="nav-basket" onclick="openModal('basket-modal')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/>
            <line x1="3" y1="6" x2="21" y2="6"/>
            <path d="M16 10a4 4 0 01-8 0"/>
          </svg>
          <span class="nav-label">Basket</span>
        </div>

        <div class="nav-btn" id="nav-getapp" onclick="openModal('getapp-modal')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="5" y="2" width="14" height="20" rx="2"/>
            <line x1="12" y1="18" x2="12" y2="18" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <span class="nav-label">Get App</span>
        </div>
      </div>

      <div class="home-indicator"></div>
    </div>
  </div>
</div>

<script>
  /* ── MOBILE ── */
  function selectCat(id, el) {
    document.querySelectorAll('.pill').forEach(function(p){ p.classList.remove('active'); });
    el.classList.add('active');
    document.getElementById('default-hint').style.display = 'none';
    document.querySelectorAll('.cat-panel').forEach(function(p){ p.classList.remove('visible'); });
    var panel = document.getElementById('panel-' + id);
    if (panel) panel.classList.add('visible');
    document.querySelectorAll('.nav-btn').forEach(function(b){ b.classList.remove('active'); });
    document.getElementById('nav-collection').classList.add('active');
  }

  function showCollection() {
    document.querySelectorAll('.nav-btn').forEach(function(b){ b.classList.remove('active'); });
    document.getElementById('nav-collection').classList.add('active');
  }

  function openModal(id) {
    document.querySelectorAll('.nav-btn').forEach(function(b){ b.classList.remove('active'); });
    if (id === 'basket-modal') document.getElementById('nav-basket').classList.add('active');
    if (id === 'getapp-modal') document.getElementById('nav-getapp').classList.add('active');
    document.getElementById(id).classList.add('open');
  }

  function closeModal(id) {
    document.getElementById(id).classList.remove('open');
    document.querySelectorAll('.nav-btn').forEach(function(b){ b.classList.remove('active'); });
    document.getElementById('nav-collection').classList.add('active');
  }

  /* ── DESKTOP ── */
  function dTab(tab) {
    document.getElementById('d-tab-collection').style.display = tab === 'collection' ? 'block' : 'none';
    document.getElementById('d-tab-basket').style.display = tab === 'basket' ? 'block' : 'none';
    document.getElementById('d-nav-collection').classList.toggle('active', tab === 'collection');
    document.getElementById('d-nav-basket').classList.toggle('active', tab === 'basket');
  }

  function dOpenLocked() {
    dTab('basket');
  }

  function dSelectCat(id, el) {
    document.querySelectorAll('.pills-wrap-d .pill-d').forEach(function(p){ p.classList.remove('active'); });
    el.classList.add('active');
    document.getElementById('d-default-hint').style.display = 'none';
    document.querySelectorAll('[id^="d-panel-"]').forEach(function(p){ p.classList.remove('visible'); });
    document.getElementById('d-panel-' + id).classList.add('visible');
  }
</script>
</body>
</html>
"""
c.html(
    html,
    height=900,      # apne page ke hisaab se badha lena
    scrolling=False
)
