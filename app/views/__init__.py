from flask import Blueprint

# Importar todos los Blueprints de las vistas
from .equipo import equipo_bp
#from .modelo import modelo_bp

# Crear un Blueprint para la raíz
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Hello, World!"

def register_blueprints(app):
    app.register_blueprint(equipo_bp)
    #app.register_blueprint(modelo_bp)
    app.register_blueprint(main_bp)  # Registrar el Blueprint de la raíz
