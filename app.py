from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

to_do_items = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def add_note():
    to_do_items.append({"date":request.form['date'],"note":request.form['note']})
    return render_template('todo.html', to_do_items=to_do_items)

if __name__ == '__main__':
    app.run()

