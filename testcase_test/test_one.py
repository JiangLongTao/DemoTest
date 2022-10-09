import pytest


@pytest.mark.pro
class TestThree:
    def test_one(self):
        fergus = 1
        tom = 1
        assert fergus == tom

    def test_two(self):
        fergus = 1
        tom = 3
        assert fergus == tom
