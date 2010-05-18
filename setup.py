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
    long_description = read('README'),

    author = 'John Sutherland, Taylor Mitchell',
    author_email = "taylor.mitchell@gmail.com",

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    package_data = {'': ['wiki/templates/wiki/*.html']},
    include_package_data = True,
    
    install_requires = ['setuptools'],

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