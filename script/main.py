from PIL import Image

ASCII_CHARS = "@%#*+=-:. "


#i should resize image to preserve aspect ratio
#basic of converting is that
#i should first convert image into grayscale
#but to do that i should maintain the aspect ratio of the image
#then i will map the grayscale values to a set of ascii characters#

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def conver_grayscale(image):
    return image.convert('L')


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]
    return ascii_str


def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)

    image = resize_image(image, new_width)

    image = conver_grayscale(image)

    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ''
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + '\n'

    return ascii_img


if __name__ == "__main__":
    print('-------------Welcome to Image to ASCII Convertor-------------')
    path = input('------Enter Path of Image: ')
    ascii_art = image_to_ascii(path)
    print(ascii_art)

    with open('../art/ascii_art.txt', 'w') as file:
        file.write(ascii_art)
