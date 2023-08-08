import datetime
class Notes:

    def __init__(self, path: str='notes.csv'):
        self._notes: list[dict[str, str, str]] = []
        self._path = path
        self._last_id = 0

    def create_note(self, new: dict[str, str, str]) -> str:
        new_id = int(self._last_id) + 1
        new['id'] = str(new_id)
        new_date = datetime.datetime.today().strftime("%d/%m/%Y - %H:%M")
        new['date'] = str(new_date)
        self._notes.append(new)
        self._last_id += 1
        return new.get('title')
    
    def save_notes(self):
        data = []
        for note in self._notes:
            data.append(';'.join([note['id'], note['date'], note['title'], note['text']]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(data)

    def load_notes(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for note in data:
            note = note.strip().split(';')
            new = {'id': note[0], 'date': note[1], 'title': note[2], 'text': note[3]}
            self._notes.append(new)
        for field in self._notes:
            self._last_id = max(self._last_id, int(field.get('id')))
        
    
    def show_notes(self):
        return self._notes
    
    def search_note(self, word: str) -> dict[str,str,str]:
        result: list[dict[str,str,str]] = []
        for note in self._notes:
            if word.lower() in note['title'].lower() or word in note['id'] or word in note['date']:
                result.append(note)
        return result
    
    def search_note_id(self, word: str) -> dict[str,str,str]:
        result: list[dict[str,str,str]] = []
        for note in self._notes:
            if word in note['id']:
                result.append(note)
        return result
    
    def edit_note(self,new: dict, index: int) -> str:
        for note in self._notes:
            if index == note.get('id'):
                note['title'] = new.get('title', note.get('title'))
                note['text'] = new.get('text', note.get('text'))
                new_date = datetime.datetime.today().strftime("%d/%m/%Y - %H:%M")
                note['date'] = str(new_date)
                return note.get('title')
            
    def delete_note(self, index: int) -> str:
        for note in self._notes:
            if index == note.get('id'):
                title = note.get('title')
                self._notes.remove(note)
                return title

            
            
    
            

    


    







