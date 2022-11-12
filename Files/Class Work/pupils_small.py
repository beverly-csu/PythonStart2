#напиши здесь свою программу
class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupils = []

filename = 'pupils_txt.txt'
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        print(data[0], data[1], '-', int(data[2]))
        pupils.append(Pupil(data[0], data[1], int(data[2])))

sum_of_marks = 0
print('\n\nОтличники:')
for pupil in pupils:
    if pupil.mark == 5:
        print(pupil.surname)
    sum_of_marks += pupil.mark

print('\n\nСредняя оценка класса:', sum_of_marks / len(pupils))