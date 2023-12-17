from Task_49 import print_contacts, add_contact, find_contact, transfer_favorit, delete_cont

CONTACTS = 'Spravochnik\\Contacts.txt'
CONTACTS1 = 'Spravochnik\\Favorite.txt'

def interface():
    while True:
        print('Выберете действие:\n' +
        '1 - Добавить контакт\n' +
        '2 - Вывести все контакты\n' +
        '3 - Найти контакт\n' +
        '4 - Добавить в изранное\n' +
        '5 - Удалить контакт\n' +
        '0 - Выйти')
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                transfer_favorit(CONTACTS, CONTACTS1)
            case 5:
                delete_cont(CONTACTS)
            case _:
                print("Не верная команда!")      
            
if __name__ == '__main__':
    interface()