import os
from flask import Blueprint, send_from_directory, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/test')
def test():
    return "Test endpoint is working!"

@main_bp.route('/', defaults={'path': ''})
@main_bp.route('/<path:path>')
def serve(path):
    if path and os.path.exists(current_app.static_folder + '/' + path):
        return send_from_directory(current_app.static_folder, path)
    else:
        return send_from_directory(current_app.static_folder, 'index.html')

def register_blueprints(app):
    from .equipo import equipo_bp
    from .modelo import modelo_bp

    app.register_blueprint(equipo_bp)
    app.register_blueprint(modelo_bp)
    app.register_blueprint(main_bp)
