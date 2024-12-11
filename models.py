
class Note:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []
        self.next_id = 1

    def add_note(self, title, content):
        note = Note(note_id=self.next_id, title=title, content=content)
        self.notes.append(note)
        self.next_id += 1

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
            return None

    def edit_note(self, note_id, title, content):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.content = content
            return note
        return None

    def remove_note(self, note_id):
        note = self.notes[note_id]
        self.notes.remove(note)