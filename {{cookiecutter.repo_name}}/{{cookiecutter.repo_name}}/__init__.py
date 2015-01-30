# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__date__ = '{{ cookiecutter.release_date }}'
__email__ = '{{ cookiecutter.email }}'
__license__ = "LGPL v3"
__maintainer__ = "{{ cookiecutter.full_name }}"

VERSION = '{{ cookiecutter.version }}'
VERSION_NUMBER_PARTS = ()
VERSION_STATUS = ''

_items = VERSION.split('-')                                           
VERSION_NUMBER_PARTS = tuple(int(i) for i in _items[0].split('.'))
if len(_items) > 1:
	VERSION_STATUS = _items[1]
__version__ = VERSION
