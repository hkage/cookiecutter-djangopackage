#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


exec(open('app_name/version.py').read())

classifiers = """
'Development Status :: 3 - Alpha',
'Framework :: Django',{% if '1.7' in cookiecutter.django_versions %}
'Framework :: Django :: 1.7',{% endif %}{% if '1.8' in cookiecutter.django_versions %}
'Framework :: Django :: 1.8',{% endif %}{% if '1.9' in cookiecutter.django_versions %}
'Framework :: Django :: 1.9',{% endif %}{% if '1.10' in cookiecutter.django_versions %}
'Framework :: Django :: 1.10',{% endif %}
'Intended Audience :: Developers',
'License :: OSI Approved :: BSD License',
'Natural Language :: English',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',{% if '1.7' in cookiecutter.django_versions or '1.8' in cookiecutter.django_versions %}
'Programming Language :: Python :: 3.2',
'Programming Language :: Python :: 3.3',{% endif %}
'Programming Language :: Python :: 3.4',{% if '1.7' != cookiecutter.django_versions %}
'Programming Language :: Python :: 3.5',{% endif %}
"""

tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    'pytest-django',
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest',
]

install_requires = [
    # 'six',
]

setup(name='{{ cookiecutter.repo_name }}',
      version=__version__,  # noqa
      description="""{{ cookiecutter.project_short_description }}""",
      long_description="""TODO:""",
      author='{{ cookiecutter.author_name }}',
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
      classifiers=[c.strip() for c in classifiers.splitlines()
                   if c.strip() and not c.startswith('#')],
      license='{{ cookiecutter.open_source_license }}',
      keywords='{{ cookiecutter.repo_name }}',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      test_suite='tests',
      setup_requires=[
          'pytest-runner',
          ],
      install_requires=install_requires,
      tests_require=tests_require,
      )
