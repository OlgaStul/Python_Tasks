# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может
#  ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# def show_menu() -> int: print("\nВыберите необходимое действие:\n"
# "1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")
# choice = int(input())
# return choice

def read_csv(filename='phonebook.csv'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file:
            data.append(line.strip('\n').split(','))
    return data


def display_all_records():
    data = read_csv() 
    for row in data:
        print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_last_name():
    last_name = input('Введите фамилию: ')
    data = read_csv()  
    for row in data:
        if row[0] == last_name:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def find_phone_number():
    phone = input('Введите номер телефона: ')
    data = read_csv()  
    for row in data:
        if row[2] == phone:
            print(f'Фамилия: {row[0]}\nИмя: {row[1]}\nНомер телефона: {row[2]}\nКомментарий: {row[3]}\n')


def add_data(filename='phonebook.csv'):
    with open(filename, 'a', encoding='utf-8') as file:  
        info = input('Введите новые данные абонента (фамилия, имя, номер, комментарий - через запятую): ').split(', ')
        file.write(','.join(info) + '\n')
        print('Данные записаны.')
    

def delete_data(filename='phonebook.csv'):
    with open(filename, 'r', encoding='utf-8') as file:
        last_name = input('Введите данные абонента, которого вы хотите удалить: ')
        data = read_csv()
        with open(filename, 'w', encoding='utf-8') as file:
            for row in data:
                if last_name not in row:
                    file.write(','.join(row) + '\n')
            if last_name not in row:
                print("Такого абонента нет, либо данные введены не корректно")
            else:
                print("Данные удалены")
                    

number = 0

print('Введите число для операции со справочником:')
print('1 - вывести весь справочник;\n2 - найти абонента по фамилии;\n'
        '3 - найти абонента по номеру телефона;\n4 - ввести новые данные абонента;\n5 - удалить данные абонента;\n'
        '6 - завершить работу.')

number = input()

if number == '1':
    display_all_records()

elif number == '2':
    find_last_name()

elif number == '3':
    find_phone_number()

elif number == '4':
    add_data()

elif number == '5':
    delete_data()

else:
    print('Работа завершена.')




