import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-wiki",
    version = "1.1dev",
    url = 'http://github.com/tmitchell/django-wiki',
    license = 'BSD',
    description = "A super simple wiki for Django.",
    long_description = read('README.rst'),

    author = 'John Sutherland, Taylor Mitchell',
    author_email = "taylor.mitchell@gmail.com",

    packages = find_packages(),
    package_data = {
        'wiki': [
            'wiki/templates/wiki/*.html',
            'wiki/media/*',
        ],
    },
#    include_package_data = True,
    
#    install_requires = ['setuptools','django','markdown'],

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