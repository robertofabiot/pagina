import os
import re

seo_data = {
    "index.html": {
        "title": "Transporte Divino Niño | Especialistas en Transporte de Carga en Nicaragua",
        "desc": "Soluciones eficientes en logística y transporte de carga terrestre en Nicaragua. Especialistas en sustancias peligrosas, transporte pesado y ligero.",
        "video": True
    },
    "perfil.html": {
        "title": "Nuestro Perfil | Transporte Divino Niño",
        "desc": "Conoce nuestra historia, misión y valores. Más de 29 años de experiencia brindando confianza y seguridad en logística.",
        "video": False
    },
    "servicios.html": {
        "title": "Nuestros Servicios | Transporte Divino Niño",
        "desc": "Ofrecemos transporte de sustancias peligrosas (Hazmat), carga pesada, distribución ligera y productos de consumo en todo el país.",
        "video": True
    },
    "contacto.html": {
        "title": "Contacto | Transporte Divino Niño",
        "desc": "Comunícate con nuestro equipo para solicitar una cotización o asesoría en transporte de carga terrestre en Nicaragua.",
        "video": False
    },
    "empleo.html": {
        "title": "Únete al Equipo | Transporte Divino Niño",
        "desc": "Sé parte de nuestra familia. Buscamos conductores, auxiliares de ruta y personal administrativo comprometido con la excelencia.",
        "video": False
    },
    "servicio-hazmat.html": {
        "title": "Transporte Hazmat | Transporte Divino Niño",
        "desc": "Servicio especializado en manejo seguro de sustancias peligrosas (Hazmat) cumpliendo con estrictas normativas de seguridad.",
        "video": True
    },
    "servicio-consumo.html": {
        "title": "Productos de Consumo | Transporte Divino Niño",
        "desc": "Soluciones de logística y transporte para productos de consumo masivo, garantizando entregas oportunas y seguras.",
        "video": True
    },
    "servicio-pesado.html": {
        "title": "Transporte Pesado | Transporte Divino Niño",
        "desc": "Flota de transporte pesado con alta capacidad para maquinaria y carga sobredimensionada a nivel nacional.",
        "video": True
    },
    "servicio-ligero.html": {
        "title": "Distribución Ligera | Transporte Divino Niño",
        "desc": "Servicio de distribución ligera para entregas rápidas y ágiles en áreas urbanas y rutas específicas.",
        "video": True
    }
}

common_keywords = "transporte de carga, logistica nicaragua, transporte pesado, transporte hazmat, transporte divino niño"

for filename, data in seo_data.items():
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title, Desc, Keywords
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["desc"]}">', content)
    content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{common_keywords}">', content)
    
    # Add OG tags if not present
    if 'property="og:title"' not in content:
        og_tags = f'''
    <meta property="og:title" content="{data["title"]}">
    <meta property="og:description" content="{data["desc"]}">
    <meta property="og:image" content="https://transdn.com/images/logos/logo-removebg-preview.png">
    <meta property="og:url" content="https://transdn.com/{filename}">
    <meta property="og:type" content="website">'''
        # Insert after keywords
        content = re.sub(r'(<meta name="keywords".*?>)', r'\1' + og_tags, content)

    # 2. Swap video for image if needed
    if not data["video"]:
        # Find video tag in banner
        video_pattern = r'<video autoplay loop muted playsinline src="images/banners/banner2\.mp4"></video>'
        replacement = r'<img src="images/banners/banner.jpg" alt="Banner" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: -1; filter: brightness(0.6);">'
        content = re.sub(video_pattern, replacement, content)
        
    # 3. Specific fix for contacto.html Map iframe
    if filename == 'contacto.html':
        if 'title="Mapa' not in content:
            content = content.replace('<iframe \n            src="https://www.google.com/maps', '<iframe \n            title="Mapa de Ubicación de Transporte Divino Niño"\n            src="https://www.google.com/maps')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualizacion completada.")
