from setuptools import setup, find_packages

setup(
    name = "django-wiki",
    version = "1.1",
    url = 'http://github.com/tmitchell/django-wiki',
    license = 'BSD',
    description = "A super simple wiki for Django.",
    author = 'Taylor Mitchell',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)