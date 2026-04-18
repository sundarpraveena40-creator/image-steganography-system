from PIL import Image

# Convert message to binary
def message_to_binary(message):
    return ''.join([format(ord(i), '08b') for i in message])

# Encode message into image
def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_msg = message_to_binary(message) + '1111111111111110'  # end marker

    pixels = img.load()
    width, height = img.size
    data_index = 0

    for i in range(width):
        for j in range(height):
            if data_index < len(binary_msg):
                r, g, b = pixels[i, j]

                r = (r & ~1) | int(binary_msg[data_index])
                data_index += 1

                if data_index < len(binary_msg):
                    g = (g & ~1) | int(binary_msg[data_index])
                    data_index += 1

                if data_index < len(binary_msg):
                    b = (b & ~1) | int(binary_msg[data_index])
                    data_index += 1

                pixels[i, j] = (r, g, b)

    img.save(output_path)
    print("Message encoded successfully!")