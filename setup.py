import sys
import os.path

from setuptools import setup, find_packages

import sqlacodegen


extra_requirements = ()
if sys.version_info < (2, 7):
    extra_requirements = ('argparse',)

here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
readme = open(readme_path).read()

setup(
    name='alengen',
    description='Automatic model code generator for SQLAlchemy',
    long_description=readme,
    version=sqlacodegen.version,
    author='Ashot Seropian',
    author_email='ashot.seropyan@gmail.com',
    url='https://github.com/massanchik/alengen',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Database',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ],
    keywords='sqlalchemy',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=(
        'SQLAlchemy >= 0.6.0'
    ) + extra_requirements,
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sqlacodegen=sqlacodegen.main:main'
        ]
    }
)
