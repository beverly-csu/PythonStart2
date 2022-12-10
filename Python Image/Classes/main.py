from PIL import Image, ImageFilter


class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Увы, но такой картинки нет :(')

    def do_left(self):
        turned_left = self.original.transpose(Image.Transpose.ROTATE_90)
        self.changed.append(turned_left)
        new_filename = self.filename.split('.')[0] + '_left.jpg'
        turned_left.save(new_filename)

    def do_cropped(self):
        box = (100, 100, 400, 450)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        new_filename = self.filename.split('.')[0] + '_cropped.jpg'
        cropped.save(new_filename)


MyImage = ImageEditor('cat.jpg')
MyImage.open()
MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()