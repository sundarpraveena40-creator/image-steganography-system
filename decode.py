from PIL import Image

# Decode message from image
def decode_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_data = ""
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    # Convert binary to message
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if byte == '11111110':  # stop condition
            break
        message += chr(int(byte, 2))

    return message