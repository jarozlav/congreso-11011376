import datetime
import jinja2
import os
import webapp2
import models


#from google.appengine.api import users

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class MainPage(webapp2.RequestHandler):
  def get(self):
    if(not self.isExist()):
      self.base_datos()
    
    template = template_env.get_template('login.html')
    self.response.out.write(template.render())
    
  def isExist(self):
    academias = models.Academia.all()
    exist = False
    for academia in academias:
      if academia.academia is not None:
	exist = True
	break
      if academia.academia != '':
	exist = True
	break
    return exist
  
    
  def base_datos(self):
    self.academias()
    self.cursos()
    self.conferencias()
    
  def academias(self):
    names = ['ISC','IGE','IQ']
    for name in names:
      academia = models.Academia()
      academia.academia = name
      academia.put()
  
  def cursos(self):
    c1 = models.Curso()
    c1.nombre = 'Introduccion a las bases de datos'
    c1.instructor = 'Martinez Martinez Pedro'
    c1.academia = 'ISC'
    c1.fecha_inicio = '21-09-2015'
    c1.fecha_fin = '27-09-2015'
    c1.lugar = 'LC 17'
    c1.hora = '8:00'
    c1.precio = 350.00
    c1.put()
    c1 = models.Curso()
    c1.nombre = 'Espiritu emprendedor'
    c1.instructor = 'Contreras Vazques Esther'
    c1.academia = 'IGE'
    c1.fecha_inicio = '21-09-2015'
    c1.fecha_fin = '27-09-2015'
    c1.lugar = 'Salon 15'
    c1.hora = '9:00'
    c1.precio = 400.00
    c1.put()
    c1 = models.Curso()
    c1.nombre = 'Termodinamica'
    c1.instructor = 'Soler Marquez Esperanza'
    c1.academia = 'IQ'
    c1.fecha_inicio = '21-09-2015'
    c1.fecha_fin = '27-09-2015'
    c1.lugar = 'LQ 3'
    c1.hora = '8:30'
    c1.precio = 550.00
    c1.put()
  
  def conferencias(self):
    c1 = models.Conferencia()
    c1.nombre = 'Algoritmos de busqueda'
    c1.ponente = 'Solano Espinosa Luis'
    c1.academia = 'ISC'
    c1.fecha = '21-09-2015'
    c1.hora = '10:00'
    c1.precio = 500.00
    c1.put()
    c1 = models.Conferencia()
    c1.nombre = 'Actitudes de negocios'
    c1.ponente = 'Perez Perez Victoria'
    c1.academia = 'IGE'
    c1.fecha = '22-09-2015'
    c1.hora = '11:00'
    c1.precio = 350.00
    c1.put()
    c1 = models.Conferencia()
    c1.nombre = 'Nanotecnologia aplicada'
    c1.ponente = 'Ruiz Solorsano Mercedes'
    c1.academia = 'IQ'
    c1.fecha = '24-09-2015'
    c1.hora = '09:00'
    c1.precio = 650.00
    c1.put()
    
  

application = webapp2.WSGIApplication([('/', MainPage)],
				     debug=True)
