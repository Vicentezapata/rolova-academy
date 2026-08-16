import os
import glob
import re
from bs4 import BeautifulSoup

# Define paths
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GALLERY_DIR = os.path.join(SKILL_DIR, "style-gallery")
THEMES_DIR = os.path.join(SKILL_DIR, "assets", "themes")

# Make sure themes directory exists
os.makedirs(THEMES_DIR, exist_ok=True)

def find_css_variable(css_text, var_names):
    """Attempt to find a specific CSS variable value from a list of possible names"""
    for var in var_names:
        match = re.search(r'{}:\s*([^;]+);'.format(re.escape(var)), css_text)
        if match:
            return match.group(1).strip()
    return None

def process_theme(filepath):
    filename = os.path.basename(filepath)
    if not filename.endswith('.html') or filename == 'index.html':
        return
        
    theme_name = filename[:-5]
    print(f"Processing {theme_name}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract styles
    style_tag = soup.find('style')
    css_content = style_tag.string if style_tag and style_tag.string else ""
    
    # Try to map variables
    bg_val = find_css_variable(css_content, ['--bg-0', '--bg-primary', '--bg-main', '--background'])
    if not bg_val:
        # fallback to extracting a default or first gradient color
        match = re.search(r'(#[0-9a-fA-F]{3,6}|rgb\([^)]+\)|rgba\([^)]+\))', css_content)
        if match:
            bg_val = match.group(1).strip()
        else:
            bg_val = '#050b1f'
            
    surface_val = find_css_variable(css_content, ['--bg-1', '--bg-secondary', '--card-bg', '--surface', '--surface-color', '--card-bg-from']) or '#f0f0f0'
    text_val = find_css_variable(css_content, ['--text-primary', '--text-main', '--text-0', '--color-text']) or '#000000'
    accent_val = find_css_variable(css_content, ['--accent-1', '--neon-cyan', '--primary', '--accent', '--color-primary']) or '#3b6cff'
    
    # Build the override mapping
    mapping_css = f'''
/* --- AUTO-GENERATED MAPPING FOR BASE.CSS COMPATIBILITY --- */
:root {{
  --bg: {bg_val};
  --surface: {surface_val};
  --border: color-mix(in srgb, {text_val} 15%, transparent);
  --text-1: {text_val};
  --text-2: color-mix(in srgb, {text_val} 70%, transparent);
  --text-3: color-mix(in srgb, {text_val} 40%, transparent);
  --accent: {accent_val};
}}
.deck {{ background: transparent !important; }}
.card, .step, .item, .thumb {{ 
  background: var(--surface) !important; 
  border-color: var(--border) !important;
  color: var(--text-1) !important;
}}
.card-accent {{ border-top-color: var(--accent) !important; }}
h1, h2, h3, h4, .h1, .h2, .h3, .h4 {{ color: var(--text-1) !important; }}
p, li, .dim {{ color: var(--text-2) !important; }}
.kicker, .eyebrow {{ color: var(--accent) !important; }}
.pill {{ background: color-mix(in srgb, var(--surface) 50%, var(--accent) 10%) !important; border-color: var(--border) !important; color: var(--text-1) !important; }}
'''
    
    # Write the compiled CSS
    css_out_path = os.path.join(THEMES_DIR, f"{theme_name}.css")
    with open(css_out_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
        f.write("\n")
        f.write(mapping_css)
        
    # Extract background decorations
    # We remove typical foreground elements like .stage, .footer, .progress-ring, h1, etc.
    # What's left in body should be the decorations
    if soup.body:
        body_clone = BeautifulSoup(str(soup.body), 'html.parser').body
        # decompose all non-decoration content
        for cls in ['stage', 'footer', 'progress-ring', 'top', 'slide-header', 'slide-footer', 'deck']:
            for el in body_clone.find_all(class_=cls):
                el.decompose()
        # also decompose typical tags
        for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'svg', 'script', 'header', 'footer']:
            for el in body_clone.find_all(tag):
                el.decompose()
                
        from bs4 import Tag
        decorations_html = "".join([str(child) for child in body_clone.children if isinstance(child, Tag)])
    else:
        decorations_html = ""
        
    dec_out_path = os.path.join(THEMES_DIR, f"{theme_name}_decorations.html")
    with open(dec_out_path, 'w', encoding='utf-8') as f:
        f.write(decorations_html)
        
    print(f" -> Compiled {theme_name}.css and {theme_name}_decorations.html")

def main():
    print(f"Building themes from {GALLERY_DIR}...")
    html_files = glob.glob(os.path.join(GALLERY_DIR, "*.html"))
    for f in html_files:
        process_theme(f)
    print("Done!")

if __name__ == "__main__":
    main()
