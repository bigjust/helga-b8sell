from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name="helga-b8sell",
    version=version,
    description=('basically b8sell'),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='irc bot b8sell',
    author='Justin Caratzas',
    author_email='bigjust@lambdaphil.es',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    installed_requires = (
        'helga_mimic',
    ),
    py_modules=['helga_b8sell'],
    zip_safe=True,
    entry_points = dict(
        helga_plugins = [
            'b8sell = helga_b8sell:b8sell',
        ],
    ),
)
