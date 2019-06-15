from unittest.mock import patch
from hypothesis import given, strategies
from app import foo


def test_foo_bar():
    assert foo.bar(1) == 2


def test_foo_baz():
    assert foo.baz() == 2


@patch("app.foo.bar")
def test_foo_baz_with_mock(mocked_bar):
    foo.baz()
    assert mocked_bar.called_once_with(1)


@given(strategies.integers())
def test_with_hypothesis(integer):
    assert foo.bar(integer) == integer + 1
