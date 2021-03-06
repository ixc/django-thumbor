# -*- coding: utf-8 -*-

from django.conf import settings

# The host serving the thumbor resized images
THUMBOR_SERVER = getattr(settings, 'THUMBOR_SERVER',
                         'http://localhost:8888').rstrip('/')

# The prefix for the host serving images with relative URLs.
# This must be a resolvable address to allow thumbor to reach the images.
THUMBOR_ROOT_URL = getattr(
    settings, 'THUMBOR_ROOT_URL', 'http://localhost:8000').rstrip('/')

# The same security key used in the thumbor service to
# match the URL construction
THUMBOR_SECURITY_KEY = getattr(settings, 'THUMBOR_SECURITY_KEY',
                               'MY_SECURE_KEY')

THUMBOR_ARGUMENTS = getattr(settings, 'THUMBOR_ARGUMENTS', {})

# An alias represents a named set of arguments which may be passed to
# the url generating function instead of the arguments. Allows re-use
# of thumbnail types across the app.
THUMBOR_ALIASES = getattr(settings, 'THUMBOR_ALIASES', {})

# Strip `http://` prefix for prettier URLs. Thumbor's HTTP loader will
# add these back in, but this will break HTTP loading via the
# `TC_AWS_ENABLE_HTTP_LOADER=True` setting for `thumbor-community/aws`.
THUMBOR_STRIP_HTTP = getattr(settings, 'THUMBOR_STRIP_HTTP', True)
