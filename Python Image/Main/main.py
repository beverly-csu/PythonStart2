from PIL import Image, ImageFilter


def print_property(img):
    print('Размер:', img.size)
    print('Формат:', img.format)
    print('Тип:', img.mode)


with Image.open('original.jpg') as original:
    print_property(original)
    original.show()
    
    gray = original.convert('L')
    print_property(gray)
    gray.show()
    gray.save('gray.jpg')

    blur = original.filter(ImageFilter.BLUR)
    blur.save('blur.jpg')
    blur.show()

    up = original.transpose(Image.Transpose.ROTATE_180)
    up.save('up.jpg')
    up.show()