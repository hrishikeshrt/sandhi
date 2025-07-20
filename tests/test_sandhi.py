#!/usr/bin/env python

"""Tests for `sandhi` package."""


from sandhi import sandhi
from indic_transliteration.sanscript import DEVANAGARI

S = sandhi.Sandhi()


# Small test to check for proper handling of avagraha
def test_avagraha():
    """Sample pytest test function with the pytest fixture as an argument."""
    results = S.sandhi("ते", "अपि", DEVANAGARI)
    assert results[0][0] == "तेऽपि"
