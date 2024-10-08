from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog,QLabel, QPushButton, QListWidget,QHBoxLayout, QVBoxLayout
import os
app = QApplication([])
win = QWidget()
win.resize(700,500)
btn_dir = QPushButton("Папка")
listFiles = QListWidget()
lbImage = QLabel("Картинка")
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_clip = QPushButton("Отзеркалить")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б")
main_line = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()
row_1 = QHBoxLayout()

col_1.addWidget(btn_dir)
col_1.addWidget(listFiles)
col_2.addWidget(lbImage)
row_1.addWidget(btn_left)
row_1.addWidget(btn_right)
row_1.addWidget(btn_clip)
row_1.addWidget(btn_sharp)
row_1.addWidget(btn_bw)
col_2.addLayout(row_1)
main_line.addLayout(col_1)
main_line.addLayout(col_2)
win.setLayout(main_line)

def filter(files,extensions):
    result = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result
def show_file_names_list():
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    filenames = filter(files,extensions)
    listFiles.clear()
    for file in filenames:
        listFiles.addItem(file)

btn_dir.clicked.connect(show_file_names_list)
win.show()
app.exec_()