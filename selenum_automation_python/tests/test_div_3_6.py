import pytest

def test_divisible_by_3(input_data):
    print("\nusing data---->")
    assert input_data%3==0

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 33)])
def test_multiple_inputs(num, output):
    assert 11*num==output
