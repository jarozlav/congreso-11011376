#import datetime
import jinja2
import os
import webapp2
import models



template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))


class IndexPage(webapp2.RequestHandler):
  def get(self):
    academias = models.Academia.all()
    context = {
      'user' : '1',
      'academias' : academias
    }
    template = template_env.get_template('index.html')
  
    self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/index', IndexPage)],
				     debug=True)
