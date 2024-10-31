from flask import Blueprint, render_template, request, redirect, url_for
from ..models import db, Modelo

modelo_bp = Blueprint('modelo', __name__, url_prefix='/modelos')

@modelo_bp.route('/')
def index():
    modelos = Modelo.query.all()
    return render_template('modelos/index.html', modelos=modelos)

@modelo_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        modelo = Modelo(nombre=nombre, fabricante_id=fabricante_id)
        db.session.add(modelo)
        db.session.commit()
        return redirect(url_for('modelo.index'))
    return render_template('modelos/create.html')

@modelo_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    modelo = Modelo.query.get_or_404(id)
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        modelo.nombre = nombre
        modelo.fabricante_id = fabricante_id
        db.session.commit()
        return redirect(url_for('modelo.index'))
    
    return render_template('modelos/edit.html', modelo=modelo)

@modelo_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    modelo = Modelo.query.get_or_404(id)
    db.session.delete(modelo)
    db.session.commit()
    return redirect(url_for('modelo.index'))
