# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её,
# читать список заметок, редактировать заметку, удалять заметку.

import os
import json
import datetime


file_notes = 'notes.json'


# Функция чтения записей из файла JSON


def read_notes(file):
    with open(file, 'r', encoding='utf-8') as data:
        try:
            notes = json.load(data)
        except json.decoder.JSONDecodeError as e:
            return None
    return notes


# Функция создания записи


def add_note(notes):
    if not notes:
        id = 1
        notes = []
    else:
        id = len(notes) + 1
    title = input('Введите имя записи: ')
    text = input('Введите текст заметки: ')
    time_marker = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    note = {'ID': id, 'TITLE': title, 'TEXT': text, 'TIME': time_marker}
    notes.append(note)
    save_note = input(
        'Сохранить запись? 1 - да, 0 - нет\n')
    while True:
        if not save_note.isdigit:
            print('Введите 0 или 1')
        else:
            if save_note == "1":
                save_notes(notes)
                print('Сохранено')
                break
            else:
                break
    input('\n"Enter - возврат в меню >> ')
    menu()

# Функция показа записей


def show_notes(notes):
    if not notes:
        print('Записей пока нет')
        input('\n"Enter - возврат в меню >> ')
        menu()
    else:
        for note in notes:
            print(f'ID: {note["ID"]}')
            print(f'TITLE: {note["TITLE"]}')
            print(f'TEXT: {note["TEXT"]}')
            print(f'TIME: {note["TIME"]}')
            print('_________________')

        input('\n"Enter - возврат в меню >> ')
        menu()

# Функция записи в файл JSON


def save_notes(note):
    with open(file_notes, 'w', encoding='utf-8') as data:
        json.dump(note, data, ensure_ascii=False, indent=4)


# Функция поиска записи
def search_note(notes):
    os.system("cls")
    menu = ('Найти запись по:\n'
            '1 - ID\n'
            '2 - Имя записи\n'
            '3 - Ключевые слова\n'
            '4 - Дате добавления/изменения\n'
            '0 - Выход')
    print(menu)
    fail_answer = 5
    while fail_answer > 0:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 1 до 4')
            fail_answer -= 1
            continue
        else:
            if answer == '1':
                os.system("cls")
                search_id = input('Введите ID записи: ')
                if not search_id.isdigit:
                    print('ID должен быть числом')
                    continue
                else:
                    for note in notes:
                        if note[0] == search_id:
                            print(note)
                            return note[0]
                print(menu)
            if answer == '2':
                os.system("cls")
                result = []
                search_title = input('Введите имя записи: ')
                for note in notes:
                    if note[1] == search_title:
                        result.append(note)
                        print(note)
                        return result
                    else:
                        print('Записи с таким именем нетю')
            if answer == '3':
                os.system("cls")
                delete_note(notes)
                print(menu)
            if answer == '4':
                os.system("cls")
                search_note(notes)
                print(menu)
            if answer == '5':
                os.system("cls")
                edit_note()
                print(menu)
            if answer == '0':
                exit(0)

    print('Похоже, вы делаете что-то не так((')
    exit(0)
        


# Функция удаления записи

def delete_note(notes):
    note = input()

# Функция меню


def menu():
    os.system("cls")
    menu = ('Добро пожаловать в программу "Блокнот"\n\n'
            'Доступные действия:\n'
            '1 - Показать все заметки\n'
            '2 - Добавить заметку\n'
            '3 - Удалить заметку\n'
            '4 - Найти заметку\n'
            '5 - Редактировать заметку\n'
            '0 - Выход')
    print(menu)
    notes = read_notes(file_notes)
    fail_answer = 5
    while fail_answer > 0:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 1 до 7')
            fail_answer -= 1
            continue
        else:
            if answer == '1':
                os.system("cls")
                show_notes(notes)
                print(menu)
            if answer == '2':
                os.system("cls")
                add_note(notes)
                print(menu)
            if answer == '3':
                os.system("cls")
                delete_note(notes)
                print(menu)
            if answer == '4':
                os.system("cls")
                search_note(notes)
                print(menu)
            if answer == '5':
                os.system("cls")
                edit_note()
                print(menu)
            if answer == '0':
                exit(0)

    print('Похоже, вы делаете что-то не так((')
    exit(0)


if __name__ == '__main__':
    menu()
