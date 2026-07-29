import os
import re

page_images = {
    "index.html": "images/servicios/pesado/pesado1.png",
    "perfil.html": "images/servicios/pesado/pesado2.png",
    "servicios.html": "images/servicios/hazmat/peligrosas1.jpeg",
    "contacto.html": "images/servicios/ligero/ligero1.png",
    "empleo.html": "images/servicios/pesado/pesado3.png",
    "servicio-hazmat.html": "images/servicios/hazmat/peligrosas2.png",
    "servicio-consumo.html": "images/servicios/consumo/variosyconsumo1.png",
    "servicio-pesado.html": "images/servicios/pesado/pesado1.png",
    "servicio-ligero.html": "images/servicios/ligero/ligero2.png"
}

for filename, img_path in page_images.items():
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    img_tag = f'<img src="{img_path}" alt="Banner" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: -1; filter: brightness(0.6);">'
    
    # Use re.DOTALL just in case, but usually it's one line
    content = re.sub(r'<video autoplay loop muted playsinline src=".*?"></video>', img_tag, content)
    content = re.sub(r'<img src="[^"]+" alt="Banner" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; z-index: -1; filter: brightness\(0\.6\);">', img_tag, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualizacion completada.")
