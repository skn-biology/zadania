"""Dictionary exercises.

Fill out the function definition, then 
run `pylama src/dicts.py` to run code checs 
and `pytest tests/test_dicts.py` to check your solutions.
"""


def word_lengths(words):
    """Return a dict containing each word of the given `words` with its length.

    Examples:

         word_lengths(['ala', 'ma', 'kota']) == {'ala': 3, 'ma': 2, 'kota': 4}
         word_lengths(['longer', 'phrases']) == {'longer': 6, 'phrases': 7}
    """


def reverse_dict(dic):
    """Reverse the given dict.

    Example:

         reverse_dict({"a": 1, "b": 2, "c": 3}) == {1: a", 2: "b", 3: "c"}
    """


def remove_keys(dic, keys):
    """Return a dict with the given keys removed.

    Example:

        remove_keys({"a": 1, "b", 3, "c": 3}, ["a", "c"]) == {"b": 3}
    """


def zip_dict(keys, values):
    """Make a dict from the given keys and values.

    The first key is the key of the first value. The second key is
    the key of the second value, etc. Keep matching them into pairs
    until at least one list has no more items.

    Examples:

        zip_dic([1, 2, 3], ["a", "b", "c]) == {1: "a", 2: "b", 3: "c"}

    Hints:
    * zip - https://docs.python.org/3.3/library/functions.html#zip
    """
