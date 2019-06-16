"""
This is public app.

Yet another detail
"""


def bar(a: int) -> int:
    """
    Add one to the number.

    :param a:
    :return:
    >>> bar(1)
    2
    """
    return a + 1


def baz():
    """
    Add one to the number.

    >>> baz()
    2
    """
    return bar(1)
