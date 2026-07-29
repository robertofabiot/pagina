import os
import glob

seo_data = {
    "index.html": {
        "title": "Transporte Divino Niño | Especialistas en Transporte de Carga en Nicaragua",
        "desc": "Soluciones eficientes en logística y transporte de carga terrestre en Nicaragua. Especialistas en sustancias peligrosas, transporte pesado y ligero."
    },
    "perfil.html": {
        "title": "Nuestro Perfil | Transporte Divino Niño",
        "desc": "Conoce nuestra historia, misión y valores. Más de 29 años de experiencia brindando confianza y seguridad en logística."
    },
    "servicios.html": {
        "title": "Nuestros Servicios | Transporte Divino Niño",
        "desc": "Ofrecemos transporte de sustancias peligrosas (Hazmat), carga pesada, distribución ligera y productos de consumo en todo el país."
    },
    "contacto.html": {
        "title": "Contacto | Transporte Divino Niño",
        "desc": "Comunícate con nuestro equipo para solicitar una cotización o asesoría en transporte de carga terrestre en Nicaragua."
    },
    "empleo.html": {
        "title": "Únete al Equipo | Transporte Divino Niño",
        "desc": "Sé parte de nuestra familia. Buscamos conductores, auxiliares de ruta y personal administrativo comprometido con la excelencia."
    },
    "servicio-hazmat.html": {
        "title": "Transporte Hazmat | Transporte Divino Niño",
        "desc": "Servicio especializado en manejo seguro de sustancias peligrosas (Hazmat) cumpliendo con estrictas normativas de seguridad."
    },
    "servicio-consumo.html": {
        "title": "Productos de Consumo | Transporte Divino Niño",
        "desc": "Soluciones de logística y transporte para productos de consumo masivo, garantizando entregas oportunas y seguras."
    },
    "servicio-pesado.html": {
        "title": "Transporte Pesado | Transporte Divino Niño",
        "desc": "Flota de transporte pesado con alta capacidad para maquinaria y carga sobredimensionada a nivel nacional."
    },
    "servicio-ligero.html": {
        "title": "Distribución Ligera | Transporte Divino Niño",
        "desc": "Servicio de distribución ligera para entregas rápidas y ágiles en áreas urbanas y rutas específicas."
    }
}

common_keywords = "transporte de carga, logistica nicaragua, transporte pesado, transporte hazmat, transporte divino niño"

for filename in glob.glob("*.html"):
    if filename not in seo_data: continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    data = seo_data[filename]
    
    # Remove old og tags and keywords if they exist poorly
    import re
    content = re.sub(r'<meta property="og:.*?>', '', content)
    content = re.sub(r'<meta name="keywords".*?>', '', content)
    
    og_and_keywords = f'''
    <meta name="keywords" content="{common_keywords}">
    <meta property="og:title" content="{data["title"]}">
    <meta property="og:description" content="{data["desc"]}">
    <meta property="og:image" content="https://transdn.com/images/logos/logo-removebg-preview.png">
    <meta property="og:url" content="https://transdn.com/{filename}">
    <meta property="og:type" content="website">'''
    
    # Insert right before </head>
    content = content.replace('</head>', og_and_keywords + '\n</head>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
