from flask import Flask, render_template, request, redirect, url_for
from models import NoteManager
app = Flask(__name__)

note_manager = NoteManager()
to_do_items = []
@app.route('/')
def index():
    notes = note_manager.get_all_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST', "GET"])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note_manager.add_note(title, content)
        return redirect(url_for('index'))
    return render_template('add_note.html')

@app.route('/edit/<int:note_id>', methods=['POST', "GET"])
def edit_note(note_id):
    note= note_manager.get_note_by_id(note_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note_manager.edit_note(note_id, title, content)
        return redirect(url_for('index'))
    return render_template('edit_note.html', note=note)

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    note_manager.delete_note(note_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

