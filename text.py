hello_message = '''Добро пожаловать в Заметки'''

main_menu = '''Главное меню:
1. Создать заметку
2. Сохранить заметку
3. Просмотреть заметку
4. Редактировать заметку
5. Удалить заметку
6. Просмотреть все заметки
7. Выход'''

input_choice = '''Введите номер команды меню: '''

empty_notebook = '''Списко заметок пуст'''

input_new_note = 'Новая заметка:'

input_search = 'Введите идентификатор или заголовок или дату: '

input_search_edit = '''Какую заметку вы хотите изменить?
Введите идентификатор или заголовок: '''

input_search_id = 'Введите ID заметки для редактирования: '

not_found = 'Заметка не найдена'

id_not_found = 'Такого ID не существует'

new_note = {'title': 'Введите заголовок: ', 'text': 'Введите текст заметки: '}

change_note = 'Введите новые данные или оставьте поле пустым, чтобы не изменять.'

def new_note_succes_create(title: str) -> str:
    return f'Заметка {title} создана'

def delete_note_succes(title: str) -> str:
    return f'Заметка {title} удалена'

def edit_note_succes(title: str) -> str:
    return f'Заметка {title} отредактирована'

def load_note(title: str) -> str:
    return f'Заметка {title}:'

def save_note() -> str:
    return f'Заметка сохранена'

