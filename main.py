#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import division
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
import StringIO
from heat_simulation import *


class DBHouse(ndb.Model):
    username = ndb.StringProperty()
    house = ndb.TextProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        housequery = DBHouse.query(DBHouse.username == user.nickname())
        userhouse = housequery.get()
        self.response.write(html.startpage)

    def post(self):
        pass


class EditHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname=user.nickname()

        edit="""
        <p>Hello {user}!</p>
        <p>Make A House!</p>
        """.format(user=nickname)
        housequery = DBHouse.query(DBHouse.username == user.nickname())
        userhouse = housequery.get()
        if userhouse == None:
            self.response.write(html.makinghouse.format(edit=edit))
        else:
            self.response.write(html.housemade.format(house="{house}".format(house=userhouse.house)))

    def post(self):
        user = users.get_current_user()
        nickname=user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse == None:
            plan = DBHouse(username=nickname, house=self.request.get("data"))
            plan.put()
            userhouse = plan
        else:
            userhouse.house = self.request.get("data")
            userhouse.put()

        self.redirect("/edit")


class ManualEntryHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        self.response.write(html.dataentry)

    def post(self):
        user = users.get_current_user()

        self.response.write(html.dataentry)


class TestHandler(webapp2.RequestHandler):
    def get(self):
        y1 = House([[0, 269.0, 0, 0], [269.0, 0, 41.0, 0], [0, 41.0, 0, 91.0], [0, 0, 91.0, 0]],
                  [[1/278667.0], [1/45600.0], [1/47040.0], [1/10.0**9]]).matrix_simulation([[18.0], [20.0], [13.0], [12.0]], 1, 300)
        x1 = range(len(y1[0]))
        y2 = House([[0, 269.0, 0, 0], [269.0, 0, 41.0, 0], [0, 41.0, 0, 91.0], [0, 0, 91.0, 0]],
                  [[1/278667.0], [1/45600.0], [1/47040.0], [1/10.0**9]]).matrix_simulation([[18.0], [20.0], [13.0], [12.0]], 1, 2000)
        x2 = range(len(y2[0]))
        self.response.write("""This is a simple example of how I have calculated the temperatures<br><br>
        The initial wall temperature is 17 C, the initial air temperature is 20 C,
        thermal capacity of the wall is 280000.0 J/C, thermal capacity of the air is 46000.0 J/C,
        the thermal conductance between the wall and air is 270.0 W/C (thermal resistance is 0.0037),
        and the change in time is 1 second.<br>
        First calculate how fast the thermal energy is moving from the walls to the air and the air to the walls from the thermal conductance multiplied
        by the temperature.<br>
        Second calculate the change in thermal energy from how fast the thermal energy is moving multiplied the change in time.<br>
        Third add the thermal energy coming in to the amount of current thermal energy in the thermal mass and subtract the amount of thermal energy going out.<br>
        Fourth calculate the temperature from the thermal energy in the thermal mass divided by the thermal capacity.<br>
        Fifth repeat until equilibrium reached.<br>
        This method became complicated fast when I added more thermal masses, so to make it simpler I created a matrix formula to do it.
        My big project is so that people can design heat efficient housing and renovations using this simulator.""")

        image1 = StringIO.StringIO()
        image2 = StringIO.StringIO()
        try:
            plt.clf()
            walls = plt.plot(x1, y1[0], label="walls")
            air = plt.plot(x1, y1[1], label="air")
            window = plt.plot(x1, y1[2], label="window")
            outside = plt.plot(x1, y1[3], label="outside")
            plt.legend()
            plt.title("The change in temperature")
            plt.xlabel("Seconds (s)")
            plt.ylabel("Temperature (C)")
            plt.savefig(image1, format="svg")
            plt.clf()
            walls = plt.plot(x2, y2[0], label="walls")
            air = plt.plot(x2, y2[1], label="air")
            window = plt.plot(x2, y2[2], label="window")
            outside = plt.plot(x2, y2[3], label="outside")
            plt.legend()
            plt.title("The change in temperature")
            plt.xlabel("Seconds (s)")
            plt.ylabel("Temperature (C)")
            plt.savefig(image2, format="svg")
        except:
            pass
        self.response.write("<p>{image}</p>".format(image=image1.getvalue()))
        self.response.write("<p>{image}</p>".format(image=image2.getvalue()))
        self.response.write("""<a href="http://heat-simulation.appspot.com/">Back to main page</a>""")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/edit', EditHandler),
    ('/dataentry', ManualEntryHandler),
    ('/test', TestHandler)
], debug=True)
