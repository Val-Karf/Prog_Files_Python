# ПРОГРАММА КУРСОВОЙ РАБОТЫ ПО ПРОЕКТИРОВАНИЮ БАЗЫ ДАННЫХ
"""
Задание курсового проекта:
Вариант 2. Спроектировать базу данных, построить программу, обеспечи вающую взаимодействие с ней в режиме диалога. В БД должны храниться сведе ния о зарегистрированных происшествиях.
База данных должна содержать данные для регистрации сообщений о про исшествиях (регистрационный номер сообщения, дата регистрации, краткая фа була (тип происшествия); информацию о принятом по происшествию решении 
(отказано в возбуждении дел, удовлетворено ходатайство о возбуждении уголов ного дела с указанием регистрационный номера заведенного дела, отправлено по 
территориальному признаку); информацию о лицах, виновных или подозревае мых в совершении происшествия (регистрационный номер лица, фамилия, имя, 
отчество, адрес, количество судимостей), отношение конкретных лиц к конкрет ным происшествиям (виновник, потерпевший, подозреваемый, свидетель). По мимо SQL запросов для создания таблиц базы данных, разработать пакет, состо ящий из процедур и функций, позволяющий:
 рассчитать данные о количестве происшествий в указанный промежуток 
времени;
 для указанного лица получить количество происшествий, в которых он за регистрирован;
 предоставить возможность добавления и изменения информации о проис шествиях, при этом предусмотреть курсоры, срабатывающие на некото рые пользовательские исключительные ситуации;
 предоставить возможность добавления и изменения информации о лицах, 
участвующих в происшествиях, при этом предусмотреть курсоры, сраба тывающие на некоторые пользовательские исключительные ситуации.
Необходимо предусмотреть возможность выдачи протокола происшествия.
"""

import sqlite3
from datetime import datetime

# Функция для создания базы данных и необходимых таблиц
def create_database():
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()

    # Таблица происшествий
    cursor.execute('''CREATE TABLE IF NOT EXISTS incidents (
                        id INTEGER PRIMARY KEY,
                        registration_number TEXT UNIQUE,
                        registration_date DATE,
                        incident_type TEXT,
                        decision TEXT
                    )''')

    # Таблица лиц
    cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
                        id INTEGER PRIMARY KEY,
                        person_registration_number TEXT UNIQUE,
                        first_name TEXT,
                        last_name TEXT,
                        middle_name TEXT,
                        address TEXT,
                        convictions INTEGER
                    )''')

    # Таблица соотношений
    cursor.execute('''CREATE TABLE IF NOT EXISTS incident_person (
                        id INTEGER PRIMARY KEY,
                        incident_id INTEGER,
                        person_id INTEGER,
                        role TEXT,
                        FOREIGN KEY(incident_id) REFERENCES incidents(id),
                        FOREIGN KEY(person_id) REFERENCES persons(id)
                    )''')

    conn.commit()
    conn.close()

# Создаем базу данных
create_database()


















# Функции для взаимодействия с базой данных
def add_incident(registration_number, registration_date, incident_type, decision):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO incidents (registration_number, registration_date, incident_type, decision)
                          VALUES (?, ?, ?, ?)''', (registration_number, registration_date, incident_type, decision))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Ошибка: Данный регистрационный номер происшествия уже существует.")
    finally:
        conn.close()

def update_incident(registration_number, decision):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE incidents SET decision = ? WHERE registration_number = ?''', (decision, registration_number))
    conn.commit()
    conn.close()

def add_person(person_registration_number, first_name, last_name, middle_name, address, convictions):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO persons (person_registration_number, first_name, last_name, middle_name, address, convictions)
                          VALUES (?, ?, ?, ?, ?, ?)''', (person_registration_number, first_name, last_name, middle_name, address, convictions))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Ошибка: Данный регистрационный номер лица уже существует.")
    finally:
        conn.close()

def link_person_to_incident(incident_reg_number, person_reg_number, role):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT id FROM incidents WHERE registration_number = ?''', (incident_reg_number,))
    incident_id = cursor.fetchone()
    cursor.execute('''SELECT id FROM persons WHERE person_registration_number = ?''', (person_reg_number,))
    person_id = cursor.fetchone()
    
    if incident_id and person_id:
        cursor.execute('''INSERT INTO incident_person (incident_id, person_id, role) VALUES (?, ?, ?)''',
                       (incident_id[0], person_id[0], role))
        conn.commit()
    else:
        print("Ошибка: Не удалось найти происшествие или лицо с указанным номером.")
    
    conn.close()

def get_incidents_count(start_date, end_date):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM incidents WHERE registration_date BETWEEN ? AND ?''',
                   (start_date, end_date))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_person_incidents_count(person_registration_number):
    conn = sqlite3.connect('incidents.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM incident_person
                      JOIN persons ON incident_person.person_id = persons.id
                      WHERE persons.person_registration_number = ?''',
                   (person_registration_number,))
    count = cursor.fetchone()[0]
    conn.close()
    return count
















def main():
    while True:
        print("\nМеню:")
        print("1. Добавить происшествие")
        print("2. Изменить решение по происшествию")
        print("3. Добавить лицо")
        print("4. Связать лицо с происшествием")
        print("5. Получить количество происшествий за период")
        print("6. Получить количество происшествий для лица")
        print("7. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            reg_number = input("Введите регистрационный номер происшествия: ")
            reg_date = input("Введите дату регистрации (YYYY-MM-DD): ")
            incident_type = input("Введите тип происшествия: ")
            decision = input("Введите решение по происшествию: ")
            add_incident(reg_number, reg_date, incident_type, decision)
        
        elif choice == '2':
            reg_number = input("Введите регистрационный номер происшествия: ")
            decision = input("Введите новое решение по происшествию: ")
            update_incident(reg_number, decision)

        elif choice == '3':
            person_reg_number = input("Введите регистрационный номер лица: ")
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            middle_name = input("Введите отчество: ")
            address = input("Введите адрес: ")
            convictions = int(input("Введите количество судимостей: "))
            add_person(person_reg_number, first_name, last_name, middle_name, address, convictions)

        elif choice == '4':
            incident_reg_number = input("Введите регистрационный номер происшествия: ")
            person_reg_number = input("Введите регистрационный номер лица: ")
            role = input("Введите роль (виновник, потерпевший, подозреваемый, свидетель): ")
            link_person_to_incident(incident_reg_number, person_reg_number, role)

        elif choice == '5':
            start_date = input("Введите начальную дату (YYYY-MM-DD): ")
            end_date = input("Введите конечную дату (YYYY-MM-DD): ")
            count = get_incidents_count(start_date, end_date)
            print(f"Количество происшествий за указанный период: {count}")
        
        elif choice == '6':
            person_reg_number = input("Введите регистрационный номер лица: ")
            count = get_person_incidents_count(person_reg_number)
            print(f"Количество происшествий для указанного лица: {count}")

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()



