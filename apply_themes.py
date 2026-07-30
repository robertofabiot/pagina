import re
import os
import glob

# 1. Update main.css
with open('assets/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace deep black with dark green for Option A
css = css.replace('#111111', '#162915')
# Replace rgba black (header) with rgba dark green
css = css.replace('rgba(17, 17, 17,', 'rgba(22, 41, 21,')

# Append light-theme styles
light_theme_css = """
/* ==========================================================================
   LIGHT THEME OVERRIDES
   ========================================================================== */
body.light-theme #header {
    background: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid rgba(0,0,0,0.05);
}
body.light-theme #header > .logo {
    color: #386737 !important;
}
body.light-theme #header > nav > ul.links > li > a,
body.light-theme #header > nav > a {
    color: #555555 !important;
}
body.light-theme #header > nav > ul.links > li > a:hover,
body.light-theme #header > nav > a:hover {
    color: #386737 !important;
}
body.light-theme #header > nav > a[href="#menu"]:before {
    color: #386737 !important;
}

body.light-theme #footer {
    background-color: #f7f7f7 !important;
    color: #555555 !important;
}
body.light-theme #footer h3, 
body.light-theme #footer h4 {
    color: #386737 !important;
}
body.light-theme #footer p {
    color: #666666 !important;
}
body.light-theme #footer a {
    color: #386737 !important;
}
body.light-theme .copyright {
    background-color: #eeeeee !important;
    color: #777777 !important;
    border-top: 1px solid rgba(0,0,0,0.1);
}

body.light-theme #banner:after, 
body.light-theme #heading:before {
    background: linear-gradient(135deg, rgba(56, 103, 55, 0.9) 0%, rgba(255, 255, 255, 0.4) 100%) !important;
}
body.light-theme #banner:before {
    background: #ffffff !important;
    opacity: 0.3 !important;
}

body.light-theme #menu {
    background-color: #ffffff !important;
}
body.light-theme #menu .links > li > a {
    color: #555555 !important;
    border-bottom-color: rgba(0,0,0,0.1) !important;
}
body.light-theme #menu .links > li > a:hover {
    color: #386737 !important;
}
body.light-theme #menu .close:before {
    color: #555555 !important;
}

/* Theme Toggle Button */
#theme-toggle {
    position: fixed;
    bottom: 120px;
    right: 30px;
    width: 60px;
    height: 60px;
    background-color: #ffffff;
    color: #386737;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    z-index: 10000;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 2px solid #386737;
}
#theme-toggle:hover {
    transform: scale(1.1);
    background-color: #f0f0f0;
}
@media screen and (max-width: 736px) {
    #theme-toggle { width: 50px; height: 50px; font-size: 20px; bottom: 90px; right: 20px; }
}
@media screen and (max-width: 480px) {
    #theme-toggle { bottom: 75px; right: 15px; }
}
"""

if "LIGHT THEME OVERRIDES" not in css:
    css += light_theme_css

with open('assets/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Inject toggle button and JS into all HTML files
js_injection = """
    <!-- Theme Toggle -->
    <div id="theme-toggle" title="Cambiar Tema">
        <i class="icon fa-adjust"></i>
    </div>
    <script>
        const toggleBtn = document.getElementById('theme-toggle');
        const body = document.body;
        
        // Cargar preferencia
        if(localStorage.getItem('theme') === 'light') {
            body.classList.add('light-theme');
        }
        
        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('light-theme');
            if(body.classList.contains('light-theme')) {
                localStorage.setItem('theme', 'light');
            } else {
                localStorage.setItem('theme', 'dark');
            }
        });
    </script>
"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if 'id="theme-toggle"' not in html:
        # Insert before closing body tag
        html = html.replace('</body>', js_injection + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Themes applied successfully.")
