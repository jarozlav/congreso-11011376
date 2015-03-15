#import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.ext import db

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class ConferenciasPage(webapp2.RequestHandler):
  def post(self):
    if(self.request.get('academia')):
      conferencias = db.Query(models.Conferencia).filter('academia', self.request.get('academia'))
    else:
      conferencias = models.Conferencia.all()
    
    template = template_env.get_template('conferencias.html')
    context = {
      'conferencias' : conferencias,
      'user' : '1'
    }
    self.response.out.write(template.render(context))
    
      
  def get(self):
    conferencias = models.Conferencia.all()
    template = template_env.get_template('conferencias.html')
    context = {
      'conferencias' : conferencias,
      'user' : '1'
    }
    self.response.out.write(template.render(context))
      

application = webapp2.WSGIApplication([('/conferencias', ConferenciasPage)],
				     debug=True)
