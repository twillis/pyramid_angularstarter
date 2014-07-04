'''
scaffold for new fancy single page application using pyramid+sqlalchemy+angular
'''
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = ['pyramid']

setup(name='pyramid_angularstarter',
      version='0.0',
      description='pyramid_angularstarter',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Tom Willis',
      author_email='tom.willis@gmail.com',
      url='https://github.com/twillis/pyramid_angularstarter',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [pyramid.scaffold]
      angularjs=pyramid_angularstarter.scaffolds:AngularProjectTemplate
      """,
      )
