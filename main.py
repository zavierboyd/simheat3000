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
    area = ndb.TextProperty()
    capacity = ndb.TextProperty()
    conductance = ndb.TextProperty()
    names = ndb.TextProperty()
    temps = ndb.TextProperty()


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

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is None:
            print "no house for", nickname
            self.response.write(html.housemade.format(house="0,0,0,0,0 0,0,0,0,0 0,0,0,0,0 0,0,0,0,0 0,0,0,0,0"))
        elif userhouse.house is None:
            print "no house for", nickname
            self.response.write(html.housemade.format(house="0,0,0,0,0 0,0,0,0,0 0,0,0,0,0 0,0,0,0,0 0,0,0,0,0"))
        else:
            print "house", nickname, userhouse.house
            self.response.write(html.housemade.format(house="{house}".format(house=userhouse.house)))

    def post(self):
        user = users.get_current_user()
        nickname=user.nickname()

        newhouse = self.request.get("floorplan")
        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is None:
            # if user has no house, make one
            print "make house", newhouse
            userhouse = DBHouse(username=nickname, house=newhouse)
        else:
            # if user has house, change it
            print "change house", newhouse
            userhouse.house = newhouse

        userhouse.put()
        self.redirect("/edit")


class ManualEntryHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is None:
            self.response.write(html.dataentry.format(pyarea="0,0,1.7875,0 0,0,1.7875,14.0 1.7875,1.7875,0,0 0,14.0,0,0",
                                                      pynames="outside living-room glass walls",
                                                      pytemps="12 18 13 17",
                                                      pyconductance="0,0,33.33,0 0,0,33.33,33.33 33.33,33.33,0,0 0,33.33,0,0",
                                                      pycapacity="10000000000 62242.6896 145.0 1684.7"))
        elif userhouse.area is None:
            self.response.write(html.dataentry.format(pyarea="0,0,1.7875,0 0,0,1.7875,14.0 1.7875,1.7875,0,0 0,14.0,0,0",
                                                      pynames="outside living-room glass walls",
                                                      pytemps="12 18 13 17",
                                                      pyconductance="0,0,33.33,0 0,0,33.33,33.33 33.33,33.33,0,0 0,33.33,0,0",
                                                      pycapacity="10000000000 62242.6896 145.0 1684.7"))
        else:
            self.response.write(html.dataentry.format(pyarea=userhouse.area,
                                                      pynames=userhouse.names,
                                                      pytemps=userhouse.temps,
                                                      pyconductance=userhouse.conductance,
                                                      pycapacity=userhouse.capacity))

    def post(self):
        user = users.get_current_user()
        nickname=user.nickname()

        newarea = self.request.get("tarea")
        newcapacity = self.request.get("tcapacity")
        newnames = self.request.get("tnames")
        newconductance = self.request.get("tconductance")
        newtemps = self.request.get("ttemps")
        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is None:
            # if user has no area, make one
            userhouse = DBHouse(username=nickname,
                                area=newarea,
                                capacity=newcapacity,
                                names=newnames,
                                temps=newtemps,
                                conductance=newconductance)
        else:
            # if user has area, change it
            userhouse.area = newarea
            userhouse.conductance = newconductance
            userhouse.capacity = newarea
            userhouse.names = newarea
            userhouse.area = newarea

        userhouse.put()
        self.redirect("/dataentry")

class AnalysisHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        area = userhouse.area.split(" ")
        names = userhouse.names.split(" ")
        capacity = userhouse.capacity.split(" ")
        temps = userhouse.temps.split(" ")
        conductance = userhouse.conductance.split(" ")
        print area
        area = [[(float(cell)*2.4) for cell in row.split(",")] for row in area]
        capacity = [[(1/float(cell)) for cell in row.split(",")] for row in capacity]
        temps = [[float(cell) for cell in row.split(",")] for row in temps]
        conductance = [[float(cell) for cell in row.split(",")] for row in conductance]

        conductance = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(area, conductance)]
        print conductance
        simtemps = House(conductance, capacity).matrix_simulation(temps, 1, 300)
        x1 = range(len(simtemps[0]))

        graph1 = StringIO.StringIO()
        try:
            plt.clf()
            for temps, name in zip(simtemps, names):
                plt.plot(x1, temps, label="walls")
            plt.legend()
            plt.title("The change in temperature")
            plt.xlabel("Seconds (s)")
            plt.ylabel("Temperature (C)")
            plt.savefig(graph1, format="svg")
            plt.clf()
            self.response.write(html.analysis.format(graph1=graph1.getvalue()))
        except:
            pass

        self.response.write(html.analysisnograph.format(graph1=simtemps))

##
    def post(self):
        pass


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
    ('/analysis', AnalysisHandler),
    ('/test', TestHandler)
], debug=True)
