"""
GAE request handlers for Sirious Margaritas.

"""

import webapp2
import urllib2
from google.appengine.ext import db

from margaritas import TwilioMargaritas

# Config
IMPURL = 'https://api.electricimp.com/v1/<code1>/<code2>'

# Global variables
tw_margarita = TwilioMargaritas(IMPURL)

        
class MainHandler(webapp2.RequestHandler):    
    def get(self):         
        """Show # of margaritas poured when user goes to the app homepage.
        """
        
        global tw_margarita
        self.response.out.write('I love margaritas! ')
        self.response.out.write('%d margaritas served so far. ' % tw_margarita.getCount())
            
            
class TwilioHandler(webapp2.RequestHandler):
    def get(self):
        """Process GET requests from Twilio containing message body.
        """
               
        global tw_margarita
        success = tw_margarita.ProcessRequest(self.request)
        self.response.out.write('Success: %s' % success)
        

app = webapp2.WSGIApplication([('/', MainHandler),
                                ('/tw', TwilioHandler)],
                              debug=True)
