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
  angularjs_w_user:        Pyramid + Angularjs + User model, registration, forgot password
  pyramid_jinja2_starter:  pyramid jinja2 starter project
  starter:                 Pyramid starter project
  zodb:                    Pyramid ZODB project using traversal
```

Note the additional scaffold "angularjs" and "angularjs_w_user", running pcreate with either of these
scaffolds will generate a project skeleton with the following
"features".

* pyramid project setup with jinja2, sqlalchemy, and a request local session attribute "db"
* a javascript project under <project_name>/client-src setup with bower, gulp, coffeescript and sass
* a skeleton angularjs project + foundation css

additionally, angular_js_w_user provides a user model and views for the following.

* login
* logout
* registration
* forgot password

database migrations via alembic are already configured with this template as well.

Hopefully everything else is self explanatory. :)
