# Conversion from Markdown to pypi's restructured text: https://coderwall.com/p/qawuyq -- Thanks James.

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''
    print 'warning: pandoc or pypandoc does not seem to be installed; using empty long_description'

import importlib
from pip.req import parse_requirements
from setuptools import setup

install_requires = parse_requirements('requirements.txt', session=False)
install_requires = [str(ir.req) for ir in install_requires]

setup(
    name='py_windows_exe',
    version=importlib.import_module('py_windows_exe').__version__,
    author='Body Labs',
    author_email='alex@bodylabs.com',
    description='Functions needed when running a Python program as a Windows exe',
    long_description=long_description,
    url='https://github.com/bodylabs/py_windows_exe',
    license='MIT',
    packages=[
        'py_windows_exe'
    ],
    install_requires=install_requires,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
