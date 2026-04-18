from encode import encode_image
from decode import decode_image

def main():
    print("----- Image Steganography -----")
    print("1. Encode Message")
    print("2. Decode Message")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        image_path = input("Enter input image path: ")
        message = input("Enter secret message: ")
        output_path = input("Enter output image path: ")

        encode_image(image_path, message, output_path)

    elif choice == '2':
        image_path = input("Enter image path to decode: ")
        message = decode_image(image_path)
        print("Hidden Message:", message)

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()