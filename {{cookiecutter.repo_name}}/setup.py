#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


exec(open('app_name/version.py').read())

tests_require = [
    'pytest==2.8.2',
    'pytest-pep8==1.0.6',
    'pytest-cov==2.2.0',
    'pytest-django==2.9.1'
]

setup(name='{{ cookiecutter.repo_name }}',
    version=__version__,
    description="""{{ cookiecutter.project_short_description }}""",,
    long_description="""""",
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    classifiers=[
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
    ],
    license='{{ cookiecutter.open_source_license }}',
    keywords='{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    setup_requires=[
        'pytest-runner==2.6.2',
    ],
    install_requires=[
        'Django>=1.6.0'
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require}
    )
