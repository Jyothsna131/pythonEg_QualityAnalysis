from app.calc import add,subtract,multiply, divide

def test_add():
    assert add(3,2)==5

def test_add_neg():
    assert add(-3,-6)==-9

def test_sub():
    assert subtract(5,3)==2

def test_mul():
    assert multiply(5,2)==10

def test_divide():
    assert divide(10,2)==5

def test_divide_by_zero():
    try:
        divide(5,0)
        assert False
    except ValueError as e:
        assert str(e)=="Cannot divide by zero"