import streamlit as st
import streamlit.components.v1 as components
import json
from pathlib import Path

QUESTIONS = [
    {"icon": "📖", "title": "Lecture Review",           "prompt": "How often do you review the previous lecture before attending the next class?",  "options": ["Never", "Rarely", "Sometimes", "Always"]},
    {"icon": "📝", "title": "Note-Taking",               "prompt": "How do you usually take notes during lectures?",                                  "options": ["Do not take notes", "Write occasionally", "Write key points", "Detailed notes with questions"]},
    {"icon": "⏱️", "title": "Free Gap Time",             "prompt": "What do you usually do during a 3-hour free gap between classes?",               "options": ["Phone or social media", "Rest or hang out", "Do light revision", "Structured study plan"]},
    {"icon": "🏫", "title": "Class Attendance",          "prompt": "How many classes do you skip in a typical week?",                                 "options": ["More than 3 classes", "2–3 classes", "1 class", "Do not skip any"]},
    {"icon": "📅", "title": "Assignment Start",          "prompt": "When do you usually start working on an assignment after it is given?",           "options": ["Night before deadline", "2–3 days before", "About 1 week before", "Immediately after assigned"]},
    {"icon": "📱", "title": "Social Media During Study", "prompt": "How much time do you spend on social media during study time?",                   "options": ["More than 3 hours", "1–2 hours", "Less than 1 hour", "Almost none"]},
    {"icon": "📋", "title": "Revision Plan",             "prompt": "How structured is your revision plan before exams?",                              "options": ["No plan", "Basic or unclear plan", "Clear plan, usually follow it", "Detailed plan, always follow it"]},
    {"icon": "🔁", "title": "Post-Class Review",         "prompt": "When do you usually review lecture material after class?",                        "options": ["Never review", "Only before exams", "Within a few days", "Same day or next day"]},
    {"icon": "🤝", "title": "Group Study",               "prompt": "How often do you participate in group study or academic discussions?",            "options": ["Never", "Rarely", "Sometimes", "Regularly"]},
    {"icon": "🗓️", "title": "Time Management",          "prompt": "How would you rate your current time management for studies?",                    "options": ["Very poor", "Poor", "Average", "Good"]},
]

def main():
    import base64
    _video_src = Path("assets/video/roslan_vid.mp4")
    _video_b64 = ""
    if _video_src.exists():
        with open(_video_src, "rb") as _vf:
            _video_b64 = base64.b64encode(_vf.read()).decode("utf-8")

    QUESTIONS_JSON = json.dumps(QUESTIONS)
    VIDEO_B64 = _video_b64


    if VIDEO_B64:
        VIDEO_HTML = (
            '<div style="'
            'width:100%;'
            'max-width:280px;'
            'margin:0 auto;'
            'border:1.5px solid #b0b0b0;'
            'border-radius:12px;'
            'overflow:hidden;'
            'box-shadow:0 2px 8px rgba(0,0,0,0.10);">'
            '<div style="width:100%;height:480px;overflow:hidden;background:#000;">'
            '<video controls style="width:100%;height:100%;object-fit:contain;display:block;background:#000;">'
            f'<source src="data:video/mp4;base64,{VIDEO_B64}" type="video/mp4">'
            '</video>'
            '</div>'
            '<div style="'
            'padding:12px 16px;'
            'background:linear-gradient(135deg,#e8e8e8 0%,#f5f5f5 40%,#c8c8c8 70%,#e0e0e0 100%);'
            'text-align:center;">'
            '<div style="font-size:15px;font-weight:800;color:#2c2c2c;margin-bottom:3px;">'
            '🎬 The Smart Way to Study'
            '</div>'
            '<div style="font-size:12px;color:#555555;">'
            'A short guide on studying smarter, not harder.'
            '</div>'
            '</div>'
            '</div>'
        )
    else:
        VIDEO_HTML = (
            '<div style="'
            'width:100%;'
            'border:1.5px solid #b0b0b0;'
            'border-radius:12px;'
            'overflow:hidden;'
            'box-shadow:0 2px 8px rgba(0,0,0,0.10);">'
            '<div style="width:100%;background:#1e293b;'
            'display:flex;align-items:center;justify-content:center;padding:40px 10px;">'
            '<p style="color:#94a3b8;font-size:12px;text-align:center;padding:10px;">'
            '📹 Video not found.<br>Ensure <code>assets/video/roslan_vid.mp4</code>'
            '<br>exists in your project folder.</p>'
            '</div>'
            '<div style="'
            'padding:12px 16px;'
            'background:linear-gradient(135deg,#e8e8e8 0%,#f5f5f5 40%,#c8c8c8 70%,#e0e0e0 100%);'
            'text-align:center;">'
            '<div style="font-size:15px;font-weight:800;color:#2c2c2c;margin-bottom:3px;">'
            '🎬 The Smart Way to Study'
            '</div>'
            '<div style="font-size:12px;color:#555555;">'
            'A short guide on studying smarter, not harder.'
            '</div>'
            '</div>'
            '</div>'
        )
        

    APP_HTML = f"""<!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <style>
    /* ── Reset ── */
    *{{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',system-ui,sans-serif;}}
    body{{background:transparent;padding:0 2px 32px;}}

    /* ── Header ── */
    #hdr{{
      text-align:center;
      background:linear-gradient(135deg,#3b4fe4 0%,#5b6ef5 100%);
      color:#fff;font-size:3rem;font-weight:900;
      padding:1.5rem 1.5rem;border-radius:20px;
      margin-bottom:14px;margin-left:-2px;margin-right:-2px;
      box-shadow:0 8px 24px rgba(59,79,228,0.35);
      text-shadow:2px 2px 4px rgba(0,0,0,0.2);letter-spacing:1px;
    }}
    #hdr .sub{{font-size:1.30rem;font-weight:400;color:#BBDEFB;margin-top:4px;letter-spacing:2px;}}

    /* ── Info cards ── */
    .info-cards{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px;}}
    .ic{{border-radius:12px;padding:.9rem 1rem;border-left:4px solid;}}
    .ic-blue{{background:linear-gradient(135deg,#EEF2FF,#E0E7FF);border-color:#6366F1;}}
    .ic-amber{{background:linear-gradient(135deg,#FFFBEB,#FEF3C7);border-color:#F59E0B;}}
    .ic-title{{font-weight:700;font-size:0.85rem;margin-bottom:3px;}}
    .ic-blue .ic-title{{color:#3730A3;}}.ic-amber .ic-title{{color:#92400E;}}
    .ic-body{{font-size:0.78rem;line-height:1.5;}}
    .ic-blue .ic-body{{color:#4338CA;}}.ic-amber .ic-body{{color:#78350F;}}

    /* ── Progress ── */
    #prog-label{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;}}
    #prog-label span{{font-size:13px;color:#64748B;font-weight:600;}}
    #prog-label strong{{font-size:13px;color:#6366F1;font-weight:700;}}
    #prog-wrap{{background:#E2E8F0;border-radius:999px;height:10px;margin-bottom:18px;overflow:hidden;}}
    #prog-bar{{height:10px;border-radius:999px;background:linear-gradient(90deg,#6366F1,#818CF8);width:0%;transition:width .45s cubic-bezier(.4,0,.2,1);}}

    /* ── Question cards ── */
    .q-card{{background:#fff;border:1.5px solid #E2E8F0;border-radius:20px;padding:18px 20px 16px;margin-bottom:12px;transition:border-color .25s,box-shadow .25s;}}
    .q-card.done{{border-color:#6EE7B7;box-shadow:0 4px 18px rgba(16,185,129,.1);}}
    .q-meta{{display:flex;align-items:center;gap:10px;margin-bottom:8px;}}
    .q-icon{{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,#EEF2FF,#E0E7FF);display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}}
    .q-card.done .q-icon{{background:linear-gradient(135deg,#D1FAE5,#A7F3D0);}}
    .q-num{{font-size:10px;font-weight:700;color:#6366F1;letter-spacing:1px;text-transform:uppercase;}}
    .q-title{{font-size:15px;font-weight:800;color:#1E293B;}}
    .q-prompt{{font-size:13.5px;color:#475569;line-height:1.5;margin-bottom:14px;}}
    .opts{{display:grid;grid-template-columns:1fr 1fr;gap:8px;}}
    .opt{{position:relative;background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:14px;padding:10px 12px;cursor:pointer;display:flex;align-items:center;gap:8px;transition:all .2s;}}
    .opt:hover{{background:#F1F5F9;border-color:#CBD5E1;}}
    .opt.sel{{background:#EEF2FF;border-color:#6366F1;box-shadow:0 2px 8px rgba(99,102,241,0.15);}}
    .opt-dot{{width:16px;height:16px;border-radius:50%;border:2px solid #CBD5E1;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
    .opt.sel .opt-dot{{border-color:#6366F1;}}
    .opt-dot-inner{{width:7px;height:7px;border-radius:50%;background:#6366F1;transform:scale(0);transition:transform .2s;}}
    .opt.sel .opt-dot-inner{{transform:scale(1);}}
    .opt-label{{font-size:13px;font-weight:600;color:#475569;line-height:1.3;}}
    .opt.sel .opt-label{{color:#3730A3;}}
    .answered-tag{{margin-left:auto;font-size:10px;font-weight:700;color:#10B981;opacity:0;transition:opacity .2s;}}
    .q-card.done .answered-tag{{opacity:1;}}

    /* ── Submit button ── */
    #sub-btn{{width:100%;background:#E2E8F0;color:#94A3B8;border:none;border-radius:16px;padding:16px;font-size:15px;font-weight:800;cursor:not-allowed;margin-top:8px;transition:all .3s;}}
    #sub-btn.rdy{{background:linear-gradient(135deg,#6366F1,#4F46E5);color:#fff;cursor:pointer;box-shadow:0 8px 18px rgba(99,102,241,0.25);}}
    #sub-btn.rdy:hover{{transform:translateY(-2px);}}

    /* ── Confetti particles ── */
    .ptcl{{position:absolute;width:6px;height:6px;border-radius:50%;pointer-events:none;opacity:0;animation:pop .65s ease-out forwards;}}
    @keyframes pop{{0%{{transform:translate(0,0) scale(1);opacity:1;}}100%{{transform:translate(var(--tx),var(--ty)) scale(0);opacity:0;}}}}

    /* ── Divider before results ── */
    #results-divider{{display:none;border:none;border-top:2px solid #E2E8F0;margin:28px 0 20px;}}

    /* ── Results section (appended below, same page) ── */
    #results-section{{display:none;}}

    /* ── Level card ── */
    .level-card{{border-radius:16px;padding:16px 18px;margin-bottom:14px;border:1px solid;}}
    .level-card h4{{margin-bottom:5px;display:flex;align-items:center;gap:8px;font-size:.95rem;}}
    .level-card p{{margin-top:3px;margin-bottom:0;color:#111827;font-size:0.87rem;line-height:1.6;}}
    .level-name{{font-weight:800;letter-spacing:0.5px;}}

    /* ── Gauge ── */
    .res-h3{{font-size:1rem;font-weight:700;color:#1E293B;margin:14px 0 8px;}}
    .gauge-wrap{{position:relative;height:14px;border-radius:999px;background:linear-gradient(90deg,#ef4444 0%,#fb923c 35%,#facc15 60%,#a3e635 80%,#22c55e 100%);box-shadow:inset 0 1px 3px rgba(0,0,0,0.2);margin:8px 0 4px;}}
    .gauge-dot{{position:absolute;top:0;width:14px;height:14px;border-radius:50%;background:#fff;border:2px solid #111827;box-shadow:0 0 5px rgba(0,0,0,0.3);}}
    .gauge-labels{{display:flex;justify-content:space-between;font-size:11px;color:#4b5563;margin-top:3px;}}
    .gauge-note{{text-align:center;font-size:10px;color:#6b7280;margin-top:2px;}}

    /* ── Factor bars ── */
    .factor-bars{{display:flex;flex-direction:column;gap:10px;margin-top:8px;}}
    .factor-row{{display:flex;align-items:center;gap:8px;}}
    .factor-label{{font-size:11px;font-weight:700;color:#374151;width:140px;flex-shrink:0;}}
    .factor-bar-bg{{flex:1;background:#F1F5F9;border-radius:999px;height:20px;overflow:hidden;}}
    .factor-bar-fill{{height:100%;border-radius:999px;display:flex;align-items:center;padding-left:6px;font-size:10px;font-weight:700;color:#fff;transition:width 0.8s cubic-bezier(.4,0,.2,1);}}
    .factor-score{{font-size:12px;font-weight:800;color:#374151;width:24px;text-align:right;}}

    /* ── Expander ── */
    .expander-btn{{width:100%;background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:12px;padding:10px 14px;text-align:left;font-size:13px;font-weight:700;color:#374151;cursor:pointer;display:flex;justify-content:space-between;align-items:center;margin-top:6px;}}
    .expander-btn:hover{{background:#F1F5F9;}}
    .expander-content{{background:#F8FAFC;border:1.5px solid #E2E8F0;border-top:none;border-radius:0 0 12px 12px;padding:12px 14px;font-size:13px;color:#374151;line-height:1.7;display:none;}}
    .expander-content.open{{display:block;}}
    .expander-content ul{{padding-left:20px;}}
    .expander-content li{{margin-bottom:5px;}}
    .caption{{font-size:11px;color:#9CA3AF;margin-top:10px;padding:7px 10px;background:#F9FAFB;border-radius:8px;border-left:3px solid #E5E7EB;}}

    /* ── What next ── */
    .what-next{{font-size:.9rem;font-weight:800;color:#1E293B;margin:14px 0 10px;}}
    .game-tabs{{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap;}}
    .game-tab{{padding:7px 14px;border-radius:10px;border:2px solid #E2E8F0;background:#fff;font-size:12px;font-weight:700;color:#64748B;cursor:pointer;transition:all .2s;}}
    .game-tab.active{{background:#6366F1;border-color:#6366F1;color:#fff;}}
    .game-frame{{border:none;width:100%;border-radius:12px;display:block;}}
    .tips-card{{background:#FFF9C4;border-left:4px solid #FBC02D;padding:14px 18px;border-radius:8px;margin-bottom:10px;font-size:13px;color:#424242;line-height:1.8;}}
    .tips-card h4{{margin-top:0;color:#F57C00;font-weight:700;margin-bottom:8px;}}
    .tips-card p{{margin-bottom:0;}}.tips-card p+p{{margin-top:10px;}}
    .quote-card{{background:blueviolet;padding:9px;border-radius:8px;text-align:center;margin-top:10px;}}
    .quote-card p{{font-size:.95rem;font-weight:700;color:#fff;margin:0;line-height:1.6;}}

    /* On Track two-column layout */
    .on-track-grid{{display:grid;grid-template-columns:1fr 1fr;gap:2px;align-items:start;}}
    .on-track-left{{min-width:0;}}
    .on-track-right{{min-width:0;}}
    @media(max-width:600px){{
      .on-track-grid{{grid-template-columns:1fr;}}
    }}
    .rebuild-card{{border:2px solid #3b82f6;border-radius:12px;padding:18px;background:#eff6ff;margin-bottom:14px;}}
    .rebuild-card h4{{margin-top:0;color:#1e40af;font-size:.95rem;font-weight:700;margin-bottom:8px;}}
    .rebuild-card ul{{padding-left:18px;line-height:1.9;color:#1e293b;font-size:13px;}}
    .resources-card{{border:3px solid #dc2626;border-radius:12px;padding:18px;background:#fef2f2;}}
    .resources-card h3{{margin-top:0;color:#991b1b;font-size:1rem;font-weight:700;margin-bottom:10px;}}
    .resources-card ul{{padding-left:0;list-style:none;color:#1e293b;font-size:13px;line-height:1.8;}}
    .resources-card li{{margin-bottom:10px;}}.resources-card a{{color:#2563eb;}}
    .resources-card .footer{{text-align:center;font-weight:800;font-size:.95rem;color:#991b1b;margin-top:14px;}}
    .resources-card .builds{{margin-top:10px;padding-left:18px;}}                              

    /* ── Retake button ── */
    .retake-btn{{width:100%;margin-top:20px;background:#F1F5F9;border:2px solid #CBD5E1;border-radius:16px;padding:14px;font-size:14px;font-weight:800;color:#64748B;cursor:pointer;transition:all .2s;}}
    .retake-btn:hover{{background:#E2E8F0;color:#374151;}}
    </style>
    </head>
    <body>

    <!-- Header -->
    <div id="hdr">
      🙋 Know Yourself
      <div class="sub">Discover your academic performance level in 10 honest questions</div>
    </div>

    <!-- Info cards -->
    <div class="info-cards">
      <div class="ic ic-blue">
        <div class="ic-title">📋 How It Works</div>
        <div class="ic-body">Answer 10 honest questions about your real study habits. We'll predict your performance level and give you a personalised action plan.</div>
      </div>
      <div class="ic ic-amber">
        <div class="ic-title">⚠️ Important</div>
        <div class="ic-body">Please answer <b>all 10 questions</b> honestly. Responses are anonymous and not stored.</div>
      </div>
    </div>

    <!-- Progress -->
    <div id="prog-label"><span id="prog-text">0 / 10 answered</span><strong id="prog-pct">0%</strong></div>
    <div id="prog-wrap"><div id="prog-bar"></div></div>

    <!-- Quiz cards -->
    <div id="quiz-cont"></div>

    <!-- Predict button -->
    <button id="sub-btn" disabled>⏳ Complete all questions</button>

    <!-- Divider shown after submit -->
    <hr id="results-divider">

    <!-- Results section — shown below quiz after submit, same continuous page -->
    <div id="results-section">
      <div id="level-card" class="level-card"></div>
      <div class="res-h3">🧭 Where you are on the performance scale</div>
      <div style="padding:0 4px;">
        <div class="gauge-wrap"><div class="gauge-dot" id="gauge-dot"></div></div>
        <div class="gauge-labels"><span>At Risk</span><span>On Track</span><span>High Performer</span></div>
        <div class="gauge-note">● your current position on the performance scale</div>
      </div>
      <div class="res-h3">💡 What's driving your result?</div>
      <div class="factor-bars" id="factor-bars"></div>
      <p style="font-size:11px;color:#6B7280;margin-top:6px;">The longer the bar, the more that area influences your profile.</p>
      <div class="res-h3">Understanding your result</div>
      <button class="expander-btn" onclick="toggleExp()">
        <span>Click To Read Explanation</span><span id="exp-arrow">▼</span>
      </button>
      <div class="expander-content" id="exp-content"></div>
      <div class="caption">⚠️ This screening is only for reflection and does not replace academic advice from your lecturers or advisors.</div>
      <div class="what-next">Based on your performance level, here are some recommended actions</div>
      <div id="what-next-content"></div>
      <button class="retake-btn" onclick="retake()">🔄 Retake the Quiz</button>
    </div>

    <script>
    const QS = {QUESTIONS_JSON};
    const ans = {{}};

    // ── Build quiz cards ──────────────────────────────────────────────────────────
    function build() {{
      const cont = document.getElementById('quiz-cont');
      cont.innerHTML = '';
      QS.forEach((q, i) => {{
        const card = document.createElement('div');
        card.className = 'q-card'; card.id = 'qc' + i;

        const optsDiv = document.createElement('div');
        optsDiv.className = 'opts';
        q.options.forEach((o, j) => {{
          const t = document.createElement('div');
          t.className = 'opt'; t.id = 'op' + i + '_' + j;
          t.innerHTML = '<div class="opt-dot"><div class="opt-dot-inner"></div></div><span class="opt-label"></span>';
          t.querySelector('.opt-label').textContent = o;
          t.addEventListener('click', () => pick(i, j, t));
          optsDiv.appendChild(t);
        }});

        const meta = document.createElement('div'); meta.className = 'q-meta';
        const icon = document.createElement('div'); icon.className = 'q-icon'; icon.textContent = q.icon;
        const txt  = document.createElement('div');
        const num  = document.createElement('div'); num.className = 'q-num'; num.textContent = 'Question ' + (i+1) + ' of ' + QS.length;
        const ttl  = document.createElement('div'); ttl.className = 'q-title'; ttl.textContent = q.title;
        txt.appendChild(num); txt.appendChild(ttl);
        const tag  = document.createElement('span'); tag.className = 'answered-tag'; tag.textContent = '✓ Answered';
        meta.appendChild(icon); meta.appendChild(txt); meta.appendChild(tag);

        const prm = document.createElement('div'); prm.className = 'q-prompt'; prm.textContent = q.prompt;
        card.appendChild(meta); card.appendChild(prm); card.appendChild(optsDiv);
        cont.appendChild(card);
      }});
      sync();
    }}

    // ── Pick answer ───────────────────────────────────────────────────────────────
    function pick(qi, oi, el) {{
      const prev = ans[qi];
      if (prev === oi) {{
        delete ans[qi];
        el.classList.remove('sel');
        document.getElementById('qc' + qi).classList.remove('done');
      }} else {{
        if (prev !== undefined) {{
          const pe = document.getElementById('op' + qi + '_' + prev);
          if (pe) pe.classList.remove('sel');
        }}
        ans[qi] = oi;
        el.classList.add('sel');
        document.getElementById('qc' + qi).classList.add('done');
        burst(el);
      }}
      sync();
    }}

    // ── Confetti burst ────────────────────────────────────────────────────────────
    function burst(el) {{
      const cols = ['#10B981','#6366F1','#F59E0B','#EC4899','#3B82F6','#F97316'];
      for (let i = 0; i < 10; i++) {{
        const p = document.createElement('div'); p.className = 'ptcl';
        const a = (Math.PI * 2 / 10) * i, d = 28 + Math.random() * 26;
        p.style.cssText = 'left:' + (38 + Math.random()*24) + '%;top:' + (38 + Math.random()*24) + '%;background:' + cols[i%cols.length] + ';--tx:' + Math.cos(a)*d + 'px;--ty:' + Math.sin(a)*d + 'px;animation-delay:' + (Math.random()*.08) + 's;';
        el.appendChild(p);
        setTimeout(() => p.remove(), 650);
      }}
    }}

    // ── Sync progress bar + button ────────────────────────────────────────────────
    function sync() {{
      const n = Object.keys(ans).length;
      const pct = Math.round((n / QS.length) * 100);
      document.getElementById('prog-bar').style.width = pct + '%';
      document.getElementById('prog-text').textContent = n + ' / ' + QS.length + ' answered';
      document.getElementById('prog-pct').textContent = pct + '%';
      const btn = document.getElementById('sub-btn');
      if (n === QS.length) {{
        btn.classList.add('rdy'); btn.disabled = false;
        btn.textContent = '🤖 Predict My Performance Level';
      }} else {{
        btn.classList.remove('rdy'); btn.disabled = true;
        btn.textContent = '⏳ ' + (QS.length - n) + ' question(s) remaining...';
      }}
    }}

    // ── Predict button ────────────────────────────────────────────────────────────
    document.getElementById('sub-btn').addEventListener('click', function() {{
      if (!this.classList.contains('rdy')) return;
      this.textContent = '⏳ Analysing...';
      this.disabled = true;
      this.classList.remove('rdy');
      setTimeout(showResults, 600);
    }});

    // ── Classify ──────────────────────────────────────────────────────────────────
    function classify(t) {{
      return t <= 10 ? 'At Risk' : t <= 20 ? 'On Track' : 'High Performer';
    }}

    // ── Show results — appended BELOW quiz on the same continuous page ─────────────
    // No screen switch. No scroll to top. Results just appear right below.
    // User naturally scrolls down to read — exactly like a normal webpage.
    function showResults() {{
      const scores = QS.map((_, i) => ans[i] || 0);
      const total  = scores.reduce((a, b) => a + b, 0);
      const level  = classify(total);

      // Reveal divider + results section below the quiz
      document.getElementById('results-divider').style.display = 'block';
      document.getElementById('results-section').style.display = 'block';

      // Smooth scroll to the divider so user sees results start right away
      document.getElementById('results-divider').scrollIntoView({{ behavior: 'smooth', block: 'start' }});

      // ── Level card ──────────────────────────────────────────────────
      const cfgMap = {{
        'High Performer': {{ bg:'#ecfdf5', border:'#6ee7b7', color:'#047857', icon:'🟢',
          msg:'Your responses reflect strong, intentional study habits. Your main next step is to stay balanced and avoid burnout.' }},
        'On Track':       {{ bg:'#fffbeb', border:'#fbbf24', color:'#92400e', icon:'🟠',
          msg:'You have decent foundations, but some habits are still limiting your ability to perform at your best consistently.' }},
        'At Risk':        {{ bg:'#fef2f2', border:'#f87171', color:'#b91c1c', icon:'🔴',
          msg:'Your current habits show a pattern linked to low consistency, procrastination, and weaker academic control. Many students improve within one semester when they focus on consistency before intensity.' }},
      }};
      const cfg  = cfgMap[level];
      const card = document.getElementById('level-card');
      card.style.backgroundColor = cfg.bg;
      card.style.borderColor     = cfg.border;
      card.innerHTML = `
        <h4>
          <span>${{cfg.icon}}</span>
          <span class="level-name" style="color:${{cfg.color}}">Your Performance Level: ${{level.toUpperCase()}}</span>
        </h4>
        <p>${{cfg.msg}}</p>`;

      // ── Gauge ───────────────────────────────────────────────────────
      const pct = Math.max(2, Math.min(98, (total / 30) * 100));
      document.getElementById('gauge-dot').style.left = 'calc(' + pct + '% - 7px)';

      // ── Factor bars ─────────────────────────────────────────────────
      const factors = [
        {{ label:'Class Engagement',    val: scores[0]+scores[1]+scores[3], max:9,  color:'#534AB7' }},
        {{ label:'Time Management',     val: scores[4]+scores[6]+scores[9], max:9,  color:'#BA7517' }},
        {{ label:'Focus & Distraction', val: scores[2]+scores[5],           max:6,  color:'#E24B4A' }},
        {{ label:'Revision Discipline', val: scores[7]+scores[8],           max:6,  color:'#1D9E75' }},
      ];
      const fb = document.getElementById('factor-bars');
      fb.innerHTML = '';
      factors.forEach(f => {{
        const p2 = Math.round((f.val / f.max) * 100);
        fb.innerHTML += `
          <div class="factor-row">
            <div class="factor-label">${{f.label}}</div>
            <div class="factor-bar-bg">
              <div class="factor-bar-fill" style="width:${{p2}}%;background:${{f.color}};">${{f.val}}</div>
            </div>
            <div class="factor-score">${{f.val}}</div>
          </div>`;
      }});

      // ── Expander text ───────────────────────────────────────────────
      document.getElementById('exp-content').innerHTML = {{
        'High Performer': '<ul><li>Your responses reflect <strong>strong and intentional study habits</strong>.</li><li>You are likely benefiting from structure, consistency, and follow-through.</li><li>Your next challenge is staying sustainable and avoiding burnout.</li></ul>',
        'On Track':       '<ul><li>You already have a <strong>usable academic foundation</strong>.</li><li>Your biggest opportunity is upgrading the way you revise and manage your time.</li><li>Small method improvements can move you into the high-performance tier.</li></ul>',
        'At Risk':        '<ul><li>Your study pattern currently shows <strong>low consistency</strong>.</li><li>Attendance, starting early, and reducing distraction are the biggest priorities.</li><li>The goal now is not perfection. It is rebuilding routine.</li></ul>',
      }}[level];

      // ── What next ───────────────────────────────────────────────────
      const wn = document.getElementById('what-next-content');

      if (level === 'High Performer') {{
        wn.innerHTML = `
          <p style="font-size:13px;color:#374151;margin-bottom:10px;">🎮 <strong>Take a Mental Break: Play a Game!</strong><br>
          You're doing great! Here's a fun game to relax and recharge.</p>
          <div class="game-tabs">
            <button class="game-tab active" onclick="switchGame('gravity',this)">🚀 Gravity Jump</button>
            <button class="game-tab" onclick="switchGame('memory',this)">🧠 Memory Puzzle</button>
            <button class="game-tab" onclick="switchGame('ttt',this)">✏️ Tic-Tac-Toe</button>
          </div>
          <div id="game-container"></div>`;
        switchGame('gravity', document.querySelector('.game-tab.active'));

      }} else if (level === 'On Track') {{
        wn.innerHTML = `
          <div class="on-track-grid">
            <div class="on-track-left">
              <div class="tips-card">
                <h4>Little Tips for Big Progress</h4>
                <p>This guide helps you manage academic pressure while taking care of your well-being.
                   It focuses on recognizing your effort and using simple strategies to improve both your learning and balance.</p>
                <p><b>Recognize Your Pressure.</b> You might feel pressure from your studies and other responsibilities.
                   Even if you seem fine, you could feel tired or close to burnout. It is important to cut down on
                   unnecessary busy work and focus on what really helps you.</p>
                <p><b>Use Your Gap Time Wisely.</b> The time between your classes is often wasted. Try using about
                   45 minutes to review what you just learned. This helps you understand better and reduces the
                   work you need to do later at home.</p>
                <p><b>Practice Active Recall.</b> Simply writing notes without thinking deeply is not very effective.
                   Instead, try Active Recall. Close your notes and explain the topic in your own words.
                   This helps you understand it better and remember it longer.</p>
                <p><b>Follow the 50/10 Focus Rule.</b> Distractions can make studying harder. Use the 50/10 rule.
                   Focus for 50 minutes, then take 10 minutes to rest. This helps you stay focused and keeps
                   you from feeling too tired.</p>
                <p><b>You've Got This.</b> You already have the ability to succeed. By using these tips, you can
                   study smarter, manage your time better, and keep a healthy balance in your life.</p>
              </div>
              <div class="quote-card">
                <p>"Small steps done consistently can make a big difference."</p>
              </div>
            </div>
            <div class="on-track-right">
              {VIDEO_HTML}
            </div>
          </div>`;

      }} else {{
        wn.innerHTML = `
          <div class="rebuild-card">
            <h4>🆘 Rebuild Structure First</h4>
            <ul>
              <li><strong>Attend every class possible.</strong> Showing up is your fastest improvement lever.</li>
              <li><strong>Start tasks on day one.</strong> Early contact reduces procrastination pressure.</li>
              <li><strong>Study with phone away.</strong> Focus for 25 minutes first, break later.</li>
              <li><strong>Get support early.</strong> Talk to your lecturer or academic advisor.</li>
            </ul>
          </div>
          <div class="resources-card">
            <h3>Training &amp; Study Skills Workshops</h3>
            <ul>
              <li>🏫 <strong>System &amp; Skills Training Concept Sdn Bhd</strong><br>
                  👉 Time management, productivity, learning strategies<br>
                  🔗 <a href="https://www.google.com/search?q=System+%26+Skills+Training+Concept+Sdn+Bhd" target="_blank">Search on Google</a></li>
              <li>🏫 <strong>Skills Training &amp; Consultancy Sdn Bhd</strong><br>
                  👉 Personal development, discipline &amp; consistency<br>
                  🔗 <a href="https://www.google.com/search?q=Skills+Training+%26+Consultancy+Sdn+Bhd" target="_blank">Search on Google</a></li>
              <li>🏫 <strong>World Skills Academy Sdn Bhd</strong><br>
                  👉 Structured learning systems &amp; skill-building<br>
                  🔗 <a href="https://www.google.com/search?q=World+Skills+Academy+Sdn+Bhd" target="_blank">Search on Google</a></li>
            </ul>
            <p style="color:#1e293b;margin-top:10px;">📌 These centres help students build:</p>
            <ul class="builds">
              <li>⏳ Time management</li>
              <li>🚫 Avoid procrastination</li>
              <li>📚 Study systems (not just "study harder")</li>
            </ul>
            <p class="footer">CONSISTENCY BEATS INTENSITY.</p>
          </div>`;
      }}
    }}

    // ── Game switcher ─────────────────────────────────────────────────────────────
    function switchGame(name, btn) {{
      document.querySelectorAll('.game-tab').forEach(t => t.classList.remove('active'));
      btn.classList.add('active');
      const gc = document.getElementById('game-container');

      const games = {{
        gravity: `<iframe class="game-frame" height="640" srcdoc='<!DOCTYPE html><html><head><style>
          body{{margin:0;display:flex;justify-content:center;align-items:center;background:#0f172a;font-family:sans-serif;overflow:hidden;}}
          #gc{{position:relative;width:420px;height:620px;background:#1e293b;border:4px solid #334155;border-radius:8px;overflow:hidden;}}
          #player{{position:absolute;width:28px;height:28px;background:#3b82f6;border-radius:4px;box-shadow:0 0 10px #3b82f6;transition:background 0.1s;}}
          #player.boosting{{background:#f59e0b;box-shadow:0 0 18px #f59e0b;}}
          .platform{{position:absolute;height:10px;border-radius:5px;}}
          #score{{position:absolute;top:10px;left:10px;color:white;font-size:18px;font-weight:bold;}}
          #bwrap{{position:absolute;top:10px;right:10px;width:80px;height:10px;background:#334155;border-radius:999px;overflow:hidden;}}
          #bbar{{height:100%;width:100%;background:#f59e0b;border-radius:999px;}}
          #blabel{{position:absolute;top:24px;right:10px;color:#f59e0b;font-size:10px;font-weight:700;}}
          #start-msg{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:white;text-align:center;}}
          #game-over{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:white;text-align:center;display:none;}}
          button{{background:#3b82f6;color:white;border:none;padding:10px 20px;border-radius:4px;cursor:pointer;font-size:15px;margin-top:10px;}}
          #tip{{position:absolute;bottom:8px;left:0;right:0;text-align:center;color:#64748b;font-size:10px;}}
        </style></head><body>
        <div id="gc">
          <div id="score">Score: 0</div>
          <div id="bwrap"><div id="bbar"></div></div>
          <div id="blabel">BOOST</div>
          <div id="player"></div>
          <div id="start-msg">
            <h2 style="font-size:1.3rem;">🚀 Gravity Jump</h2>
            <p style="font-size:12px;margin:6px 0;">← → to move</p>
            <p style="font-size:12px;margin:0;color:#f59e0b;">SPACE / ↑ for BOOST!</p>
            <button onclick="startGame()">Start Game</button>
          </div>
          <div id="game-over"><h2>Game Over!</h2><p id="fs"></p><button onclick="startGame()">Try Again</button></div>
          <div id="tip">← → Move | SPACE / ↑ Boost Jump</div>
        </div>
        <script>
          var cont=document.getElementById("gc"),player=document.getElementById("player"),
              sc=document.getElementById("score"),sm=document.getElementById("start-msg"),
              gom=document.getElementById("game-over"),fs=document.getElementById("fs"),
              bb=document.getElementById("bbar");
          var ga=false,score=0,px=196,py=520,vy=0,plats=[],keys={{}},boost=100;
          var GRAV=0.38,JUMP=-11,BST=-22,MOVE=5,BMAX=100;
          window.addEventListener("keydown",function(e){{keys[e.code]=true;e.preventDefault();}});
          window.addEventListener("keyup",function(e){{keys[e.code]=false;}});
          function col(i){{return["#10b981","#6366f1","#f59e0b","#ec4899","#3b82f6"][i%5];}}
          function startGame(){{
            ga=true;score=0;px=196;py=520;vy=0;boost=100;plats=[];
            plats.push({{x:160,y:570,w:100,c:"#10b981"}});
            for(var i=1;i<7;i++)plats.push({{x:Math.random()*(420-90),y:570-i*100,w:70+Math.random()*50,c:col(i)}});
            sm.style.display="none";gom.style.display="none";update();
          }}
          function update(){{
            if(!ga)return;
            if(keys["ArrowLeft"]||keys["KeyA"])px-=MOVE;
            if(keys["ArrowRight"]||keys["KeyD"])px+=MOVE;
            if(px<-28)px=420;if(px>420)px=-28;
            if((keys["Space"]||keys["ArrowUp"]||keys["KeyW"])&&boost>=30&&vy>-5){{
              vy=BST;boost=Math.max(0,boost-30);
              player.classList.add("boosting");
              setTimeout(function(){{player.classList.remove("boosting");}},200);
            }}
            boost=Math.min(BMAX,boost+0.4);
            bb.style.width=(boost/BMAX*100)+"%";
            vy+=GRAV;py+=vy;
            if(vy>0){{
              for(var i=0;i<plats.length;i++){{
                var p=plats[i];
                if(px+28>p.x&&px<p.x+p.w&&py+28>p.y&&py+28<p.y+12){{
                  vy=JUMP;py=p.y-28;boost=Math.min(BMAX,boost+20);
                }}
              }}
            }}
            if(py<200){{
              var d=200-py;py=200;score+=Math.floor(d);
              for(var i=0;i<plats.length;i++){{
                plats[i].y+=d;
                if(plats[i].y>640){{plats[i].y-=680;plats[i].x=Math.random()*(420-90);plats[i].w=70+Math.random()*50;}}
              }}
            }}
            if(py>640){{ga=false;gom.style.display="block";fs.textContent="Final Score: "+score;return;}}
            player.style.left=px+"px";player.style.top=py+"px";sc.textContent="Score: "+score;
            var old=document.querySelectorAll(".platform");
            for(var i=0;i<old.length;i++)old[i].remove();
            for(var i=0;i<plats.length;i++){{
              var d=document.createElement("div");d.className="platform";
              d.style.cssText="left:"+plats[i].x+"px;top:"+plats[i].y+"px;width:"+plats[i].w+"px;background:"+plats[i].c+";box-shadow:0 0 8px "+plats[i].c+"66;";
              cont.appendChild(d);
            }}
            requestAnimationFrame(update);
          }}
        <\\/script></body></html>'></iframe>`,

        memory: `<iframe class="game-frame" height="560" scrolling="no" srcdoc='<!DOCTYPE html><html><head><style>
          html,body{{margin:0;padding:0;height:100%;overflow:hidden;background:#f8fafc;font-family:sans-serif;}}
          body{{display:flex;justify-content:center;align-items:flex-start;padding-top:10px;}}
          #gc{{width:400px;text-align:center;padding:10px 20px 20px;}}
          h3{{margin:0 0 6px;font-size:1.1rem;color:#1e293b;}}
          #status{{font-size:13px;color:#64748b;margin-bottom:4px;}}
          .grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px;}}
          .card{{height:75px;background:#6366f1;border-radius:8px;cursor:pointer;display:flex;justify-content:center;align-items:center;font-size:28px;color:transparent;transition:0.3s;}}
          .card.flipped{{background:white;border:2px solid #6366f1;color:#1e293b;}}
          .card.matched{{background:#10b981;border-color:#10b981;color:white;cursor:default;}}
          button{{background:#6366f1;color:white;border:none;padding:8px 20px;border-radius:4px;cursor:pointer;font-size:14px;margin-top:12px;}}
        </style></head><body><div id="gc"><h3>Memory Match</h3><div id="status">Find all pairs!</div>
        <div class="grid" id="grid"></div><button onclick="init()">New Game</button></div>
        <script>
          var icons=["⭐","🍎","🚀","🌈","💎","🎨","🍕","🐱"];
          var cards=[],flipped=[],matched=0,canFlip=true;
          function init(){{
            var g=document.getElementById("grid");g.innerHTML="";
            cards=icons.concat(icons).sort(function(){{return Math.random()-0.5;}});
            flipped=[];matched=0;canFlip=true;
            document.getElementById("status").textContent="Find all pairs!";
            cards.forEach(function(ic){{
              var c=document.createElement("div");c.className="card";c.dataset.icon=ic;
              c.onclick=function(){{flip(c);}};g.appendChild(c);
            }});
          }}
          function flip(c){{
            if(!canFlip||c.classList.contains("flipped")||c.classList.contains("matched"))return;
            c.classList.add("flipped");c.textContent=c.dataset.icon;flipped.push(c);
            if(flipped.length===2){{
              canFlip=false;var a=flipped[0],b=flipped[1];
              if(a.dataset.icon===b.dataset.icon){{
                a.classList.add("matched");b.classList.add("matched");matched+=2;flipped=[];canFlip=true;
                if(matched===cards.length)document.getElementById("status").textContent="You Won! 🎉";
              }} else {{
                setTimeout(function(){{
                  a.classList.remove("flipped");b.classList.remove("flipped");
                  a.textContent="";b.textContent="";flipped=[];canFlip=true;
                }},1000);
              }}
            }}
          }}
          init();
        <\\/script></body></html>'></iframe>`,

        ttt: `<iframe class="game-frame" height="540" scrolling="no" srcdoc='<!DOCTYPE html><html><head><style>
          html,body{{margin:0;padding:0;height:100%;overflow:hidden;background:#f0f2f5;font-family:"Segoe UI",sans-serif;}}
          body{{display:flex;justify-content:center;align-items:center;}}
          .card{{background:white;padding:1.5rem;border-radius:20px;box-shadow:0 10px 25px rgba(0,0,0,0.1);text-align:center;width:300px;}}
          h2{{color:#1a73e8;margin:0 0 1rem;font-size:1.3rem;}}
          .board{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1rem;}}
          .cell{{width:84px;height:84px;background:#f8f9fa;border:2px solid #dee2e6;border-radius:12px;display:flex;justify-content:center;align-items:center;font-size:2.2rem;font-weight:bold;cursor:pointer;transition:all 0.2s;user-select:none;}}
          .cell:hover{{background:#e9ecef;border-color:#1a73e8;}}
          .cell.x{{color:#1a73e8;}}.cell.o{{color:#d93025;}}
          .cell.winner{{background:#e8f0fe;border-color:#1a73e8;}}
          .status{{font-size:1rem;font-weight:600;margin-bottom:.8rem;color:#5f6368;}}
          .restart{{background:#1a73e8;color:white;border:none;padding:.6rem 1.2rem;border-radius:8px;font-size:.9rem;font-weight:600;cursor:pointer;}}
          .pinfo{{display:flex;justify-content:space-around;margin-bottom:.8rem;}}
          .player{{padding:.4rem .8rem;border-radius:6px;font-size:.85rem;}}
          .player.active{{background:#e8f0fe;color:#1a73e8;font-weight:bold;border:1px solid #1a73e8;}}
        </style></head><body><div class="card"><h2>Tic-Tac-Toe</h2>
          <div class="pinfo"><div id="pX" class="player active">You (X)</div><div id="pO" class="player">Computer (O)</div></div>
          <div id="status" class="status">Your Turn</div>
          <div class="board">
            <div class="cell" onclick="cellClick(0)"></div><div class="cell" onclick="cellClick(1)"></div><div class="cell" onclick="cellClick(2)"></div>
            <div class="cell" onclick="cellClick(3)"></div><div class="cell" onclick="cellClick(4)"></div><div class="cell" onclick="cellClick(5)"></div>
            <div class="cell" onclick="cellClick(6)"></div><div class="cell" onclick="cellClick(7)"></div><div class="cell" onclick="cellClick(8)"></div>
          </div>
          <button class="restart" onclick="restart()">New Game</button></div>
        <script>
          var board=["","","","","","","","",""],active=true,H="X",AI="O";
          var wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
          function cells(){{return document.querySelectorAll(".cell");}}
          function cellClick(i){{
            if(board[i]||!active)return;
            move(i,H);
            if(!checkWin(H)&&!checkTie()){{
              document.getElementById("status").textContent="Computer...";
              document.getElementById("pX").classList.remove("active");
              document.getElementById("pO").classList.add("active");
              active=false;
              setTimeout(function(){{
                var m=best();move(m,AI);
                if(!checkWin(AI)&&!checkTie()){{
                  document.getElementById("status").textContent="Your Turn";
                  active=true;
                  document.getElementById("pO").classList.remove("active");
                  document.getElementById("pX").classList.add("active");
                }}
              }},500);
            }}
          }}
          function move(i,p){{board[i]=p;var cl=cells();cl[i].textContent=p;cl[i].classList.add(p.toLowerCase());}}
          function best(){{
            var m=findW(AI);if(m>-1)return m;
            m=findW(H);if(m>-1)return m;
            if(!board[4])return 4;
            var co=[0,2,6,8].filter(function(x){{return!board[x];}});
            if(co.length)return co[Math.floor(Math.random()*co.length)];
            var av=[];for(var i=0;i<9;i++)if(!board[i])av.push(i);
            return av[Math.floor(Math.random()*av.length)];
          }}
          function findW(p){{
            for(var i=0;i<wins.length;i++){{
              var w=wins[i],a=w[0],b=w[1],c=w[2];
              if(board[a]===p&&board[b]===p&&!board[c])return c;
              if(board[a]===p&&board[c]===p&&!board[b])return b;
              if(board[b]===p&&board[c]===p&&!board[a])return a;
            }}return -1;
          }}
          function checkWin(p){{
            for(var i=0;i<wins.length;i++){{
              var w=wins[i];
              if(board[w[0]]===p&&board[w[1]]===p&&board[w[2]]===p){{
                document.getElementById("status").textContent=p===H?"You Win!":"Computer Wins!";
                var cl=cells();cl[w[0]].classList.add("winner");cl[w[1]].classList.add("winner");cl[w[2]].classList.add("winner");
                active=false;return true;
              }}
            }}return false;
          }}
          function checkTie(){{
            for(var i=0;i<9;i++)if(!board[i])return false;
            document.getElementById("status").textContent="It is a Tie!";active=false;return true;
          }}
          function restart(){{
            board=["","","","","","","","",""];active=true;
            document.getElementById("status").textContent="Your Turn";
            document.getElementById("pX").classList.add("active");
            document.getElementById("pO").classList.remove("active");
            var cl=cells();for(var i=0;i<9;i++){{cl[i].textContent="";cl[i].classList.remove("x","o","winner");}}
          }}
        <\\/script></body></html>'></iframe>`,
      }};

      gc.innerHTML = games[name] || '';
    }}

    // ── Expander toggle ───────────────────────────────────────────────────────────
    function toggleExp() {{
      const c = document.getElementById('exp-content');
      const a = document.getElementById('exp-arrow');
      c.classList.toggle('open');
      a.textContent = c.classList.contains('open') ? '▲' : '▼';
    }}

    // ── Retake ────────────────────────────────────────────────────────────────────
    function retake() {{
      // Clear answers
      Object.keys(ans).forEach(k => delete ans[k]);

      // Hide results + divider
      document.getElementById('results-divider').style.display  = 'none';
      document.getElementById('results-section').style.display  = 'none';

      // Re-enable predict button
      const btn = document.getElementById('sub-btn');
      btn.disabled = true;
      btn.classList.remove('rdy');
      btn.textContent = '⏳ Complete all questions';

      // Clear option selections
      document.querySelectorAll('.opt.sel').forEach(el => el.classList.remove('sel'));
      document.querySelectorAll('.q-card.done').forEach(el => el.classList.remove('done'));

      // Scroll to top of page to start quiz again
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
      sync();
    }}

    // ── Init ──────────────────────────────────────────────────────────────────────
    build();
    </script>
    </body>
    </html>"""

    # Add dynamic height script with initial height
    APP_HTML_WITH_AUTO_HEIGHT = APP_HTML + """
    <script>
    (function() {
        function sendHeight() {
            const height = Math.max(
                document.body.scrollHeight,
                document.body.offsetHeight,
                document.documentElement.clientHeight,
                document.documentElement.scrollHeight,
                document.documentElement.offsetHeight
            );
            window.parent.postMessage({
                type: "streamlit:setFrameHeight",
                height: height + 50
            }, "*");
        }
        
        // Send height immediately and on load
        if (document.readyState === 'loading') {
            window.addEventListener('DOMContentLoaded', function() {
                setTimeout(sendHeight, 50);
                setTimeout(sendHeight, 200);
            });
        } else {
            setTimeout(sendHeight, 50);
            setTimeout(sendHeight, 200);
        }
        
        window.addEventListener('load', sendHeight);
        
        // Watch for content changes
        const observer = new MutationObserver(function() {
            sendHeight();
        });
        observer.observe(document.body, { childList: true, subtree: true, attributes: true });
        
        // Override showResults to trigger height update
        const originalShowResults = window.showResults;
        window.showResults = function() {
            if (originalShowResults) originalShowResults();
            setTimeout(sendHeight, 100);
            setTimeout(sendHeight, 300);
            setTimeout(sendHeight, 600);
        };
        
        // Also trigger on any click that might change content
        document.addEventListener('click', function() {
            setTimeout(sendHeight, 100);
        });
    })();
    </script>
    """

    # Use a reasonable starting height (shows most content, then expands)
    components.html(APP_HTML_WITH_AUTO_HEIGHT, height=2800, scrolling=True)
