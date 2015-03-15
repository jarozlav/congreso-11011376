from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import db
import logging

class Conferencia(db.Model):
    nombre = db.StringProperty()
    ponente = db.StringProperty()#db.IntegerProperty() #Ponente que dara la conf
    academia = db.StringProperty()#db.IntegerProperty() #ISC, IQ, IE
    fecha = db.StringProperty()
    lugar = db.StringProperty()
    hora = db.StringProperty()
    precio = db.FloatProperty()

class Curso(db.Model):
    nombre = db.StringProperty()
    instructor = db.StringProperty()#db.IntegerProperty() #Ponente que dara el curso
    academia = db.StringProperty()#db.IntegerProperty()
    fecha_inicio = db.StringProperty()
    fecha_fin = db.StringProperty()
    lugar = db.StringProperty()
    hora = db.StringProperty()
    precio = db.FloatProperty()
    
class Ponente(db.Model):
    nombre = db.StringProperty()
    ap_paterno = db.StringProperty()
    ap_materno = db.StringProperty()
    especialidad = db.StringProperty()
    esc_origen = db.IntegerProperty()
    
class Academia(db.Model):
    academia = db.StringProperty()
    
class Escuela(db.Model):
    escuela = db.StringProperty()
    