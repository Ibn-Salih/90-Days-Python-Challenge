# - Topics:
# - Learn the basics of steganography and how hidden data is embedded within other files.
# - Project:
# - Write a Python script that hides text within an image 
# - using steganography techniques.


from PIL import Image
import numpy as np

def encode_text_in_image(image_path, secret_text, output_path):
    """
    Hides text in an image using LSB steganography
    :param image_path: Path to the original image
    :param secret_text: Text to hide
    :param output_path: Where to save the encoded image
    """
    # Open the image and convert to numpy array
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Convert text to binary
    binary_text = ''.join([format(ord(char), '08b') for char in secret_text])
    binary_text += '1111111111111110'  # EOF marker (16 bits)
    
    # Validate text fits in image
    max_bits = img_array.size * 3  # 3 color channels per pixel
    if len(binary_text) > max_bits:
        raise ValueError("Text too large for this image")
    
    # Embed text in LSBs
    text_index = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB channels
                if text_index < len(binary_text):
                    # Clear LSB and set to text bit
                    img_array[i,j,k] = (img_array[i,j,k] & 0xFE) | int(binary_text[text_index])
                    text_index += 1
    
    # Save the encoded image
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print(f"Message hidden in {output_path}")

def decode_text_from_image(image_path):
    """
    Extracts hidden text from an image
    :param image_path: Path to the encoded image
    :return: Extracted secret text
    """
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Extract LSBs
    binary_text = []
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB channels
                binary_text.append(str(img_array[i,j,k] & 1))
    
    # Convert binary to text
    binary_text = ''.join(binary_text)
    # Split into 8-bit chunks
    bytes_ = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    # Find EOF marker and decode
    secret_text = []
    for byte in bytes_:
        if byte == '11111111':  # Check for EOF marker
            break
        secret_text.append(chr(int(byte, 2)))
    
    return ''.join(secret_text)

def main():
    print("Image Steganography Tool")
    mode = input("Encode (e) or Decode (d)? ").lower()
    
    if mode == 'e':
        image_path = input("Path to original image: ")
        text = input("Secret message: ")
        output_path = input("Output image path: ")
        encode_text_in_image(image_path, text, output_path)
    elif mode == 'd':
        image_path = input("Path to encoded image: ")
        text = decode_text_from_image(image_path)
        print(f"Extracted message: {text}")
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()