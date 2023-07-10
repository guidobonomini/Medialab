Medialab Test Workbench
================

Medialab Test Workbench
 - Guido Bonomini




[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Docker
================

To run the application, execute the following commands::

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up


Setting Up Your Admin account
================

To create an **superuser account**, use this command:

    $ docker-compose -f local.yml run --rm python manage.py createsuperuser


Type checks
================

Running type checks with mypy:

    $ docker-compose -f local.yml run --rm django mypy medialab


Test coverage
================

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage html
    $ open htmlcov/index.html

Running tests with py.test in docker

    $ docker-compose -f local.yml run --rm django pytest


To-do's:
================
- Fix CI tests to adapt to proyect