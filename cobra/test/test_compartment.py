# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
from cobra.core import Metabolite, Model, Reaction, Compartment


def test__eq__():
    a = b = Compartment("x")
    c = "x"
    d = Compartment("x")
    e = Compartment ("z")
    assert a.__eq__(b) == True
    assert a.__eq__(c) == True
    assert a.__eq__(d) == True
    assert a.__eq__(e) == False


def test__ne__():
    a = b = Compartment("x")
    c = "x"
    d = Compartment("x")
    e = Compartment ("z")
    assert a.__ne__(b) == False
    assert a.__ne__(c) == False
    assert a.__ne__(d) == False
    assert a.__ne__(e) == True


def test_error_with_non_sane_id():
    with pytest.raises(TypeError):
        Compartment("Trust Me This ID Is Sane")