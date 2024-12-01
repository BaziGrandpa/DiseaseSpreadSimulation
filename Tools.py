import tkinter as tk
from PIL import Image, ImageTk


def draw_quadrilateral_outline(canvas, points, line_color="black", line_width=2):
    """
    Draws an irregular quadrilateral outline using lines.

    :param canvas: The tkinter Canvas widget.
    :param points: A list of four tuples, each representing a point (x, y).
    :param line_color: The color of the outline.
    :param line_width: The width of the lines.
    """
    # Draw lines between consecutive points
    for i in range(len(points)):
        start = points[i]
        end = points[(i + 1) % len(points)]  # Connect the last point to the first
        canvas.create_line(
            start[0], start[1], end[0], end[1],
            fill=line_color, width=line_width
        )

def render_text(canvas, x, y, text, font=("Arial", 16), color="black"):
    """
    Renders text on the canvas at the specified position.
    
    :param canvas: The tkinter Canvas widget.
    :param x: The x-coordinate of the text position.
    :param y: The y-coordinate of the text position.
    :param text: The text to display.
    :param font: The font of the text (family, size).
    :param color: The color of the text.
    """
    canvas.create_text(x, y, text=text, font=font, fill=color)