# Python Program to find the Colors in an Image
from PIL import Image
from collections import Counter
# Open the image
image = Image.open('input.jpg')

if __name__ == '__main__':
    # Convert the image to a list of RGB tuples
    pixels = list(image.getdata())
    # Use Counter to count the occurrences of each color
    color_counts = Counter(pixels)
    # Get the 6 most common colors
    top_colors = color_counts.most_common(6)
    # Print the extracted colors and their counts
    for i, (color, count) in enumerate(top_colors):
        color_block = "\033[48;2;{};{};{}m    \033[0m".format(color[0], color[1], color[2])
        print(f"Color {i + 1}: {color_block} RGB: {color} - Count: {count}")