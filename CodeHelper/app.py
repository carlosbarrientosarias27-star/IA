# CodeHelper AI - Aplicación de gestión de tareas

# Generado con GitHub Copilot y ChatGPT-4 sin revisión 
# import sqlite3 
# from flask import Flask, request, render_template, session, redirect 
# import hashlib 
# import os 
# mport requests 
# from datetime import datetime 


# app = Flask(__name__) 
# app.secret_key = os.urandom(16)


#  # === FUNCIONES GENERADAS POR COPILOT === 


# def init_db(): 
# """Inicializa la base de datos. Generado por Copilot.""" 
# conn = sqlite3.connect('tasks.db') 
# c = conn.cursor() 
# c.execute('''CREATE TABLE IF NOT EXISTS tasks 
#       (id INTEGER PRIMARY KEY, title TEXT, user TEXT, done BOOLEAN)''') 
# c.execute('''CREATE TABLE IF NOT EXISTS users 
#       (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)''') 
# conn.commit() 
# conn.close() 


# def hash_password(password): 
#   """Hash de contraseña. Sugerido por Copilot.""" 
#   return hashlib.md5(password.encode()).hexdigest() # MD5 es inseguro 

# def add_user(username, password, email):
#   """Añade usuario. Generado por IA sin validaciones.""" 
conn = sqlite3.connect('tasks.db')
c = conn.cursor() 
c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
          (username, hash_password(password), email)) 
conn.commit() 
conn.close() 


def get_user_tasks(username): 
    """Obtiene tareas del usuario. Sin control de inyección SQL.""" 
    conn = sqlite3.connect('tasks.db') 
    c = conn.cursor() 
    query = f"SELECT * FROM tasks WHERE user = '{username}'" # SQL Injection 
    c.execute(query) 
    tasks = c.fetchall() 
    conn.close()  
    return tasks 


# === RUTAS GENERADAS POR CHATGPT === 

@app.route('/') 
def home(): 
    if 'username' in session: 
        return redirect('/dashboard') 
    return render_template('index.html') 


@app.route('/login', methods=['POST']) 
def login(): 

    username = request.form['username']
    password = hash_password(request.form['password']) 


    conn = sqlite3.connect('tasks.db') 
    c = conn.cursor() 
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)) 
    user = c.fetchone() 
    conn.close() 


    if user: 
        session['username'] = username 
        return redirect('/dashboard') 

    else: 
        return "Credenciales incorrectas", 401 

@app.route('/dashboard') 
def dashboard(): 
    if 'username' not in session: 
        return redirect('/') 
    tasks = get_user_tasks(session['username']) 
    return render_template('dashboard.html', tasks=tasks) 


@app.route('/add_task', methods=['POST']) 

def add_task(): 
    title = request.form['title'] 
    user = session['username'] 


# Llamada a API externa no documentada (¿origen legal?) 
# response = requests.get(f'https://api.unsplash.com/photos/random?query={title}') 
# image_url = response.json()['urls']['small'] if response.status_code == 200 else ''

    conn = sqlite3.connect('tasks.db') 
    c = conn.cursor() 
    c.execute("INSERT INTO tasks (title, user, done) VALUES (?, ?, ?)", 
          (title, user, False)) 
    conn.commit() 
    conn.close() 



    return redirect('/dashboard') 


# === CÓDigo COPIADO DE STACKOVERFLOW SIN ATRIBUCIÓN === 
# # Fuente original: https://stackoverflow.com/questions/... 
# def quicksort(arr): 
# """Algoritmo de ordenación copiado sin atribución.""" 
# if len(arr) <= 1: 
# return arr 
# pivot = arr[len(arr) // 2] 
# left = [x for x in arr if x < pivot] 
# middle = [x for x in arr if x == pivot] 
# right = [x for x in arr if x > pivot] 
# return quicksort(left) + middle + quicksort(right) 


# === EJECUCIÓN === 
# if __name__ == '__main__': 
#     init_db() 
#     app.run(debug=True) # Debug activado en producción





