class Notes:

    def __init__(self, path: str='notes.csv'):
        self._notes: list[dict[str, str, str]] = []
        self._path = path
        self._last_id = 0

    def create_note(self, new: dict[str, str, str]) -> str:
        new_id = int(self._last_id) + 1
        new['id'] = str(new_id)
        self._notes.append(new)
        self._last_id += 1
        return new.get('title')
    
    def save_notes(self):
        data = []
        for note in self._notes:
            data.append(';'.join([note['id'], note['title'], note['date'], note['text']]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write(data)

    def load_notes(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for note in data:
            note = note.strip().split(';')
            new = {'id': note[0], 'title': note[1], 'date': note[2], 'text': note[3]}
            self._notes.append(new)
    
    def show_notes(self):
        return self._notes
    
    def search_note(self, word: str) -> dict[str,str,str]:
        result: list[dict[str,str,str]] = []
        for note in self._notes:
            if word.lower() in note['title'].lower():
                result.append(note)
                break
        return result
    


    







