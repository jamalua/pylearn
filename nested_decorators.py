def first_decorator(func):
    print(func.__name__)

    def first_wapper():
        print("*" * 10)
        func()
        print("*" * 10)

    return first_wapper


def second_decorator(func):
    print(func.__name__)

    def second_wrapper():
        print("%" * 10)
        func()
        print("%" * 10)

    return second_wrapper


@first_decorator
@second_decorator
def print_hello():
    print("hello")


print_hello()
