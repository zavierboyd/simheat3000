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
import os
import webapp2
import cgi
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users

## import Jinja2 later
#import jinja2
#env = jinja2.Enviroment(
#    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/html")
#)


import html
import outside_temps
import StringIO
import numpy as np
import numpy.linalg as la
from heat_simulation import *

logo = "/logo/Logo.png"

class DBHouse(ndb.Model):
    username = ndb.StringProperty()
    house = ndb.TextProperty()
    area = ndb.TextProperty()
    capacity = ndb.TextProperty()
    conductance = ndb.TextProperty()
    names = ndb.TextProperty()
    temps = ndb.TextProperty()
    winarea = ndb.TextProperty()
    winconductance = ndb.TextProperty()
    rofarea = ndb.TextProperty()
    rofconductance = ndb.TextProperty()


class DBQuickHouse(ndb.Model):
    username = ndb.StringProperty()
    mainroom = ndb.StringProperty()
    mainwinarea = ndb.TextProperty()
    fullwinarea = ndb.TextProperty()
    mainexternal = ndb.TextProperty()
    maininternal = ndb.TextProperty()
    fullexternal = ndb.TextProperty()
    fullrwindows = ndb.TextProperty()
    mainrinternal = ndb.TextProperty()
    fullrexternal = ndb.TextProperty()
    fullrroof = ndb.TextProperty()
    mainrexternal = ndb.TextProperty()
    mainrwindows = ndb.TextProperty()
    mainrroof = ndb.TextProperty()
    mainrfloor = ndb.TextProperty()
    fullrfloor = ndb.TextProperty()
    mainsize = ndb.TextProperty()
    fullsize = ndb.TextProperty()


def setdata(nickname):
    userhouseq = DBQuickHouse(
        username=nickname,
        mainroom="Room",
        mainwinarea='4.29',
        fullwinarea='26.66',
        mainexternal='4',
        maininternal='14',
        fullexternal='44',
        fullrwindows='0.17',
        mainrinternal='0.6',
        fullrexternal='0.54',
        fullrroof='0.5',
        mainrexternal='0.54',
        mainrwindows='0.17',
        mainrroof='0.5',
        mainrfloor='1',
        fullrfloor='1',
        mainsize='20',
        fullsize='103.548')
    userhouseq.put()
    area = """0,{Minwall},{Mexwall} {Minwall},0,{Hexwall} {Mexwall},{Hexwall},0""".format(Minwall=float(userhouseq.maininternal),
                                                                                              Mexwall=float(userhouseq.mainexternal),
                                                                                              Hexwall=float(userhouseq.fullexternal)-float(userhouseq.mainexternal))
    winarea = """0,0,{Mwin} 0,0,{Hwin} {Mwin},{Hwin},0""".format(Mwin=float(userhouseq.mainwinarea),
                                                                 Hwin=float(userhouseq.fullwinarea)-float(userhouseq.mainwinarea))
    rofarea = """0,0,{Mroof} 0,0,{Hroof} {Mroof},{Hroof},0""".format(Mroof=float(userhouseq.mainsize),
                                                                     Hroof=float(userhouseq.fullsize))
    rofconductance="""0,0,{Muroof} 0,0,{Huroof} {Muroof},{Huroof},0""".format(Muroof=1/(float(userhouseq.mainrroof)),
                                                                              Huroof=1/(float(userhouseq.fullrroof)))
    names = """{M} Rest-of-the-House Outside""".format(M=userhouseq.mainroom)
    winconductance = "0,0,{Muwin} 0,0,{Huwin} {Muwin},0,{Huwin}".format(Muwin=1/(float(userhouseq.mainrwindows)),
                                                                        Huwin=1/(float(userhouseq.fullrwindows)))
    conductance = """0,{uin},{Muex} {uin},0,{uex} {Muex},{uex},0""".format(uin=1/(float(userhouseq.mainrinternal)),
                                                                         uex=1/(float(userhouseq.fullrexternal)),
                                                                         Muex=1/(float(userhouseq.mainrexternal)))
    capacity = """{Mcapa} {Hcapa} 100000000000000000000""".format(Mcapa=((float(userhouseq.mainsize))*2.4*0.00121)+((200*1000)*4.2),
                                                                  Hcapa=((float(userhouseq.fullsize)-float(userhouseq.mainsize))*2.4*0.00121)+((10*(float(userhouseq.fullsize)-float(userhouseq.mainsize))*1000)*4.2))
    temps = """15 15 15"""
    userhouse = DBHouse(
        username=nickname,
        area=area,
        capacity=capacity,
        names=names,
        temps=temps,
        conductance=conductance,
        winconductance=winconductance,
        winarea=winarea,
        rofarea=rofarea,
        rofconductance=rofconductance)
    userhouse.put()
    return userhouseq,userhouse


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html.startpage)

    def post(self):
        pass

class HouseHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
        userhouseq = housequeryq.get()

        if userhouseq is None:
            userhouseq, userhouse = setdata(nickname)

        self.response.write(html.housemesure.format(
            riwall=userhouseq.maininternal,
            rewall=userhouseq.mainexternal,
            hewall=userhouseq.fullexternal,
            rwindow=userhouseq.mainwinarea,
            hwindow=userhouseq.fullwinarea,
            rfloor=userhouseq.mainsize,
            hfloor=userhouseq.fullsize))

    def post(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
        userhouseq = housequeryq.get()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()

        riwall = self.request.get("RIwall")
        rewall = self.request.get("REwall")
        hewall = self.request.get("HEwall")
        rwindow = self.request.get("Rwindow")
        hwindow = self.request.get("Hwindow")
        rfloor = self.request.get("Rfloor")
        hfloor = self.request.get("Hfloor")
        area = """0,{Minwall},{Mexwall} {Minwall},0,{Hexwall} {Mexwall},{Hexwall},0""".format(Minwall=float(riwall),
                                                                                              Mexwall=float(rewall),
                                                                                              Hexwall=float(hewall)-float(rewall))
        winarea = """0,0,{Mwin} 0,0,{Hwin} {Mwin},{Hwin},0""".format(Mwin=float(rwindow),
                                                                     Hwin=float(hwindow)-float(rwindow))
        rofarea = """0,0,{Mroof} 0,0,{Hroof} {Mroof},{Hroof},0""".format(Mroof=float(rfloor),
                                                                         Hroof=float(hfloor))
        capacity = """{Mcapa} {Hcapa} 100000000000000000000""".format(Mcapa=((float(rfloor))*2.4*0.00121)+((200*1000)*4.2),
                                                                      Hcapa=((float(hfloor)-float(rfloor))*2.4*0.00121))


        userhouse.area = area
        userhouse.capacity = capacity
        userhouse.winarea = winarea
        userhouse.rofarea = rofarea

        userhouseq.username = nickname
        userhouseq.mainwinarea = rwindow
        userhouseq.fullwinarea = hwindow
        userhouseq.mainexternal = rewall
        userhouseq.maininternal = riwall
        userhouseq.fullexternal = hewall
        userhouseq.mainsize = rfloor
        userhouseq.fullsize = hfloor

        userhouseq.put()
        userhouse.put()

        self.response.write(html.housemesure.format(
            riwall=riwall,
            rewall=rewall,
            hewall=hewall,
            rwindow=rwindow,
            hwindow=hwindow,
            rfloor=rfloor,
            hfloor=hfloor))


class SimHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
        userhouseq = housequeryq.get()

        if userhouseq is None:
            userhouseq, userhouse = setdata(nickname)

        self.response.write(html.sim.format(
            irwall=userhouseq.mainrexternal,
            ihwall=userhouseq.fullrexternal,
            irwindow=userhouseq.mainrwindows,
            ihwindow=userhouseq.fullrwindows,
            irroof=userhouseq.mainrroof,
            ihroof=userhouseq.fullrroof,
            irfloor=userhouseq.mainrfloor,
            ihfloor=userhouseq.fullrfloor,))

def savesim(handler):
    user = users.get_current_user()
    nickname = user.nickname()

    housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
    userhouseq = housequeryq.get()

    housequery = DBHouse.query(DBHouse.username == nickname)
    userhouse = housequery.get()

    iriwall = userhouseq.mainrinternal
    irroof = handler.request.get("IRroof")
    ihroof = handler.request.get("IHroof")
    irwindow = handler.request.get("IHwindow")
    ihwindow = handler.request.get("IHwindow")
    irwall = handler.request.get("IHwall")
    ihwall = handler.request.get("IHwall")
    irfloor = handler.request.get("IHfloor")
    ihfloor = handler.request.get("IHfloor")


    rofconductance="""0,0,{Muroof} 0,0,{Huroof} {Muroof},{Huroof},0""".format(Muroof=1/(float(irroof)),
                                                                              Huroof=1/(float(ihroof)))
    winconductance = "0,0,{Muwin} 0,0,{Huwin} {Muwin},0,{Huwin}".format(Muwin=1/(float(irwindow)),
                                                                        Huwin=1/(float(ihwindow)))
    conductance = """0,{uin},{Muex} {uin},0,{uex} {Muex},{uex},0""".format(uin=1/(float(iriwall)),
                                                                         uex=1/(float(ihwall)),
                                                                         Muex=1/(float(irwall)))

    userhouse.rofconductance = rofconductance
    userhouse.winconductance = winconductance
    userhouse.conductance = conductance

    userhouseq.mainrexternal = irwall
    userhouseq.fullrexternal = ihwall
    userhouseq.mainrwindows = irwindow
    userhouseq.fullrwindows = ihwindow
    userhouseq.mainrroof = irroof
    userhouseq.fullrroof = ihroof
    userhouseq.mainrfloor = irfloor
    userhouseq.fullrfloor = ihfloor

    userhouseq.put()
    userhouse.put()


class InfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html.infopage)

    def post(self):
        pass


class PagesHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html.pages)


class EditHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname=user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is None:
            print "no house for", nickname
            house=" ".join(([(",".join(["outside" for i in range(100)])+" ")*50]))
            self.response.write(html.housemade.format(house=house))
        elif userhouse.house is None:
            print "no house for", nickname
            house=" ".join(([(",".join(["outside" for i in range(100)])+" ")*50]))
            self.response.write(html.housemade.format(house=house))
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
        if userhouse.house is None:
            userhouse.house = newhouse
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
            self.response.write(html.dataentry.format(pyarea="0,14.0,0,0 14.0,0,1.7875,0 0,1.7875,0,1.7875 0,0,1.7875,0",
                                                      pynames="walls living-room glass outside",
                                                      pytemps="17 20 13 12",
                                                      pyconductance="0,33.33,0,0 33.33,0,33.33,0 0,33.33,0,33.33 0,0,33.33,0",
                                                      pycapacity="278667.0 45600.0 47040.0 10000000000"))
        elif userhouse.area is None:
            self.response.write(html.dataentry.format(pyarea="0,14.0,0,0 14.0,0,1.7875,0 0,1.7875,0,1.7875 0,0,1.7875,0",
                                                      pynames="walls living-room glass outside",
                                                      pytemps="17 20 13 12",
                                                      pyconductance="0,33.33,0,0 33.33,0,33.33,0 0,33.33,0,33.33 0,0,33.33,0",
                                                      pycapacity="278667.0 45600.0 47040.0 10000000000"))
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
        print newcapacity,"newcapacity"
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
            userhouse.capacity = newcapacity
            userhouse.names = newnames
            userhouse.temps = newtemps

        userhouse.put()
        self.redirect("/dataentry")


class QuickEntryHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
        userhouseq = housequeryq.get()

        if userhouseq is None:
            userhouseq, userhouse = setdata(nickname)


        self.response.write(html.quickenter.format(mainroom=userhouseq.mainroom,
                                                   mainwinarea=float(userhouseq.mainwinarea),
                                                   fullwinarea=float(userhouseq.fullwinarea),
                                                   mainexternal=float(userhouseq.mainexternal),
                                                   maininternal=float(userhouseq.maininternal),
                                                   fullexternal=float(userhouseq.fullexternal),
                                                   rwindows=float(userhouseq.fullrwindows),
                                                   rinternal=float(userhouseq.mainrinternal),
                                                   rexternal=float(userhouseq.fullrexternal),
                                                   rroof=float(userhouseq.fullrroof),
                                                   mainrexternal=float(userhouseq.mainrexternal),
                                                   mainrwindows=float(userhouseq.mainrwindows),
                                                   mainrroof=float(userhouseq.mainrroof),
                                                   mainsize=float(userhouseq.mainsize),
                                                   fullsize=float(userhouseq.fullsize)))


    def post(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequeryq = DBQuickHouse.query(DBQuickHouse.username == nickname)
        userhouseq = housequeryq.get()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()

        mainroom = (self.request.get("main"))
        mainwinarea = (self.request.get("Mwindows"))
        fullwinarea = (self.request.get("Hwindows"))
        mainexternal = (self.request.get("Mexternal"))
        maininternal = (self.request.get("Minternal"))
        fullexternal = (self.request.get("Hexternal"))
        fullrwindows = (self.request.get("Rwindows"))
        mainrinternal = (self.request.get("Rinternal"))
        fullrexternal = (self.request.get("Rexternal"))
        fullrroof = (self.request.get("Rroof"))
        mainrexternal = (self.request.get("MRexternal"))
        mainrwindows = (self.request.get("MRwindows"))
        mainrroof = (self.request.get("MRroof"))
        mainsize = (self.request.get("Msize"))
        fullsize = (self.request.get("Hsize"))
        area = """0,{Minwall},{Mexwall} {Minwall},0,{Hexwall} {Mexwall},{Hexwall},0""".format(Minwall=float(maininternal),
                                                                                              Mexwall=float(mainexternal),
                                                                                              Hexwall=float(fullexternal)-float(mainexternal))
        winarea = """0,0,{Mwin} 0,0,{Hwin} {Mwin},{Hwin},0""".format(Mwin=float(mainwinarea),
                                                                     Hwin=float(fullwinarea)-float(mainwinarea))
        rofarea = """0,0,{Mroof} 0,0,{Hroof} {Mroof},{Hroof},0""".format(Mroof=float(mainsize),
                                                                         Hroof=float(fullsize))
        rofconductance="""0,0,{Muroof} 0,0,{Huroof} {Muroof},{Huroof},0""".format(Muroof=1/(float(mainrroof)),
                                                                                  Huroof=1/(float(fullrroof)))
        names = """{M} Rest-of-the-House Outside""".format(M=mainroom)
        winconductance = "0,0,{Muwin} 0,0,{Huwin} {Muwin},0,{Huwin}".format(Muwin=1/(float(mainrwindows)),
                                                                            Huwin=1/(float(fullrwindows)))
        conductance = """0,{uin},{Muex} {uin},0,{uex} {Muex},{uex},0""".format(uin=1/(float(mainrinternal)),
                                                                             uex=1/(float(fullrexternal)),
                                                                             Muex=1/(float(mainrexternal)))
        capacity = """{Mcapa} {Hcapa} 100000000000000000000""".format(Mcapa=((float(mainsize))*2.4*0.00121)+((200*1000)*4.2),
                                                                      Hcapa=((float(fullsize)-float(mainsize))*2.4*0.00121)+((10*(float(fullsize)-float(mainsize))*1000)*4.2))
        temps = """15 15 15"""

        userhouse.area = area
        userhouse.conductance = conductance
        userhouse.capacity = capacity
        userhouse.names = names
        userhouse.temps = temps
        userhouse.winconductance = winconductance
        userhouse.winarea = winarea
        userhouse.rofarea = rofarea
        userhouse.rofconductance = rofconductance

        userhouseq.username = nickname
        userhouseq.mainroom = mainroom
        userhouseq.mainwinarea = mainwinarea
        userhouseq.fullwinarea = fullwinarea
        userhouseq.mainexternal = mainexternal
        userhouseq.maininternal = maininternal
        userhouseq.fullexternal = fullexternal
        userhouseq.fullrwindows = fullrwindows
        userhouseq.mainrinternal = mainrinternal
        userhouseq.fullrexternal = fullrexternal
        userhouseq.fullrroof=fullrroof
        userhouseq.mainrexternal = mainrexternal
        userhouseq.mainrwindows=mainrwindows
        userhouseq.mainrroof=mainrroof
        userhouseq.mainsize = mainsize
        userhouseq.fullsize = fullsize
        userhouseq.put()
        userhouse.put()
        self.redirect("/winanalysis")


class AnalysisHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse is not None:
            area = userhouse.area.split(" ")
            names = userhouse.names.split(" ")
            capacity = userhouse.capacity.split(" ")
            temps = userhouse.temps.split(" ")
            conductance = userhouse.conductance.split(" ")
            print area,"area"
            print capacity,"capacity"
            outtemps=outside_temps.temps.split(" ")
            outtemps = [[float(cell) for cell in row.split(",")] for row in outtemps]
            area = [[(float(cell)*2.4) for cell in row.split(",")] for row in area]
            capacity = [[(1/float(cell)) if float(cell) > 0.01 else (1/0.01) for cell in row.split(",")] for row in capacity]
            temps = [[float(cell) for cell in row.split(",")] for row in temps]
            conductance = [[float(cell) for cell in row.split(",")] for row in conductance]

            conductance = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(area, conductance)]
            print conductance
            simtemps = House(conductance, capacity).matrix_simulation(temps, 1, 60*60*24*31, outtemps)
            x1 = range(len(simtemps[0]))

            graph1 = StringIO.StringIO()
            try:
                plt.clf()
                for temps, name in zip(simtemps, names):
                    plt.plot(x1, temps, label=name)
                plt.legend()
                plt.title("The change in temperature")
                plt.xlabel("1/4 hours (900s)")
                plt.ylabel("Temperature (C)")
                plt.savefig(graph1, format="svg")
                plt.clf()
                self.response.write(html.analysis.format(graph1=graph1.getvalue()))
            except:
                self.response.write(html.analysisnograph.format(graph1=simtemps))
        else:
            self.redirect("/dataentry")

    def post(self):
        pass


class AnalysisNpHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse.area is not None:
            area = userhouse.area.split(" ")
            names = userhouse.names.split(" ")
            capacity = userhouse.capacity.split(" ")
            temps = userhouse.temps.split(" ")
            conductance = userhouse.conductance.split(" ")
            print area,"area"
            print capacity,"capacity"
            outtemps=outside_temps.temps.split(" ")
            outtemps = [[float(cell) for cell in row.split(",")] for row in outtemps]
            area = [[(float(cell)*2.4) for cell in row.split(",")] for row in area]
            capacity = [[(1/float(cell)) if float(cell) > 0.01 else (1/0.01) for cell in row.split(",")] for row in capacity]
            temps = [[float(cell) for cell in row.split(",")] for row in temps]
            conductance = [[float(cell) for cell in row.split(",")] for row in conductance]

            conductance = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(area, conductance)]
            print conductance
            simtemps = House(conductance, capacity).matrix_simulstionnp(temps, 1, 60*60*24*31, outtemps)
            x1 = range(len(simtemps[0]))

            graph1 = StringIO.StringIO()
            try:
                plt.clf()
                for temps, name in zip(simtemps, names):
                    plt.plot(x1, temps, label=name)
                plt.legend()
                plt.title("The change in temperature")
                plt.xlabel("1/4 hours (900s)")
                plt.ylabel("Temperature (C)")
                plt.savefig(graph1, format="svg")
                plt.clf()
                self.response.write(html.analysis.format(graph1=graph1.getvalue()))
            except:
                self.response.write(html.analysisnograph.format(graph1=simtemps))
        else:
            self.redirect("/dataentry")

    def post(self):
        pass


class AnalysisNpPowerHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse.area is not None:
            area = userhouse.area.split(" ")
            names = userhouse.names.split(" ")
            capacity = userhouse.capacity.split(" ")
            temps = userhouse.temps.split(" ")
            conductance = userhouse.conductance.split(" ")
            outtemps=outside_temps.temps.split(" ")
            outtemps = [[float(cell) for cell in row.split(",")] for row in outtemps]
            area = [[(float(cell)*2.4) for cell in row.split(",")] for row in area]
            capacity = [[(1/float(cell)) if float(cell) > 0.01 else (1/0.01) for cell in row.split(",")] for row in capacity]
            temps = [[float(cell) for cell in row.split(",")] for row in temps]
            conductance = [[float(cell) for cell in row.split(",")] for row in conductance]

            conductance = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(area, conductance)]
            print conductance
            simtemps = House(conductance, capacity).matrix_simulstionnppower(temps, 1, 60*60*24*31, outtemps)
            x1 = range(len(simtemps[0]))

            graph1 = StringIO.StringIO()
            try:
                plt.clf()
                for temps, name in zip(simtemps, names):
                    plt.plot(x1, temps, label=name)
                plt.legend()
                plt.title("The change in temperature")
                plt.xlabel("1/4 hours (900s)")
                plt.ylabel("Temperature (C)")
                plt.savefig(graph1, format="svg")
                plt.clf()
                self.response.write(html.analysis.format(graph1=graph1.getvalue()))
            except:
                self.response.write(html.analysisnograph.format(graph1=simtemps))
        else:
            self.redirect("/dataentry")

    def post(self):
        pass


class AnalysisNpPowerWinHandler(webapp2.RequestHandler):
    def get(self):
        savesim(self)
        user = users.get_current_user()
        nickname = user.nickname()

        housequery = DBHouse.query(DBHouse.username == nickname)
        userhouse = housequery.get()
        if userhouse.area is not None:
            area = userhouse.area.split(" ")
            names = userhouse.names.split(" ")
            capacity = userhouse.capacity.split(" ")
            temps = userhouse.temps.split(" ")
            conductance = userhouse.conductance.split(" ")
            winarea = userhouse.winarea.split(" ")
            winconductance = userhouse.winconductance.split(" ")
            rofarea = userhouse.rofarea.split(" ")
            rofconductance = userhouse.rofconductance.split(" ")
            outtemps=outside_temps.temps.split(" ")
            outtemps = [[float(cell) for cell in row.split(",")] for row in outtemps]
            area = [[(float(cell)*2.4) for cell in row.split(",")] for row in area]
            winarea = [[float(cell) for cell in row.split(",")] for row in winarea]
            winconductance = [[float(cell) for cell in row.split(",")] for row in winconductance]
            capacity = [[(1/float(cell)) if float(cell) > 0.01 else (1/0.01) for cell in row.split(",")] for row in capacity]
            temps = [[float(cell) for cell in row.split(",")] for row in temps]
            conductance = [[float(cell) for cell in row.split(",")] for row in conductance]
            rofarea = [[float(cell) for cell in row.split(",")] for row in rofarea]
            rofconductance = [[float(cell) for cell in row.split(",")] for row in rofconductance]

            print temps
            area = [[cella-cellwa for cella, cellwa in zip(rowa, rowwa)] for rowa, rowwa in zip(area, winarea)]
            winUA = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(winarea, winconductance)]
            walUA = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(area, conductance)]
            rofUA = [[cella*cellc for cella, cellc in zip(rowa, rowc)] for rowa, rowc in zip(rofarea, rofconductance)]
            UA = [[win+wal+rof for wal, win, rof in zip(walrow, winrow, rofrow)] for walrow, winrow, rofrow in zip(walUA, winUA, rofUA)]
            simtemps, kWh, money = House(UA, capacity).matrix_simulstionnppower(temps, 1, 60*60*24*30*12, outtemps)
            x1 = range(len(simtemps[0]))

            graph1 = StringIO.StringIO()
            try:
                plt.clf()
                for temps, name in zip(simtemps, names):
                    plt.plot(x1, temps, label=name)
                plt.legend()
                plt.title("The change in temperature")
                plt.xlabel("1/4 hours (900s)")
                plt.ylabel("Temperature (C)")
                plt.savefig(graph1, format="svg")
                plt.clf()
                self.response.write(html.analysis.format(graph1=graph1.getvalue(), kWh=kWh, room=names[0], money=money))
            except:
                self.response.write(html.analysis.format(graph1=simtemps, kWh=kWh, room=names[0], money=money))
        else:
            self.redirect("/quick")

    def post(self):
        pass


class TestHandler(webapp2.RequestHandler):
    def get(self):
        outtemps=outside_temps.temps.split(" ")
        outtemps = [[float(cell) for cell in row.split(",")] for row in outtemps]
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
        self.response.write("""<a href="/">Back to main page</a>""")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/house', HouseHandler),
    ('/info', InfoHandler),
    ('/sim', SimHandler),
    ('/edit', EditHandler),
    ('/dataentry', ManualEntryHandler),
    ('/quick', QuickEntryHandler),
    ('/winanalysis', AnalysisNpPowerWinHandler),
    ('/analysis', AnalysisHandler),
    ('/analysisnp', AnalysisNpHandler),
    ('/analysisnppower', AnalysisNpPowerHandler),
    ('/pages', PagesHandler),
    ('/test', TestHandler)
], debug=True)
