from __future__ import division
__author__ = 'zavidan'
try:
    import matplotlib.pyplot as plt
except:
    pass
import webapp2
import cgi
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users
import html
import outside_temps
import StringIO
import numpy as np
import numpy.linalg as la
from heat_simulation import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html.startpage)

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
