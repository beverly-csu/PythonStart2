from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QApplication, QWidget,
    QPushButton, QLabel, QListWidget, QFileDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import os

# Создание виджетов
app = QApplication([])
window = QWidget()
btn_open_dir = QPushButton('Открыть папку')
btn_rotate_left = QPushButton('Лево')
btn_rotate_right = QPushButton('Право')
btn_mirror = QPushButton('Отзеркалить')
btn_contrast = QPushButton('Резкость')
btn_black_white = QPushButton('Ч/Б')
image = QLabel('Тут должны быть картинка, но она потерялась')
image_list = QListWidget()

h_main = QHBoxLayout()
v_left = QVBoxLayout()
v_right = QVBoxLayout()
h_add = QHBoxLayout()
# Создание виджетов

# Размещение на layout'ах
h_add.addWidget(btn_rotate_left)
h_add.addWidget(btn_rotate_right)
h_add.addWidget(btn_mirror)
h_add.addWidget(btn_contrast)
h_add.addWidget(btn_black_white)

v_left.addWidget(btn_open_dir)
v_left.addWidget(image_list)

v_right.addWidget(image)
v_right.addLayout(h_add)

h_main.addLayout(v_left, stretch=2)
h_main.addLayout(v_right, stretch=6)
# Размещение на layout'ах

# Функции обработчики
class ImageProccesor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modifed'

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        path = os.path.join(dir, filename)
        self.image = Image.open(path)

    def showImage(self, path):
        image.hide()
        pixmap = QPixmap(path)
        w, h = image.width(), image.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmap)
        image.show()

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        path = os.path.join(path, self.filename)
        self.image.save(path)

    def do_flip(self):
        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.saveImage()
        path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(path)

    def do_left(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.saveImage()
        path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(path)

    def do_right(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.saveImage()
        path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(path)

    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(path)
    
imgProc = ImageProccesor()

def showCurrentImage():
    if image_list.currentRow() > 0:
        filename = image_list.currentItem().text()
        imgProc.loadImage(workDir, filename)
        path = os.path.join(workDir, filename)
        imgProc.showImage(path)

workDir = ''

def chooseDir():
    current_dir = QFileDialog.getExistingDirectory(window)
    return (len(current_dir) != 0, current_dir)

def showFiles():
    result = chooseDir()
    if result[0]:
        global workDir
        workDir = result[1]
        files = os.listdir(workDir)
        images = filter(files, ['.png', '.jpg', '.bpm', '.jpeg'])
        image_list.clear()
        image_list.addItems(images)

def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
                break
    return result
# Функции обработчики

# Привязка кнопок
btn_open_dir.clicked.connect(showFiles)
btn_black_white.clicked.connect(imgProc.do_bw)
btn_mirror.clicked.connect(imgProc.do_flip)
btn_rotate_left.clicked.connect(imgProc.do_left)
btn_rotate_left.clicked.connect(imgProc.do_right)
btn_contrast.clicked.connect(imgProc.do_sharpen)
image_list.currentRowChanged.connect(showCurrentImage)
# Привязка кнопок

# Результат
window.resize(900, 600)
window.setWindowTitle('EasyEditor')
window.setLayout(h_main)
window.show()
app.exec()
# Результат
