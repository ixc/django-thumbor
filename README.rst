django-thumbor
==============

.. image:: https://travis-ci.org/ricobl/django-thumbor.png?branch=master
    :target: https://travis-ci.org/ricobl/django-thumbor
    :alt: CI status on Travis CI

.. image:: http://img.shields.io/pypi/v/django-thumbor.svg
    :target: https://pypi.python.org/pypi/django-thumbor/
    :alt: Latest django-thumbor PyPI version

.. image:: https://img.shields.io/pypi/dm/django-thumbor.svg
    :target: https://pypi.python.org/pypi/django-thumbor/
    :alt: Number of downloads for django-thumbor on PyPI

.. image:: https://coveralls.io/repos/ricobl/django-thumbor/badge.png?branch=master
    :target: https://coveralls.io/r/ricobl/django-thumbor?branch=master
    :alt: Code coverage on Coveralls

.. image:: https://gemnasium.com/ricobl/django-thumbor.svg
    :target: https://gemnasium.com/ricobl/django-thumbor
    :alt: Dependency Status on Gemnasium


A django application to resize images using the
`thumbor <https://github.com/globocom/thumbor>`_ service.

Usage
-----

Both ``thumbor_url`` templatetag and the ``generate_url`` helper uses the same
arguments as `libthumbor <https://github.com/heynemann/libthumbor>`_, you can
check the `wiki <https://github.com/heynemann/libthumbor/wiki>`_ for more info.

You can pass an absolute URL, protocol relative URL (which Thumbor will attempt
to load over HTTP), a path relative URL (beginning with `/`, which will be
prefixed with the value of `THUMBOR_ROOT_URL`), or a name to be used with the
default storage class.

On templates:

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url 'image.jpg' width=300 %}" width="300" />

    or

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' width=300 %}" width="300" />

    or

    {% load thumbor_tags %}
    <img src="{% thumbor_url '//example.com/media/image.jpg' width=300 %}" width="300" />

    or

    {% load thumbor_tags %}
    <img src="{% thumbor_url 'http://example.com/media/image.jpg' width=300 %}" width="300" />

    or

    {% load thumbor_tags %}
    <img src="{% thumbor_url model.image_field width=300 %}" width="300" />

If you need a thumbnail for a static file:

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% static_thumbor_url 'image.jpg' width=300 %}" width="300" />

    is equivalent to

    {% load staticfiles thumbor_tags %}
    <img src="{% static "image.jpg" as image_url %}{% thumbor_url image_url width=300 %}" width="300" />

If you need the result in a template variable, use `assign_thumbor_url` or
`assign_static_thumbor_url`, instead.

.. code-block:: html

    {% load thumbor_tags %}
    {% assign_thumbor_url '/media/image.jpg' width=300 as thumb_url %}
    <img src="{{ thumb_url }}" width="300" />

    or

    {% load thumbor_tags %}
    {% assign_static_thumbor_url 'image.jpg' width=300 as thumb_url %}
    <img src="{{ thumb_url }}" width="300" />


**Filters**

Split `filters <https://github.com/thumbor/thumbor/wiki/Filters>`_ with
``:`` (or use a ``list`` object):

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url url filters='watermark(http://domain.com/watermark.png,-10,-10,20):brightness(10)' %}" />
    <img src="{% thumbor_url url filters=filter_list %}" />

On code:

.. code-block:: python

    from django_thumbor import generate_url
    resized = generate_url("/media/image.jpg", width=300)


**Re-using argument sets (aliases)**

You can re-use argument sets through globally defined aliases. This prevents
repeating thumbnail parameters all over the code and can improve thumbor
performance because thumbnails are re-used as well. If you're migrating
from django-easy-thumbnails, you'll find the pattern very familiar, and it
should make porting much more straight-forward.

On templates:

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' alias="thumb-square" %}" />

On code:

.. code-block:: python

    from django_thumbor import generate_url
    resized = generate_url("/media/image.jpg", alias="thumb-square")

And in your ``settings.py``:

.. code-block:: python

    THUMBOR_ALIASES = {
        'thumb-square': {
            'width': 300,
            'height': 300,
            'filters': ['brightness(10)']}
    }


**Override server address**

There is an extra parameter to specify a custom server to be used instead of
``settings.THUMBOR_SERVER``.

On templates:

.. code-block:: html

    {% load thumbor_tags %}
    <img src="{% thumbor_url '/media/image.jpg' thumbor_server='http://localhost:8888/foo' width=300 %}" width="300" />

On code:

.. code-block:: python

    from django_thumbor import generate_url
    custom_server = "http://localhost:8888/foo"
    resized = generate_url(
        "/media/image.jpg", thumbor_server=custom_server, width=300)


Installation
------------

.. code-block:: bash

    pip install django-thumbor


Configuration
-------------

Add the app to the ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'django_thumbor',
    )

Here are the default settings that you can override:

.. code-block:: python

    # The host serving the thumbor resized images
    THUMBOR_SERVER = 'http://localhost:8888'

    # The prefix for the host serving images with relative URLs.
    # This must be a resolvable address to allow thumbor to reach the images.
    THUMBOR_ROOT_URL = getattr(
        settings, 'THUMBOR_ROOT_URL', 'http://localhost:8000').rstrip('/')

    # The same security key used in the thumbor service to
    # match the URL construction
    THUMBOR_SECURITY_KEY = 'MY_SECURE_KEY'

    # Default arguments passed to the `generate_url` helper or
    # the `thumbor_url` templatetag
    THUMBOR_ARGUMENTS = {}

    # An alias represents a named set of arguments to the generate_url function
    # or thumbor_url template tag. Use it to share general thumbnail
    # configurations without repeating yourself.
    THUMBOR_ALIASES = {}

    # Strip `http://` prefix for prettier URLs. Thumbor's HTTP loader will
    # add these back in, but this will break HTTP loading via the
    # `TC_AWS_ENABLE_HTTP_LOADER=True` setting for `thumbor-community/aws`.
    THUMBOR_STRIP_HTTP = True


Contributing
------------

Install
.......

Fork, clone, create a virtualenv and run:

.. code-block:: bash

    git clone git://github.com/ricobl/django-thumbor.git
    mkvirtualenv django-thumbor
    make install

Test
....

Add tests on ``testproject/tests``, add code and run:

.. code-block:: bash

    make test
