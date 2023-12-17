# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()  
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end = '\n\n') 
        else:
            print('Список контактов пустой')    
    
def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info 

def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:    
        file.writelines(all_cont)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    print("Выберите критерий для поиска:" +
        '1 - Имя' +
        '2 - Фамилия' +
        '3 - Телефон'
         )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)


def delete_cont(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        del_cont = file.readlines()
    print("Выберите критерий для поиска:" +
        '1 - Имя' +
        '2 - Фамилия' +
        '3 - Телефон'
         )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in del_cont:
        cont_as_list = cont.strip().split()
        if data in cont_as_list[comm - 1]:
            print(*cont_as_list)
            del_cont.remove(data)

def transfer_favorit(file_name, file_name1):
    print('Выбирите действие:' +
        '1 - Скопировать файл в папку Избранное' +
        '3 - Добавить новый контакт в папку Избранное'
        )
    ans = int(input())
    if ans == 1:
        with open(file_name, 'r', encoding='utf8') as file:
            search_file = str(find_contact(file_name))
        with open(file_name1, 'r', encoding='utf8') as file:
            all_copy_cont = file.readlines()
        all_copy_cont.append('\n' + search_file)
        with open(file_name1, 'w', encoding='utf8') as file:    
            file.writelines(all_copy_cont)
    elif ans == 2:
        new_cont_favr = add_contact(file_name1)
    else:
        print('Неверная команда')

