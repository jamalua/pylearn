from pytestTutorial import calculator

def test_add():
    calc = calculator()
    result = calc.add(2,3)
    assert result == 5    

def test_add_string():
    calc = calculator()
    result = calc.add('Hello',' World') 
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

def test_product():
    calc = calculator()
    assert calc.multiply(5,5) == 25
 
 





