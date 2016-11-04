#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Removes Tracis-CI file from project"""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_example_project(project_directory):
    """Removes the example Django project"""
    location = os.path.join(PROJECT_DIRECTORY, 'example')
    shutil.rmtree(location)


if __name__ == '__main__':
    if '{{ cookiecutter.create_example_project }}'.lower() != 'y':
        remove_example_project(PROJECT_DIRECTORY)
    if '{{ cookiecutter.use_travis }}'.lower() != 'y':
        remove_file('.travis.yml')
    if '{{ use_bumpversion }}'.lower() != 'y':
        remove_file('.bumpversion.cfg')
