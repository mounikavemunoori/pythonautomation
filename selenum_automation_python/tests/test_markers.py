import pytest

class Test_Markers(object):
    @pytest.mark.great
    def test_greater(self):
        num=100
        assert num>100

    @pytest.mark.great
    def test_greater_equal(self):
        num=100
        assert num >= 100

    @pytest.mark.others
    def test_less(self):
        num=100
        assert num < 200

