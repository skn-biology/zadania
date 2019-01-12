import pytest

from exercises.dicts import word_lengths


@pytest.mark.parametrize('words, expected', (
    (['ala', 'ma', 'kota'], {'ala': 3, 'ma': 2, 'kota': 4}),
    (['1', '12', '123', '1234'], {'1': 1, '12': 2, '123': 3, '1234': 4})
))
def test_word_len(words, expected):
    assert word_lengths(words) == expected
