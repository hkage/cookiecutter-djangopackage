#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove a file from the project directory.

    :param str filepath: Path to the file to be deleted.
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(directory):
    """Remove an entire directory from the project.

    :param str directory: Path of the directory.
    """
    location = os.path.join(PROJECT_DIRECTORY, directory)
    shutil.rmtree(location)


if __name__ == '__main__':
    #if '{{ cookiecutter.create_example_project }}'.lower() != 'y':
    #    remove_directory('example')
    if '{{ cookiecutter.use_travis }}'.lower() != 'y':
        remove_file('.travis.yml')
    if '{{ cookiecutter.use_bumpversion }}'.lower() != 'y':
        remove_file('.bumpversion.cfg')
