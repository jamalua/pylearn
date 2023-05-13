'''
def mapper(fnc):
    def inner(listof_values):
        return [fnc(value) for value in listof_values]
    return inner

@mapper
def camelcase(s):
    return ''.join([word.capitalize() for word in s.split('_')])


names = ['hello_how_are_you','I_a_fine','nice_to_see_you']
print(camelcase(names))



def f1(func):
    def wrapper(*args):
        print('Started')
        func(*args)
        print('Ended')
    return wrapper

@f1
def f(a, b=9):
    print(a,b)

f('Hi! ')



import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print(f"Function took: {time.time() - before} seconds")
    return wrapper

@timer
def run():
    time.sleep(2)

run()


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}> {msg} </{tag}>')
    return wrap_text

print_hi = html_tag('h1')
print_hi('Test Headline!')
print_hi('Another Headline')

'''
'''
def f1(func):
    def wrapper(a):
        print("Started")
        func()
        print(a)
        print("Ended")
    return wrapper

def f():
    print('Hello')

#f1(f)()

#Having a decorator is actually having these two comaands
f = f1(f)
#Now calling f() in essence will call the wrapper function
f('Wrapper Value')

'''

# def outer_function():
#     m = 'Hi'

#     def inner_function():
#         print(m)
#     return inner_function

# outer_function()()

class decorator_class:

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f"call methid executed this before {self.original_function.__name__}")
        funcRun =  self.original_function(*args, **kwargs)
        return funcRun
    

@decorator_class
def display():
    print('Display function ran')

@decorator_class
def display_info(name,age):
    print(f'display_info ran with arguments ({name}, {age})')

display()
display_info('John',25)
