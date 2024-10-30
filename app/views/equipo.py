from flask import Blueprint, render_template, request, redirect, url_for
from ..models import db, Equipo

equipo_bp = Blueprint('equipo', __name__, url_prefix='/equipos')

@equipo_bp.route('/')
def index():
    equipos = Equipo.query.all()
    return render_template('equipos/index.html', equipos=equipos)

@equipo_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        costo = request.form['costo']
        equipo = Equipo(nombre=nombre, categoria=categoria, costo=costo)
        db.session.add(equipo)
        db.session.commit()
        return redirect(url_for('equipo.index'))
    return render_template('equipos/create.html')
