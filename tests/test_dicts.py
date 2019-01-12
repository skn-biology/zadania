import pytest

from exercises.dicts import (
    word_lengths, reverse_dict, remove_keys, zip_dict
)


@pytest.mark.parametrize('words, expected', (
    (['ala', 'ma', 'kota'], {'ala': 3, 'ma': 2, 'kota': 4}),
    (['1', '12', '123', '1234'], {'1': 1, '12': 2, '123': 3, '1234': 4})
))
def test_word_len(words, expected):
    assert word_lengths(words) == expected


@pytest.mark.parametrize('dic, expected', (
    ({"a": 1, "b": 2, "c": 3}, {1: "a", 2: "b", 3: "c"}),
    ({}, {}),
))
def test_reverse_dict(dic, expected):
    assert reverse_dict(dic) == expected


@pytest.mark.parametrize('dic, keys, expected', (
    ({"a": 1, "b": 2, "c": 3}, [], {"a": 1, "b": 2, "c": 3}),
    ({"a": 1, "b": 2, "c": 3}, ["asda", 1, 2, 3], {"a": 1, "b": 2, "c": 3}),
    ({"a": 1, "b": 2, "c": 3}, ["a"], {"b": 2, "c": 3}),
    ({"a": 1, "b": 2, "c": 3}, ["a", "b", "c", "d"], {}),
    ({}, [1, 2, 3], {}),
))
def test_remove_keys(dic, keys, expected):
    assert remove_keys(dic, keys) == expected


@pytest.mark.parametrize('keys, vals, expected', (
    ([1, 2, 3], ["a", "b", "c"], {1: "a", 2: "b", 3: "c"}),
    ("abc", "cde", {"a": "c", "b": "d", "c": "e"}),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["a", "b", "c"], {1: "a", 2: "b", 3: "c"}),
    ([1, 2, 3], ["a", "b", "c", 'd', 'e', 'f', 'g'], {1: "a", 2: "b", 3: "c"}),
    ([1, 2, 3], [], {}),
    ([], ["a", "b", "c"], {}),
))
def test_zip_dict(keys, vals, expected):
    assert zip_dict(keys, vals) == expected
