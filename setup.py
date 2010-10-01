import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-wiki",
    version = read('VERSION.txt'),
    url = 'http://github.com/tmitchell/django-wiki',
    license = 'BSD',
    description = "A super simple wiki for Django.",
    long_description = read('README.rst'),

    author = 'Taylor Mitchell',
    author_email = "taylor.mitchell@gmail.com",

    packages = find_packages(),
    package_data = {
        'wiki': [
            'wiki/templates/wiki/*.html',
            'wiki/media/*',
        ],
    },

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)