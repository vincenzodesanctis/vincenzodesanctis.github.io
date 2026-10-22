import re
import os
from pathlib import Path
from titles import TITLE_MAPPING
from sorting import MANUAL_ORDER

STATIC_DIR = Path("static/media/albums/certifications")
CONTENT_DIR = Path("content/certifications")

# --- MAPPA DEI TITOLI ---
CATEGORY_TITLES = {
    "cybersecurity": "Cybersecurity",
    "cloud_infrastructure": "Cloud & Infrastructure",
    "systems_devops": "Systems, Networking & DevOps",
    "ai_data": "AI & Data Science",
    "software_development": "Software & Development",
    "management_leadership": "Management & Leadership",
    "academic_corporate": "Academic & Corporate Training",
    "other_certifications": "Other"
}

# --- ORDINE DELLE CATEGORIE (SLUG CORRETTI CON I TRATTINI) ---
CATEGORY_ORDER = [
    "cybersecurity",
    "cloud-infrastructure",
    "management-leadership",
    "ai-data",
    "systems-devops",
    "software-development",
    "academic-corporate",
    "other-certifications"
]
# ----------------------------------------------------------

print("🚀 Generazione pagine con ordine personalizzato...")

categories = {}
for file in STATIC_DIR.rglob("*_thumb.webp"):
    category_raw = file.parent.name
    slug = category_raw.lower().replace(" ", "-").replace("&", "and").replace("_", "-").replace("--", "-")
    
    title = CATEGORY_TITLES.get(category_raw, category_raw.replace("-", " ").replace("_", " ").title())
    
    large_file = file.parent / file.name.replace("_thumb.webp", "_large.webp")
    
    if large_file.exists():
        if slug not in categories:
            categories[slug] = {"title": title, "pairs": []}
            
        thumb_path = f"/media/albums/certifications/{category_raw}/{file.name}"
        large_path = f"/media/albums/certifications/{category_raw}/{large_file.name}"
        file_key = file.name.replace('_thumb.webp', '')
        
        existing_files = [p[2] for p in categories[slug]["pairs"]]
        if file.name not in existing_files:
            categories[slug]["pairs"].append((thumb_path, large_path, file.name, file_key))

def sort_by_manual_order(item):
    file_key = item[3]
    if file_key in MANUAL_ORDER:
        return (0, MANUAL_ORDER.index(file_key))
    else:
        return (1, file_key)

# Genera le pagine delle singole categorie
for slug, data in categories.items():
    data["pairs"].sort(key=sort_by_manual_order)
    count = len(data["pairs"])
    title_with_count = f"{data['title']} ({count})"

    html_grid = '<div class="full-bleed mt-8 mb-12 not-prose">\n'
    html_grid += '  <div class="cert-grid">\n'
    for thumb, large, filename, file_key in data["pairs"]:
        
        mapped_title = TITLE_MAPPING.get(file_key, "").strip()
        if mapped_title:
            clean_title = mapped_title
        else:
            clean_title = file_key.replace('_', ' ').replace('-', ' ').title()
            if len(clean_title) > 40:
                clean_title = clean_title[:37] + "..."
        
        html_grid += f'    <a href="{large}" onclick="event.preventDefault(); openMyLightbox(\'{large}\', \'{slug}\');" class="block transition-transform duration-200 hover:scale-[1.02]" data-gallery="{slug}">\n'
        html_grid += f'      <div class="cert-thumb-box">\n'
        html_grid += f'        <img src="{thumb}" class="cert-thumb-img" />\n'
        html_grid += f'      </div>\n'
        html_grid += f'      <span class="text-xs text-center mt-2 block text-gray-700 dark:text-gray-300 w-full px-1" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; word-break: break-word;">{clean_title}</span>\n'
        html_grid += f'    </a>\n'
    html_grid += '  </div>\n'
    html_grid += '</div>\n'
    
    # JavaScript del Lightbox
    html_grid += '''
<div id="my-custom-lightbox" onclick="if(event.target === this) closeMyLightbox();" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(0,0,0,0.95); z-index:9999999; justify-content:center; align-items:center; flex-direction:column; opacity: 0; transition: opacity 0.3s ease;">
    <span onclick="closeMyLightbox()" style="position:absolute; top:20px; right:30px; color:white; font-size:45px; font-weight:bold; cursor:pointer; user-select: none; z-index: 10000000;">&times;</span>
    <button onclick="changeMyImage(-1); event.stopPropagation();" style="position:absolute; left:20px; background:rgba(255,255,255,0.1); border:none; color:white; font-size:40px; cursor:pointer; outline:none; padding: 10px 20px; border-radius: 50%; z-index: 10000000;">&#10094;</button>
    <img id="my-lightbox-img" src="" onclick="event.stopPropagation();" style="max-width:90vw; max-height:85vh; object-fit:contain; border-radius: 8px; box-shadow: 0 0 30px rgba(0,0,0,0.8);">
    <button onclick="changeMyImage(1); event.stopPropagation();" style="position:absolute; right:20px; background:rgba(255,255,255,0.1); border:none; color:white; font-size:40px; cursor:pointer; outline:none; padding: 10px 20px; border-radius: 50%; z-index: 10000000;">&#10095;</button>
</div>
<script>
  let currentMyGallery = []; let currentMyIndex = 0;
  function openMyLightbox(url, gallerySlug) {
    const links = document.querySelectorAll('a[data-gallery="' + gallerySlug + '"]');
    currentMyGallery = Array.from(links).map(a => a.getAttribute('href'));
    currentMyIndex = currentMyGallery.indexOf(url);
    if (currentMyIndex === -1) currentMyIndex = 0;
    document.getElementById('my-lightbox-img').src = currentMyGallery[currentMyIndex];
    const modal = document.getElementById('my-custom-lightbox');
    modal.style.display = 'flex'; document.body.classList.add('lightbox-active');
    setTimeout(() => { modal.style.opacity = '1'; }, 10);
  }
  function closeMyLightbox() {
    const modal = document.getElementById('my-custom-lightbox');
    modal.style.opacity = '0';
    setTimeout(() => { modal.style.display = 'none'; document.body.classList.remove('lightbox-active'); }, 300);
  }
  function changeMyImage(step) {
    currentMyIndex += step;
    if (currentMyIndex >= currentMyGallery.length) currentMyIndex = 0;
    if (currentMyIndex < 0) currentMyIndex = currentMyGallery.length - 1;
    document.getElementById('my-lightbox-img').src = currentMyGallery[currentMyIndex];
  }
  document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('my-custom-lightbox');
    if (modal.style.display === 'flex') {
      if (e.key === 'ArrowRight') changeMyImage(1);
      if (e.key === 'ArrowLeft') changeMyImage(-1);
      if (e.key === 'Escape') closeMyLightbox();
    }
  });
</script>
'''
    
    indented_html = '\n'.join(['        ' + line for line in html_grid.splitlines()])
    
    md_content = f"""---
title: "{title_with_count}"
type: landing
sections:
  - block: markdown
    content:
      title: "{title_with_count}"
      text: |
{indented_html}
---
"""
    with open(CONTENT_DIR / f"{slug}.md", "w", encoding="utf-8") as f:
        f.write(md_content)

# Aggiorna l'indice con l'ordine personalizzato
total_certs = sum(len(data["pairs"]) for data in categories.values())
index_title = f"Certifications & Credentials ({total_certs})"

hub_content = f"""---
title: "{index_title}"
type: landing
sections:
  - block: markdown
    content:
      title: "{index_title}"
      subtitle: "Select a category to view my professional certifications and completed courses."
      text: |
"""

# 1. Aggiungiamo le categorie nell'ordine specificato
for s in CATEGORY_ORDER:
    if s in categories:
        data = categories[s]
        count = len(data["pairs"])
        cred_word = "credential" if count == 1 else "credentials"
        hub_content += f"        - **[{data['title']}](/certifications/{s}/)** ({count} {cred_word})\n"

# 2. Aggiungiamo eventuali categorie extra non previste (per sicurezza, in fondo)
for s, data in categories.items():
    if s not in CATEGORY_ORDER:
        count = len(data["pairs"])
        cred_word = "credential" if count == 1 else "credentials"
        hub_content += f"        - **[{data['title']}](/certifications/{s}/)** ({count} {cred_word})\n"

hub_content += """    design:
      columns: '1'
---
"""
with open(CONTENT_DIR / "_index.md", "w", encoding="utf-8") as f:
    f.write(hub_content)

print(f"✅ Fatto! {total_certs} credenziali totali, ordinate correttamente.")


# --- AGGIORNAMENTO AUTOMATICO DELLA HOME PAGE ---
home_file = Path("content/_index.md")
if home_file.exists():
    content = home_file.read_text(encoding="utf-8")
    # Trova qualsiasi numero seguito da " verified credentials" e lo sostituisce
    content = re.sub(r'\d+(?= verified credentials)', str(total_certs), content)
    # Trova qualsiasi numero dopo "Explore All " e lo sostituisce
    content = re.sub(r'(?<=Explore All )\d+(?= Credentials)', str(total_certs), content)
    home_file.write_text(content, encoding="utf-8")
    print(f"✅ Home Page aggiornata con {total_certs} credenziali.")
