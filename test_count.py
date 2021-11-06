import count 

def test_count_zeros():
    assert count.count([0,0,0], 0) == 2

def test_count_string():
    assert count.count(["a", "a", "a"], "a") == 3


x = ''
print(x.vars())