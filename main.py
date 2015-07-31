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
import webapp2
from heat_simulation import *


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class TestHandler(webapp2.RequestHandler):
    def get(self):
        a = House([[0, 43.0], [43.0, 0]], [[1/120000], [1/200000]]).matrix_simulation([[200], [0]], 3)
        for i in range(len(a)):
            self.response.write("<p>Part {num}: {list} </p>".format(num=i, list=a[i]))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/test', TestHandler)
], debug=True)
