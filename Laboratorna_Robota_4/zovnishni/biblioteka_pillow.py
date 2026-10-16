from PIL import Image, ImageDraw


def run_pillow_demo():
    # Генерація матричного зображення через Pillow
    img = Image.new('RGB', (150, 50), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 20), "Lab Complete", fill=(255, 255, 0))

    path = "output/pillow_canvas.png"
    img.save(path)
    return f"[pillow] Створено нове растрове зображення: {path}"
