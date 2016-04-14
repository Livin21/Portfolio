import webapp2
import urllib2,json
import jinja2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import mail
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SplashHandler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'onload.html')
        self.response.out.write(template.render(path, {}))

class MainHandler(webapp2.RequestHandler):
	def post(self):
		output=self.validate(self.request.get('subject'),self.request.get('message'));
		output=json.dumps(output)
		self.response.out.write(output)

	def validate(self,subject,messagebody):
		message = mail.EmailMessage()
		message.sender = "\"MyPortfolio\" <jarvis@portfolio-website-1260.appspotmail.com>";
		message.to = "livin@lmntrx.com";
		message.subject=subject;
		message.body=messagebody;
		message.send()
		return {'login_url':"",'message':"sucess"};

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render({}))
		
app = webapp2.WSGIApplication([
	(r'/', SplashHandler),
    ('/more', MainHandler),
    ('/post', MainHandler)
], debug=True)
