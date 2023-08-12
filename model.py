import datetime
class Notes:
    # Метод инициализации
    def __init__(self, path: str='notes.csv'):
        self._notes: list[dict[str, str, str]] = []
        self._path = path
        self._last_id = 0

    # Метод создания заметки
    def create_note(self, new: dict[str, str, str]) -> str:
        new_id = int(self._last_id) + 1
        new['id'] = str(new_id)
        new_date = datetime.datetime.today().strftime("%d/%m/%Y - %H:%M")
        new['date'] = str(new_date)
        self._notes.append(new)
        self._last_id += 1
        return new.get('title')
    
    # Метод сохранения заметки
    def save_note(self) -> str:
        data = []
        for note in self._notes:
            data.append(';'.join([note['id'], note['date'], note['title'], note['text']]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(data)
        return 

    # Метод сохранения изменений в файл
    def save_to_file(self):
        data = []
        for note in self._notes:
            data.append(';'.join([note['id'], note['date'], note['title'], note['text']]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(data)

    # Метод загрузки данных из файла
    def load_notes(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for note in data:
            note = note.strip().split(';')
            new = {'id': note[0], 'date': note[1], 'title': note[2], 'text': note[3]}
            self._notes.append(new)
        for field in self._notes:
            self._last_id = max(self._last_id, int(field.get('id')))
        
    # Метод печати заметок в консоль
    def show_notes(self):
        return self._notes
    
    # Метод поиска заметки по названию, дате или ID
    def search_note(self, word: str) -> dict[str,str,str]:
        result: list[dict[str,str,str]] = []
        for note in self._notes:
            if word.lower() in note['title'].lower() or word in note['id'] or word in note['date']:
                result.append(note)
        return result
    
    # Метод поиска заметки по ID
    def search_note_id(self, word: str) -> dict[str,str,str]:
        result: list[dict[str,str,str]] = []
        for note in self._notes:
            if word in note['id']:
                result.append(note)
        return result
    
    # Метод редактирования заметки
    def edit_note(self,new: dict, index: int) -> str:
        for note in self._notes:
            if index == note.get('id'):
                note['title'] = new.get('title', note.get('title'))
                note['text'] = new.get('text', note.get('text'))
                new_date = datetime.datetime.today().strftime("%d/%m/%Y - %H:%M")
                note['date'] = str(new_date)
                return note.get('title')
            
    # Метод удаления заметки
    def delete_note(self, index: int) -> str:
        for note in self._notes:
            if index == note.get('id'):
                title = note.get('title')
                self._notes.remove(note)
                return title
            
    # Метод нумерации ID
    def new_ids(self):
        new_id = 0
        for note in self._notes:
            new_id = new_id + 1
            note['id'] = str(new_id)
        return self._notes

            
            
    
            

    


    







