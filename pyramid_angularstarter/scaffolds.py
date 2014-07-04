'''
the command that does the thing
'''

from pyramid.scaffolds import PyramidTemplate


class AngularProjectTemplate(PyramidTemplate):
    _template_dir = 'angularstarter'
    summary = 'Pyramid + Angularjs'
