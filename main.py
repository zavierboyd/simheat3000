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
    import webapp2
    import matplotlib.pyplot as plt
except:
    pass

import StringIO
from heat_simulation import *


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Testing deployment!')


class TestHandler(webapp2.RequestHandler):
    def get(self):
        y = House([[0, 269.2656], [269.2656, 0]], [[1/278666.667], [1/45600.0]]).matrix_simulation([[17.0], [20.0]], 1)
        x = range(len(y[0]))
        self.response.write("""This shows a simulation of heat flow between the surrounding walls and the air inside.<br>
        The numbers shown below are the temperatures over each second for the walls and the air.<br>
        Part 0 shows the temperatures of the walls, Part 1 shows the temperatures of the air.<br>
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
        for i in range(len(y)):
            self.response.write("<p>Part {num}: {list} </p>".format(num=i, list=y[i]))

        image = StringIO.StringIO()
        try:
            plt.clf()
            walls = plt.plot(x, y[0], label="walls")
            air = plt.plot(x, y[1], label="air")
            plt.legend()
            plt.title("The change in temperature")
            plt.xlabel("Seconds (s)")
            plt.ylabel("Temperature (C)")
            plt.savefig(image, format="svg")
        except:
            pass
        self.response.write(image.getvalue())

def test():
    y = House([[0, 269.2656], [269.2656, 0]], [[1/278666.667], [1/45600.0]]).matrix_simulation([[17.0], [20.0]], 1)
    x = range(len(y[0]))

    image = StringIO.StringIO()
    try:
        walls = plt.plot(x, y[0], label="walls")
        air = plt.plot(x, y[1], label="air")
        plt.legend()
        plt.savefig(image, format="svg")
    except:
        pass

test()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/test', TestHandler)
], debug=True)
# look how fast he's running
# look at fast the thermal energy is moving
# thermal energy = temp * thermal capacity