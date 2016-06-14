# cookiecutter-djangopackage

This is a cookiecutter template for Django packages, inspired by https://github.com/pydanny/cookiecutter-djangopackage and customized to my personal defaults and needs. It replaces my old Django package template "django-app-skeleton".

## Features

* Support for Django >= 1.7
* [Tox](https://tox.readthedocs.io/en/latest/) configuration
* [Pytest](http://pytest.org/latest/) for unit testing
* [Sphinx](http://www.sphinx-doc.org/en/stable/) documentation
* [Bumpversion](https://github.com/peritus/bumpversion) for updating version information
* (Optional) Travis-CI configuration

## Usage

Install cookiecutter:

    $ pip install cookiecutter

Initialize the package by using the cookiecutter template:

    $ cookiecutter https://github.com/hkage/cookiecutter-djangopackage.git
