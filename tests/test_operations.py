from src.math_operation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert sub(5,4) == 1
    assert sub(10,5) == 5
    assert sub(6,2) == 4
    assert sub(10,12) == -2
    assert sub(9,5) == -4