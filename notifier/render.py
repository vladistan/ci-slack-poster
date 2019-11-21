import os
from jinja2 import Environment


class Renderer(object):

    def __init__(self):
        self.env = Environment(autoescape=True)
        self.vars = {}

    def set_vars(self, vars):
        self.vars = vars

    def render(self, inp):
        t = self.env.from_string(inp)
        return t.render(self.vars)

    def parse_file(self, path):
        with open(path, 'r') as tmpl:
            text = tmpl.read()
            t = self.env.from_string(text)
            return t.render(self.vars)

    def use_os_env(self):
        self.vars = os.environ
