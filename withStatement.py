class WithStatementTestClass:
    def __init__(self):
        print("WithStatementTestClass created")
    
    def __enter__(self):
        print("__enter method called")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'traceback {traceback}')
    
    def __repr__(self):
        return 'This is the WithStatementTestClass object'
    
    def __str__(self):
        return "__str__ method is called on WithStatementTestClass class "

if __name__ == "__main__":
    with WithStatementTestClass() as obj:
        print(f'processing: {obj}')
        print(str(obj))
        print(repr(obj))
    
    print('Indentation block is left')
