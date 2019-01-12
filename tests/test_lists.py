import pytest
from exercises.lists import (
    make_ala_ma_kota, custom_range, reverse_list, flatten,
    only_odds, middle_n
)


def test_make_ala_ma_kota():
    assert make_ala_ma_kota() == ['ala', 'ma', 'kota']


@pytest.mark.parametrize('start, end, expected', (
    (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (5, 12, [5, 6, 7, 8, 9, 10, 11]),
    (1, 2, [1]),
    (1, 1, []),
    (5, 2, [])
))
def test_custom_range(start, end, expected):
    assert custom_range(start, end) == expected


@pytest.mark .parametrize('lista, expected', (
    ([1, 2, 3, 4], [1, 3]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([2, 2, 2, 2], []),
    ([1, 5, 3, 7, 2, 8, 5], [1, 5, 3, 7, 5]),
    ([], []),
))
def test_only_odds(lista, expected):
    assert only_odds(lista) == expected


@pytest.mark .parametrize('numbers, size, expected', (
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [5]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [3, 4, 5, 6, 7]),
    ([4, 5, 6, 7, 8, 9, 10, 11, 12], 5, [6, 7, 8, 9, 10]),
    ([5, 6, 7, 8, 9], 10000, [5, 6, 7, 8, 9]),
    ([], 1, []),
))
def test_middle_n(numbers, size, expected):
    assert middle_n(numbers, size) == expected



@pytest.mark .parametrize('lista, expected', (
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([1, [2, 3], 4, 5], [5, 4, [2, 3], 1]),
    ([], []),
))
def test_reverse_list(lista, expected):
    assert reverse_list(lista) == expected


@pytest.mark .parametrize('lista, expected', (
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, [2, 3], 4, 5], [1, 2, 3, 4, 5]),
    ([1, [2, 3], [4, 5]], [1, 2, 3, 4, 5]),
    ([[[[1]]], [2, 3], [4, 5]], [1, 2, 3, 4, 5]),
    ([], []),
))
def test_flatten(lista, expected):
    assert flatten(lista) == expected
