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
            im = Image.open(path)
        except IOError:
            return "the path is not an image file"
        pix = im.load()
        width, hight = im.size
        code = ""
        for i in range(width):
            for j in range(hight):
                if pix[i, j] == 1:
                    code += chr(j)
    else:
        code = "the path not exists"
    return code


assert decryption("resources//hamlet.txt") == "the path is not an image file", "Not the expected result"
assert decryption("blabla.com") == "the path not exists", "Not the expected result"
print("decryption of the cipher: " + decryption(MY_PATH))
