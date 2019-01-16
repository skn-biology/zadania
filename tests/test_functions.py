import pytest

from exercises.functions import (
    last_arg, to_dict
    )


@pytest.mark.parametrize('args, expected', (
    ((1,), 1),
    ((1, 2, 3), 3),
    ((3, 'a',), 'a'),
    ((3, 'a', 1), 1),
    ((3, 3, 3, 3), 3),
))
def test_last_arg(args, expected):
    assert last_arg(*args) == expected


@pytest.mark.parametrize('arg', (
    {},
    {'a': 1, 'b': 'b'},
    {'c': None},
))
def test_to_dict(arg):
    assert to_dict(**arg) == arg
