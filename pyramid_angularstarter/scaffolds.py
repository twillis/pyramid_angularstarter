'''
the command that does the thing
'''

from pyramid.scaffolds.template import Template


class AngularProjectTemplate(Template):
    _template_dir = 'angularstarter'
    summary = 'Pyramid + Angularjs'

    def pre(self, command, output_dir, vars):
        pass

    def post(self, command, output_dir, vars):
        pass

    def out(self, msg):
        print(msg)
