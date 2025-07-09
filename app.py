from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def obtener_conexion():
    return sqlite3.connect('database.db')

def crear_tabla():
    """Crea la tabla 'contactos' si no existe."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

@app.route('/')
def inicio():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM contactos')
    contactos = cursor.fetchall()
    conexion.close()
    return render_template('index.html', contactos=contactos)

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre  = request.form['nombre']
        telefono = request.form['telefono']
        email   = request.form['email']
        
      

           

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)',
            (nombre, telefono, email)
        )
        conexion.commit()
        conexion.close()

        return redirect('/')
    return render_template('agregar.html')

@app.route('/buscar', methods=["GET","POST"])
def buscar():
    resultados = []
    if request.method == "POST":
        termino = request.form['termino']
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM contactos WHERE nombre LIKE ?', ('%' + termino + '%',))
        resultados = cursor.fetchall()
        conexion.close()
    return render_template('buscar.html', resultados=resultados)
    
@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    if request.method == "POST":
        nombre  = request.form['nombre']
        telefono = request.form['telefono']
        email   = request.form['email']
        
        cursor.execute(
            'UPDATE contactos SET nombre = ?, telefono = ?, email = ? WHERE id = ?',
            (nombre, telefono, email, id)
        )
        conexion.commit()
        conexion.close()
        return redirect('/')
    
    cursor.execute('SELECT * FROM contactos WHERE id = ?', (id,))
    contacto = cursor.fetchone()
    conexion.close()
    
    return render_template('editar.html', contacto=contacto)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM contactos WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    return redirect('/')

if __name__ == '__main__':
    
    crear_tabla()         # Asegura que la tabla exista antes de arrancar
    app.run(debug=True)

