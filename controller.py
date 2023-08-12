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
                my_notes.new_ids()
                my_notes.save_note()
                view.print_message(text.save_note())
            case 3:
                word = view.input_search(text.input_search)
                result = my_notes.search_note(word)
                view.print_notes(result, text.not_found)
            case 4:
                word = view.input_search(text.input_search_edit)
                result = my_notes.search_note(word)
                view.print_notes(result, text.not_found)
                if result:
                    if len(result) != 1:
                        current_id = view.input_search(text.input_search_id)
                        result = my_notes.search_note_id(current_id)
                        view.print_notes(result, text.id_not_found)
                    else:
                        current_id = result[0].get('id')
                    for id in result:
                        if id.get('id') == current_id:
                            new_note = view.input_note(text.change_note)
                            note = my_notes.edit_note(new_note, current_id)
                            view.print_message(text.edit_note_succes(note))
                else:
                    view.print_message(text.not_found)
            case 5:
                word = view.input_search(text.input_search_delete)
                result = my_notes.search_note(word)
                view.print_notes(result, text.not_found)
                if result:
                    if len(result)!= 1:
                        current_id = view.input_search(text.input_search_id)
                        result = my_notes.search_note_id(current_id)
                        view.print_notes(result, text.id_not_found)
                    else:
                        current_id = result[0].get('id')
                    for id in result:
                        if id.get('id') == current_id:
                            note = my_notes.delete_note(current_id)
                            view.print_message(text.delete_note_succes(note))
                else:
                    view.print_message(text.not_found)
                my_notes.new_ids()
            case 6:
                notes = my_notes.show_notes()
                view.print_notes(notes, text.empty_notebook)
            case 7:
                my_notes.new_ids()
                my_notes.save_to_file()
                view.print_message(text.save_notes())
            case 8:
                break
            
