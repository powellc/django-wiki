import os
from setuptools import setup, find_packages

#from finddata import find_package_data

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
    #package_data = find_package_data(),

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
