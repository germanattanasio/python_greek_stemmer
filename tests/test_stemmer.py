# -*- coding: utf-8 -*

from greek_stemmer_plus import GreekStemmer


try:
    from yaml import CLoader as Loader, load as load_yaml
except ImportError:
    from yaml import Loader, load as load_yaml


def test_stem_examples():
    gs = GreekStemmer()
    words = []
    with open("tests/fixtures/examples.yml", "r", encoding="utf-8") as f:
        words = load_yaml(f.read(), Loader=Loader)

    for word, st in words.items():
        assert gs.stem(word) == st


def test_stem_with_non_greek_letters():
    gs = GreekStemmer()
    assert gs.stem("englishΟΣ") == "englishΟΣ"


def test_stem_empty_input():
    gs = GreekStemmer()
    assert gs.stem("") == ""


def test_stem_with_numbers_symbols():
    gs = GreekStemmer()
    assert gs.stem("word123$") == "word123$"


def test_stem_long_word():
    gs = GreekStemmer()
    long_word = "a" * 1000 + "ΟΣ"
    assert gs.stem(long_word) == "a" * 1000 + "ΟΣ"
