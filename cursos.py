import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db


template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class CursosPage(webapp2.RequestHandler):
  def post(self):
    if(self.request.get('academia')):
      cursos = db.Query(models.Curso).filter('academia', self.request.get('academia'))
    else:
      cursos = models.Curso.all()

    template = template_env.get_template('cursos.html')
    context = {
      'cursos' : cursos,
      'user' : '1'
    }
    self.response.out.write(template.render(context))
      
  def get(self):
    cursos = models.Curso.all()
    template = template_env.get_template('cursos.html')
    context = {
      'cursos' : cursos,
      'user' : '1'
    }
    self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/cursos', CursosPage)],
				     debug=True)
