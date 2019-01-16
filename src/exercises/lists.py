"""List exercises.

Fill out the functions with your implementation, then
run `pylama src/exercises/lists.py` to run code checks
and `pytest tests/test_lists.py` to check your solutions.
"""


def make_ala_ma_kota():
    """Return a list with 3 elements - 'ala', 'ma' and 'kota'. """


def custom_range(start, end):
    """Return a list of numbers from start (inclusive) to end (exclusive).

    Examples:

        > custom_range(1, 5)
        [1, 2, 3, 4]
        > custom_range(3, 6)
        [3, 4, 5]
    """


def only_odds(numbers):
    """Go through the given `number` and remove only the odd ones.

    e.g.: only_odds([1, 2, 3, 3, 4, 4, 5]) == [1, 3, 5]
    """


def middle_n(numbers, size):
    """Return the `size` middle items of the given list.

    Assume that size is always odd and that there are always an odd
    number of numbers (it makes things easier).

    Examples:

        > middle_n([1, 2, 3, 4, 5, 6, 7], 1) == [4]
        > middle_n([1, 2, 3, 4, 5, 6, 7], 3) == [3, 4, 5]
        > middle_n([1, 2, 3], 100) == [1, 2, 3]

    Hints:
     * `len(numbers) / 2`
     * first work out where the slice should start from
    """


def reverse_list(lista):
    """Return the given list reversed.

    e.g. reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    """


def is_list(to_check):
    """Check whether the given thingy is a list.

    This is a helper function to make the next one a bit easier.

    :param to_check: The thing to check
    :return: whether `to_check` is a list (True or False)
    """
    return isinstance(to_check, list)


def flatten(lista):
    """Flatten the given list.

    e.g.: flatten([1, [[2, 3], [4, 5]], [[[[6]]]]]) == [1, 2, 3, 4, 5, 6]
    """
