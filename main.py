import os
import webapp2
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
print template_dir
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)