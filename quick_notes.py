from datetime import datetime
import json
import os


import load_config



# Czyszczenie zawartości okna konsoli
def eraser():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def print_header(option_name, width=56):
    # Przygotownaie napisu
    name_up = option_name.upper()
    center_line = name_up.center(width, '-')
    # Przygotowanie lini
    line = '-' * width
    # Drukowanie zawartości
    print(line)
    print(center_line)
    print(line)

#1 Utwórz nowy plik
def create_new_file(nazwa_pliku):
    option_name = 'utwórz-nowy-plik'
    print_header(option_name)

    new_file = input('Podaj nazwę pliku: ')

#2 Zmiana ścieżki pliku
def change_path():
    print

#3 Dodaj wpis z aktualną datą
def add_entry1(nazwa_pliku):
    option_name = 'dodaj-wpis-z-aktualna-datą'
    print_header(option_name)

    # Pobieranie i formatowanie daty
    today = datetime.now()
    today_same = today.strftime("%d.%m.%Y")
    print(today_same)
    # Pobiera wpis od użytkowniku
    new_entry = input('Wpisz treść swojego wpisu: \n--> ')
    
    try:
        with open(nazwa_pliku, 'a', encoding='utf-8') as plik:
            plik.write(today_same+' '+new_entry+'\n')
            eraser()
            print(f'\nTwój wpis: {new_entry} został dodany pomyślnie!\n')

    except FileNotFoundError:
        print('Plik nie został znaleziony!')

#4 Dodaj wpis z własną datą
def add_entry2(nazwa_pliku):
    eraser()
    option_name = 'dodaj-wpis-z-własną-datą'
    print_header(option_name)

    # Pobieranie daty od użytkownika
    today_u = input('Wpisz własną datę w formacie: DD.MM.RRRR \n-->')
    # Walidacja formatu daty
    try:
        datetime.strptime(today_u, "%d.%m.%Y")
    except ValueError:
        eraser()
        print('Nieprawidłowy format daty! Wprowadź datę ponownie!')
        return add_entry2(nazwa_pliku)
    
    # Pobieranie wpisu od użytkownika
    new_entry = input('Wpisz treść swojego wpisu: \n--> ')

    try:
        with open(nazwa_pliku, 'a', encoding='utf-8') as plik:
            plik.write(today_u+' '+new_entry+'\n')
            eraser()
            print(f'\nTwój wpis: {new_entry} z datą {today_u} zpstał dodany pomyślnie!\n')
    except FileNotFoundError:
        print('Plik nie został znaleziony!')

#5 Wyświetla wpisy z pliku
def open_txt(file_name):
    option_name = 'wyświetl-swoje-wpisy'

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            odczytany = file.read()
            eraser()
            print_header(option_name)
            print(f'\nTwoje wpisy: \n\n{odczytany}')
    except FileNotFoundError:
        print('Plik nie został znaleziony!')

#6 Wyczyśc zawartość pliku
def clear_txt(file_name):
    option_name = '!!!-wyczyść-zawartość-pliku-!!!'
    print_header(option_name)

    print('\nCzy na pewno chcesz wyczyścić Plik???')
    choise = input('Pamiętaj, że zmiany są nieodwracalne! T/N\n-->')

    if choise.lower() == 'n':
        pass
    elif choise == 't':
        print('Plik został wyczyszczony pomyślnie!')
        eraser()
        with open(file_name, 'w', encoding='utf-8') as file:
            pass
    else:
        print('Wybież prawidłową opcje!')
        return clear_txt(file_name)

#Funkcja odpowiadająca za MENU 
def main_menu():
    
    # Ładowanie konfiguracji
    nazwa = load_config.load_config()
    print(load_config.load_config())
    
    name_q = 'Zakończono-program-Do-zobaczenia'
    
    # Główna pętla
    while True:
         
        # Wyświetla menu
        print('-'*56)
        print('Witaj w programie do szybkich notatek!'.center(56))
        print('-'*56)
        print('Co chcesz zrobić?')
        print('1. Utwórz nowy plik. (W trakcjie dodawania)')
        print('2. Podaj ścieżkę do istniejącego pliku. (W trakcjie dodawania)')
        print('3. Dodaj nowy wpis z dzisiejszą datą.')
        print('4. Dodaj nowy wpis z własną datą.')
        print('5. Wyświetl swoje wpisy.')
        print('6. !!! Wyczyść zawartość pliku !!!')
        print('Q. Wyjdź z programu.')
        print('-'*56)

        choice = input('Co chcesz zrobić? Podaj nr opcji: ')
        match choice:
            case '1':
                create_new_file(nazwa)
            case '2':
                print("Opcja 2")
            case '3':
                add_entry1(nazwa)
            case '4':
                add_entry2(nazwa)
            case '5':
                open_txt(nazwa)
            case '6':
                clear_txt(nazwa)
            case 'q' | 'Q':
                eraser()
                print_header(name_q)
                break
            case _:
                print('\nNieprawidłowa opcja Menu! Wprowadź poprawną opcje!\n')

if __name__ == "__main__":
    main_menu()