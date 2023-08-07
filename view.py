import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit and 0 < int(choice) < 8:
            return int(choice)
        
def print_message(message):
   print('\n' + '-'*len(message))
   print(message)
   print('-'*len(message) + '\n')

def input_note(message) -> dict[str,str,str]:
    new = {}
    print_message(message)
    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return new

def print_notes(notes: list[dict[str,str,str]], error: str):
    if notes:
        print('\n' + '-'*80)
        for note in notes:
            print(f'{note.get("id"):>3}. {note.get("title"):<10} ; {note.get("date"):^10} ; {note.get("text")}')
        print('-'*80 + '\n')
    else:
      print_message(error)

def input_search(message) -> str:
    return input(message)