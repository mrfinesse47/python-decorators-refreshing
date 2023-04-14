# a decorator accepts a function as an argument.

def decorator_function(f):

    def wrapper_function():
        print('wrapper executed this before: ', f.__name__)
        return f()

    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)

decorated_display()

# is the same as:


@decorator_function  # is: decorated_display = decorator_function(display)
def display():
    print("display function ran")


display()
