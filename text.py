hello_message = '''Добро пожаловать в Заметки'''

main_menu = '''Главное меню:
1. Создать заметку
2. Сохранить заметку
3. Просмотреть заметку
4. Редактировать заметку
5. Удалить заметку
6. Просмотреть все заметки
7. Выход'''

edit_menu = '''Меню редактирования:
1. Редактировать заголовок
2. Редактировать заметку
3. Выход'''

input_choice = '''Введите номер команды меню: '''

empty_notebook = '''Списко заметок пуст'''

input_new_note = 'Новая заметка:'

input_title = 'Введите заголовок: '

not_found = 'Заметка не найдена'

new_note = {'title': 'Введите заголовок: ', 'date': 'Введите дату: ', 'text': 'Введите текст заметки: '}

def new_note_succes_create(title: str) -> str:
    return f'Заметка {title} создана'

def delete_note_succes(title: str) -> str:
    return f'Заметка {title} удалена'

def edit_note_succes(title: str) -> str:
    return f'Заметка {title} отредактирована'

def load_note(title: str) -> str:
    return f'Заметка {title}:'

def save_note(title: str) -> str:
    return f'Заметка {title} сохранена'

