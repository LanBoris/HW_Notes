import text
import view
import model

my_notes = model.Notes()

def start():
    my_notes.load_notes()
    view.print_message(text.hello_message)
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                note = view.input_note(text.input_new_note)
                title = my_notes.create_note(note)
                view.print_message(text.new_note_succes_create(title))
            case 2:
                my_notes.save_notes()
                view.print_message(text.save_note(title))
            case 3:
                word = view.input_search(text.input_title)
                result = my_notes.search_note(word)
                view.print_notes(result, text.not_found)
                break
            case 6:
                notes = my_notes.show_notes()
                view.print_notes(notes, text.empty_notebook)
            case 7:
                break
            
