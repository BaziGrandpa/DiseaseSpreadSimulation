import tkinter as tk
from PIL import Image, ImageTk

def init(canvas):
    # Load the image using Pillow
    img_width = 1200
    img_height = 800
    image_path = "Campus.png"  # Replace with your image path
    image = Image.open(image_path)
    image = image.resize((img_width, img_height))  # Resize as needed
    background_image = ImageTk.PhotoImage(image)
    return background_image