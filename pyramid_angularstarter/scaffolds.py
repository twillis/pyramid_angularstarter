'''
the command that does the thing
'''

from pyramid.scaffolds import PyramidTemplate


class AngularProjectTemplate(PyramidTemplate):
    _template_dir = 'angularstarter'
    summary = 'Pyramid + Angularjs'


class AngularProjectTemplateWUser(PyramidTemplate):
    _template_dir = 'angularstarter_w_user_model'
    summary = 'Pyramid + Angularjs + User model, registration, forgot password'
