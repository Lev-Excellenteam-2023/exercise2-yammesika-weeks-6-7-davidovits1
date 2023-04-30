
from PIL import Image
import os.path

MY_PATH = "resources//code.png"


def decryption(path):
    """
    Gets a path of an image and decodes a code hidden in pixels
    :param path: path of image
    :return: code 
    """
    if os.path.exists(path):
        try:
            image = Image.open(path)
        except IOError:
            return "the path is not an image file"
        code = code_from_image(image)

    else:
        code = "the path not exists"
    return code


def code_from_image(image):
    """
    Decodes a code hidden in pixels of image
    :param image: image object
    :return: the code hidden in the image
    """
    pix = image.load()
    width, height = image.size
    return ''.join(chr(column) for row in range(width) for column in range(height) if pix[row, column] == 1)


def main():
    assert decryption("resources//hamlet.txt") == "the path is not an image file", "Not the expected result"
    assert decryption("blabla.com") == "the path not exists", "Not the expected result"
    print("decryption of the cipher: " + decryption(MY_PATH))


if __name__ == "__main__":
    # Call the main handler function
    main()
