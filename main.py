from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QListWidget, 
    QHBoxLayout, QVBoxLayout, QFileDialog)

import os
from PIL import Image 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ImageProcessor():
    def __init__ (self):
        self.image = None 
        self.full_path = None
    def loadimage(self, dir, name):
        self.full_path = os.path.join(dir, name)
        self.image = Image.open(self, self.full_path)

    def showImage(self):
        lbl_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lbl_image.width(), lbl_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbl_image.setPixmap(pixmapimage)
        lbl_image.show()





app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Редактор изображений')
main_win.resize(700, 500)

# создание виджетов
btn_select_dir = QPushButton('Выбрать папку')
list_widget_images = QListWidget()
lbl_image = QLabel('Картинка')
btn_left = QPushButton('Влево')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_bw = QPushButton('Ч/б')

# расположение виджжетов
layout_edit_buttons = QHBoxLayout()
layout_edit_buttons.addWidget(btn_left)
layout_edit_buttons.addWidget(btn_right)
layout_edit_buttons.addWidget(btn_mirror)
layout_edit_buttons.addWidget(btn_sharpness)
layout_edit_buttons.addWidget(btn_bw)

layout_image = QVBoxLayout()
layout_image.addWidget(lbl_image, 95)
layout_image.addLayout(layout_edit_buttons, 5)

layout_files = QVBoxLayout()
layout_files.addWidget(btn_select_dir)
layout_files.addWidget(list_widget_images)

layout_main = QHBoxLayout()
layout_main.addLayout(layout_files, 20)
layout_main.addLayout(layout_image, 80)

main_win.setLayout(layout_main)
current_dir = " "
current_image = ImageProcessor()

def showFileNames ():
    print("открываем")
    global current_dir
    current_dir = QFileDialog.getExistingDirectory()
    
    all_files = os.listdir(current_dir)
    image_files = images_select(all_files)

    list_widget_images.clear()
    list_widget_images.addItems(image_files)

def images_select(all_files):
    result = []
    extentions = (".png", ".jpg", ".jpeg", '.gif')

    for file_name in all_files:
        for ext in extentions:
            if file_name.endswith(ext):
                result.append(file_name)


        


    return result 


def showChoosenImage():
    name_image = list_widget_images.currentItem().text()
    current_image.loadimage(current_dir, name_image)
    current_image.showImage()


btn_select_dir.clicked.connect(showFileNames)
list_widget_images.currentRowChanged.connect(showChoosenImage)


main_win.show()
app.exec_()
