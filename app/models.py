from . import db

class Equipo(db.Model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelos.id'))
    categoria = db.Column(db.String(50))
    costo = db.Column(db.Float)
    # Definir otros campos y relaciones

class Modelo(db.Model):
    __tablename__ = 'modelos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricantes.id'))
    # Definir otros campos y relaciones
