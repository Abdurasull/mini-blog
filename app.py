import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# JSON fayl nomi
TASKS_FILE = 'tasks.json'

# JSON faylidan vazifalarni o'qish
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
    except :
        tasks = []  # Fayl topilmasa bo'sh ro'yxat qaytariladi
    return tasks

# JSON fayliga vazifalarni yozish
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

@app.route('/')
def index():
    # tasks = load_tasks()  # Vazifalarni fayldan o'qish
    return render_template('index1.html')

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    muallif = request.form.get('muallif')
    price = request.form.get('price')
    dict_1 = {}
    dict_1['name'] = title
    dict_1['author'] = muallif
    dict_1['price'] = price
    if title:
        tasks = load_tasks()
        tasks.append(dict_1)  # Yangi kitobni qo‘shish
        save_tasks(tasks)  # O‘zgartirilgan bazani faylga yozish
    return redirect('/index1.html')

@app.route('/delete/<int:index>')
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)  # Vazifani o‘chirish
        save_tasks(tasks)  # O‘zgartirilgan ro‘yxatni faylga yozish
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
