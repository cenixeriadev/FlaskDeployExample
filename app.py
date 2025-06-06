from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tu-clave-secreta-por-defecto')

tareas = [
    {"id": 1, "titulo": "Ejemplo de tarea", "descripcion": "Esta es una tarea de ejemplo", "completada": False},
    {"id": 2, "titulo": "Configurar aplicación", "descripcion": "Configurar la aplicación Flask", "completada": True}
]

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        
        if titulo:
            nueva_tarea = {
                "id": len(tareas) + 1,
                "titulo": titulo,
                "descripcion": descripcion,
                "completada": False
            }
            tareas.append(nueva_tarea)
            flash('Tarea agregada exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('El título es obligatorio', 'error')
    
    return render_template('agregar.html')

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = not tarea['completada']
            flash('Tarea actualizada!', 'success')
            break
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [tarea for tarea in tareas if tarea['id'] != tarea_id]
    flash('Tarea eliminada!', 'success')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)