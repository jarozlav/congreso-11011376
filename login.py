#import datetime
import jinja2
import os
#from webapp2_extras import sessions
import webapp2
import models
from google.appengine.ext import db

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class LoginPage(webapp2.RequestHandler):
    def post(self):
      user = self.request.get('user')
      passw = self.request.get('pass')
      context = {}
      if(not self.isNoneorEmpty(user, passw)):
	academias = models.Academia.all()
	template = template_env.get_template('index.html')
	context['user'] = user
	context['academias'] = academias
      else:
        template = template_env.get_template('login.html')
	context['error'] = 'No ingresaste usuario ni contrasenia'
      
      self.response.out.write(template.render(context))
      
            
    def get(self):
      template = template_env.get_template('login.html')
      self.response.out.write(template.render())


    def isNoneorEmpty(self, user, passw):
        if(user is None and passw is None):
            return True
        if(user == '' and passw == ''):
            return True
        return False
     
application = webapp2.WSGIApplication([('/login', LoginPage)],
				     debug=True)
