import logging
logging.basicConfig(level=logging.DEBUG)

import re
import sys

ALLOWED_DJANGO_VERSIONS = ['1.8', '1.9', '1.10', 'master']
APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

app_name = '{{ cookiecutter.app_name }}'
logger = logging.getLogger('pre_gen_project')

if not re.match(APP_REGEX, app_name):
    logger.error('Invalid app_name "{}"'.format(app_name))
    sys.exit(1)

for django_version in '{{ cookiecutter.django_versions }}'.split(","):
	if str(django_version).strip() not in ALLOWED_DJANGO_VERSIONS:
		logger.error('Invalid Django version "{}". '.format(django_version))
		sys.exit(1)
