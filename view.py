import text

# Метод работы с главным меню
def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit():
            if 0 < int(choice) < 9:
                return int(choice)
            else: 
                print_message(text.wrong_choice)
                choice = input(text.input_choice)
                return int(choice)
        else: 
            print_message(text.wrong_char)

# Метод печати сообщения        
def print_message(message):
   print('\n' + '-'*len(message))
   print(message)
   print('-'*len(message) + '\n')

# Метод ввода заметки через консоль
def input_note(message) -> dict[str,str,str]:
    new = {}
    print_message(message)
    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return new

# Метод печати заметки в консоль
def print_notes(notes: list[dict[str,str,str]], error: str):
    if notes:
        print('\n' + '-'*80)
        for note in notes:
            print(f'{note.get("id"):>3}. {note.get("title"):<10} ; {note.get("date"):^10} ; {note.get("text")}')
        print('-'*80 + '\n')
    else:
      print_message(error)

# Метод ввода данных для поиска
def input_search(message) -> str:
    return input(message)
