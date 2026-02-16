from pathlib import Path
import os
import json
from quick_notes import print_header, eraser


# Wczytuje konfiguracje z pliku JSON lub tworzy domyślną konfigurację, jeśli plik nie istnieje
def load_config():
    # Nazwy stałe plików
    CONFIG_FILE = './data/config.json'

    loading = 'Wczytywanie-konfiguracji-z-pliku...'
    

    if not os.path.exists(CONFIG_FILE):
        return create_default_config()
    else:
        print(print_header(loading))
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as cf:
                config = json.load(cf)
                return config.get('current_file')
            
        except(json.JSONDecodeError, IOError):
            print('Błąd podczas wczytywania konfiguracji.')
            return create_default_config()
    

def create_default_config():
    print('Nie znaleziono pliku konfiguracyjnego.\nChcesz utworzyć nowy folder czy skorzystać z już istniejącego?')
    choice = input('1. Utwórz nowy folder\n2. Skorzystaj z istniejącego folderu\nQ. Wyjdź z programu.\nPodaj nr opcji: ')
    name_q = 'Zakończono-program-Do-zobaczenia'

    match choice:
        case '1':
            pass
        case '2':
            pass
        case 'q' | 'Q':
            print_header(name_q)
            exit()

def new_note_file():
    pass
    