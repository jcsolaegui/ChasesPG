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
import webapp2
import os
import jinja2
from google.appengine.ext import db

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)

class MainHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template);
		self.write(t.render(params));

class MainPage(MainHandler):	
	def get(self):
		self.renderFront();

	def renderFront(self):		
		acts = db.GqlQuery("select * from Activity ORDER BY date desc")
		self.render("index.html", activities = acts)
		

	def post(self):
		requestActivity = self.request.get('activity');
		if (requestActivity):
			activity = Activity(activity = requestActivity)
			activity.put()

class Activity(db.Model):
	activity = db.TextProperty(required = True)
	date = db.DateTimeProperty(auto_now_add = True)

app = webapp2.WSGIApplication([
	('/', MainPage)
], debug=True)
