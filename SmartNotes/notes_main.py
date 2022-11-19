from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QLineEdit, QTextEdit, QListWidget
)
import json

# Базовая структура файлов с заметками
notes = {
    "Приветствуем в приложении": {
        "текст": "Вы можете пользовать приложением как угодно!",
        "теги": ["начало", "приветствие"]
    }
}
# Базовая структура файлов с заметками

# Запись стартовой заметки
with open('notes.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file)
# Запись стартовой заметки

# Создание виджетов
app = QApplication([])
window = QWidget()
note_field = QTextEdit()
notes_list = QListWidget()
tags_list = QListWidget()
btn_create_note = QPushButton('Создать заметку')
btn_delete_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')
btn_add_tag = QPushButton('Добавить к заметке')
btn_remove_tag = QPushButton('Открепить от заметки')
btn_search_by_tag = QPushButton('Искать заметки по тегу')
lbl_for_notes = QLabel('Список заметок:')
lbl_for_tags = QLabel('Список тегов:')
search_tag_field = QLineEdit()
# Создание виджетов

# Создание лэйаутов
main_layout = QHBoxLayout()

left_side = QVBoxLayout()
right_side = QVBoxLayout()

h_1 = QHBoxLayout()
h_2 = QHBoxLayout()
h_3 = QHBoxLayout()
h_4 = QHBoxLayout()
h_5 = QHBoxLayout()
h_6 = QHBoxLayout()
h_7 = QHBoxLayout()
h_8 = QHBoxLayout()
h_9 = QHBoxLayout()
# Создание лэйаутов

# Распределение виджетов
h_1.addWidget(lbl_for_notes)
h_2.addWidget(notes_list)
h_3.addWidget(btn_create_note)
h_3.addWidget(btn_delete_note)
h_4.addWidget(btn_save_note)
h_5.addWidget(lbl_for_tags)
h_6.addWidget(tags_list)
h_7.addWidget(search_tag_field)
h_8.addWidget(btn_add_tag)
h_8.addWidget(btn_remove_tag)
h_9.addWidget(btn_search_by_tag)

right_side.addLayout(h_1)
right_side.addLayout(h_2)
right_side.addLayout(h_3)
right_side.addLayout(h_4)
right_side.addLayout(h_5)
right_side.addLayout(h_6)
right_side.addLayout(h_7)
right_side.addLayout(h_8)
right_side.addLayout(h_9)

left_side.addWidget(note_field)

main_layout.addLayout(left_side)
main_layout.addLayout(right_side)

window.setLayout(main_layout)
# Распределение виджетов

# Преднастройка приложения
window.resize(600, 400)
window.setWindowTitle('Умные заметки')
search_tag_field.setPlaceholderText('Введите тег...')
# Преднастройка приложения

# Запуск приложения
window.show()
app.exec()
# Запуск приложения