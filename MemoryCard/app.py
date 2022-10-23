from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QButtonGroup
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton

def show_result():
    grpbox_answers.hide()
    grpbox_result.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)
    grpbox_answers.show()
    grpbox_result.hide()
    btn_ok.setText('Ответить')

def start_test():
    if btn_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()

app = QApplication([])
window = QWidget()

lbl_question = QLabel('Вопрос?')
btn_ok = QPushButton('Ответить')
btn_ok.clicked.connect(start_test)

grpbox_answers = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
btn_group = QButtonGroup()
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)

grpbox_result = QGroupBox('Результат ответа')
lbl_result = QLabel('Правильный ответ: 1234')
v_line_result = QVBoxLayout()

v_line_result.addWidget(lbl_result, alignment=Qt.AlignCenter)
grpbox_result.setLayout(v_line_result)
grpbox_result.hide()

h_line_ans = QHBoxLayout()
v_line_ans_1 = QVBoxLayout()
v_line_ans_2 = QVBoxLayout()

v_line_ans_1.addWidget(rbtn_1)
v_line_ans_1.addWidget(rbtn_2)
v_line_ans_2.addWidget(rbtn_3)
v_line_ans_2.addWidget(rbtn_4)
h_line_ans.addLayout(v_line_ans_1)
h_line_ans.addLayout(v_line_ans_2)

grpbox_answers.setLayout(h_line_ans)

v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(lbl_question, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(grpbox_answers)
h_line_main_2.addWidget(grpbox_result)
h_line_main_3.addWidget(btn_ok)

v_line_main.addLayout(h_line_main_1)
v_line_main.addLayout(h_line_main_2)
v_line_main.addLayout(h_line_main_3)

window.setLayout(v_line_main)

window.show()
app.exec()