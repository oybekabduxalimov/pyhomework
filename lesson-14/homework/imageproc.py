import numpy as np
import os
from PIL import Image

def load_image(image_path):
    """
    Loads an image and converts it to a NumPy array.
    :param image_path: Path to the image file
    :return: Image as a NumPy array or None if file not found
    """
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return None
    return np.array(Image.open(image_path))

def flip_image(img_array):
    """
    Flips an image horizontally and vertically.
    :param img_array: Image as NumPy array
    :return: Flipped image
    """
    return np.flipud(np.fliplr(img_array))

def add_noise(img_array):
    """
    Adds random noise to an image.
    :param img_array: Image as NumPy array
    :return: Noisy image
    """
    noise = np.random.randint(-50, 50, img_array.shape, dtype=np.int16)
    return np.clip(img_array + noise, 0, 255).astype(np.uint8)

def brighten_image(img_array, value=40):
    """
    Brightens an image by adding a constant value to pixel intensities.
    :param img_array: Image as NumPy array
    :param value: Brightness increment value (default 40)
    :return: Brightened image
    """
    return np.clip(img_array + value, 0, 255).astype(np.uint8)

def apply_mask(img_array):
    """
    Applies a black mask at the center of an image.
    :param img_array: Image as NumPy array
    :return: Image with a black mask applied
    """
    h, w, _ = img_array.shape
    x, y = w // 2 - 50, h // 2 - 50
    img_array[y:y+100, x:x+100] = 0
    return img_array

def main():
    image_path = "images/birds.jpg"
    img_array = load_image(image_path)
    if img_array is not None:
        Image.fromarray(flip_image(img_array)).save("flipped.jpg")
        Image.fromarray(add_noise(img_array)).save("noisy.jpg")
        Image.fromarray(brighten_image(img_array)).save("brightened.jpg")
        Image.fromarray(apply_mask(img_array)).save("masked.jpg")

if __name__ == "__main__":
    main()
