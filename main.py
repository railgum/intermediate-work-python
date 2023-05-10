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
            '3 - Дате добавления/изменения\n'
            '0 - Выход')
    print(menu)
    fail_answer = 5
    while fail_answer > 0:
        answer = input('Введите номер действия:>> ')
        if not answer.isdigit():
            print('Нужно ввести число от 0 до 3')
            fail_answer -= 1
            continue
        else:
            if answer == '1':
                os.system("cls")
                try:
                    search_id = int(input('Введите ID записи: '))
                    if  search_id > len(notes):
                        print('Записи с таким ID нет')
                    else:
                        for note in notes:
                            if note['ID'] == search_id:
                                print(note)
                                break
                except ValueError:
                    print('ID должен быть числом')
                    break
                input('\n"Enter - возврат в меню >> ')
                os.system("cls")
                print(menu)
            if answer == '2':
                os.system("cls")
                # result = []
                count = 0
                search_title = input('Введите имя записи: ')
                for note in notes:
                    if note['TITLE'] == search_title:
                        # result.append(note)
                        print(note)
                        count += 1
                if count == 0:
                    print('Записи с таким именем нет')

                input('\n"Enter - возврат в меню >> ')
                os.system("cls")
                print(menu)
            if answer == '3':
                os.system("cls")
                try:
                    count = 0
                    search_date = input('Введите дату записи в формате 01-03-2023: ')
                    date_obj = datetime.datetime.strptime(search_date, '%d-%m-%Y').date()
                    for note in notes:
                        temp_date = datetime.datetime.strptime(note['TIME'], '%d-%m-%Y %H:%M')
                        if temp_date.date() == date_obj:
                            print(note)
                            count += 1
                    if count == 0:
                        print('В этот день записей не было')
                        break
                except ValueError:
                    print('Неверный формат даты')
                input('\n"Enter - возврат в меню >> ')
                os.system("cls")
                print(menu)
            if answer == '0':
                return
        

# Функция удаления записи

def delete_note(notes):
    del_note = input('Введите ID записи, которую хотите удалить: ')
    for note in notes:
        if note['ID'] == int(del_note):
            notes.remove(note)
            break
    print('Удалено')

    save_note = input(
        'Сохранить изменения? 1 - да, 0 - нет\n')
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

# Функция редактирования записей

def edit_note(notes):
    ed_note = input('Введите ID записи, которую хотите изменить: ')
    for note in notes:
        if note['ID'] == int(ed_note):
            new_title = input('Введите новое имя: ')
            new_text = input('Введите текст записи: ')
            note['TITLE'] = new_title
            note['TEXT'] = new_text
            note['TIME'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
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
                if not notes:
                    print('К сожалению записей ещё нет ')
                    break
                else:
                    search_note(notes)
                os.system("cls")
                print(menu)
            if answer == '5':
                os.system("cls")
                edit_note(notes)
                print(menu)
            if answer == '0':
                exit(0)

    print('Похоже, вы делаете что-то не так((')
    exit(0)


if __name__ == '__main__':
    menu()
