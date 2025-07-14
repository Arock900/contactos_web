from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://contactos_db_haiu_user:1sKvnRSG3Jb0v7Of2oWHOY4A5fKPzkwh@dpg-d1qn95je5dus73f56dkg-a.oregon-postgres.render.com/contactos_db_haiu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'mi_clave_secreta'

db = SQLAlchemy(app)

# Modelo Contacto
class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)

@app.route('/')
def inicio():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        nuevo_contacto = Contacto(nombre=nombre, telefono=telefono, email=email)
        db.session.add(nuevo_contacto)
        db.session.commit()

        flash('Contacto agregado exitosamente', 'success')
        return redirect(url_for('inicio'))

    return render_template('agregar.html')

@app.route('/buscar', methods=["GET", "POST"])
def buscar():
    resultados = []
    if request.method == "POST":
        termino = request.form['termino']
        resultados = Contacto.query.filter(Contacto.nombre.ilike(f'%{termino}%')).all()
    return render_template('buscar.html', resultados=resultados)

@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id):
    contacto = Contacto.query.get_or_404(id)

    if request.method == "POST":
        contacto.nombre = request.form['nombre']
        contacto.telefono = request.form['telefono']
        contacto.email = request.form['email']

        db.session.commit()

        flash("Contacto actualizado correctamente", "success")
        return redirect(url_for('inicio'))

    return render_template('editar.html', contacto=contacto)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    contacto = Contacto.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    flash("Contacto eliminado correctamente", "success")
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Crear la tabla si no existe
    app.run(debug=True)
