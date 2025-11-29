import io
from PIL import Image, ImageChops, ImageEnhance

def convert_to_ela_image(image_path, quality=90):
    """
    Convert an image to its ELA (Error Level Analysis) representation.
    Returns a PIL Image (RGB).
    """
    original = Image.open(image_path).convert('RGB')

    # Save to JPEG in memory
    buffer = io.BytesIO()
    original.save(buffer, 'JPEG', quality=quality)
    buffer.seek(0)
    compressed = Image.open(buffer)

    # Difference between original and compressed
    ela_image = ImageChops.difference(original, compressed)

    # Scale differences to full 0-255
    extrema = ela_image.getextrema()  # list of (min, max) for each channel
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)

    return ela_image
