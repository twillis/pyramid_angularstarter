# Pyramid Angular Starter

This is a project scaffold for the [pyramid web
framework](http://www.pylonsproject.org/projects/pyramid/about) that
is setup for javascript development using
[angularjs](https://angularjs.org/) and other nice things.

Hopefully it will save you an hour or 2 when you are starting that
next awesome twitter clone.



## Project generation

This is a project scaffold so you use it in the normal pyramid way.


```bash

$ pcreate -l

Available scaffolds:
  alchemy:                 Pyramid SQLAlchemy project using url dispatch
  angularjs:               Pyramid + Angularjs
  pyramid_jinja2_starter:  pyramid jinja2 starter project
  starter:                 Pyramid starter project
  zodb:                    Pyramid ZODB project using traversal

```

Note the additional scaffold "angularjs", running pcreate with this
scaffold will generate a project skeleton with the following
"features".

* pyramid project setup with jinja2, sqlalchemy a javascript
* project under <project_name>/client-src setup with bower, gulp, coffeescript and sass
* a skeleton angularjs project + foundation css
* a supervisor config to run both pserve and gulp watch


Hopefully everything else is self explanatory. :)