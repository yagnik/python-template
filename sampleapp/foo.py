"""
This is public app.

Yet another detail
"""
from sampleapp.metrics import METRICS

request_processing_seconds = METRICS["request_processing_seconds"]


def bar(a: int) -> int:
    """
    Add one to the number.

    :param a:
    :return:
    >>> bar(1)
    2
    """
    return a + 1


@request_processing_seconds()
def baz():
    """
    Add one to the number.

    >>> baz()
    2
    """
    return bar(1)
