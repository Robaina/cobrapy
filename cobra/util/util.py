# -*- coding: utf-8 -*-

from __future__ import absolute_import

from depinfo import print_dependencies
from six import string_types


def format_long_string(string, max_length=50):
    if len(string) > max_length:
        string = string[:max_length - 3]
        string += '...'
    return string


class AutoVivification(dict):
    """Implementation of perl's autovivification feature. Checkout
    http://stackoverflow.com/a/652284/280182 """

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def show_versions():
    """Print dependency information."""
    print_dependencies("cobra")


def is_not_sane(string):
    """Check if a string is sane to be used as an ID for cobra components."""
    return not isinstance(string, string_types) or \
        len(string) < 1 or string is ' '
