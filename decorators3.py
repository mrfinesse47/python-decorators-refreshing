# a decorator accepts a function as an argument.

def decorator_function(f):

    def wrapper_function():
        print('wrapper executed this before: ', f.__name__)
        return f()

    return wrapper_function


@decorator_function  # is: decorated_display = decorator_function(display)
def display():
    print("display function ran")


@decorator_function  # will not work due to wrong number of args -- see decorators4.py
def display_info(name, age):
    print(f'display info ran with 2 arguments {name} and {age}')


display_info("Kevin", 22)
