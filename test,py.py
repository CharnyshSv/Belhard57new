import pytest

def multiply(a,b):
    return a*b

@pytest.mark.parametrize(
    'a,b,c', [
        (2,4,8),
        (3,5,15),
        (3,7,21),
        (12,8,96)
    ]
)

def test_myltiply(a,b,c):
    assert multiply(a, b) == c

