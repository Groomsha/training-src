import pytest

from pyneng.pyneng_01_intro.task_05 import *

audit: list = [(2, "column"), (1, "test"), (0, "line")]


@pytest.mark.parametrize("value, result", audit)
def test_list_words(value, result):
    assert words[value] == result
