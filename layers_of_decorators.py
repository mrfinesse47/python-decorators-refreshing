# a decorator accepts a function as an argument.

# class decorator_class(object):

class decorator_class(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('__call__ method executed this before: ', self.f.__name__)
        return self.f(*args, **kwargs)


def decorator_function(f):

    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before: ', f.__name__)
        return f(*args, **kwargs)

    # here we can call a decorator class
    return decorator_class(wrapper_function)


@decorator_function  # is: decorated_display = decorator_function(display)
def display():
    print("display function ran")


@decorator_function  # will not work due to wrong number of args
def display_info(name, age):
    print(f'display info ran with 2 arguments {name} and {age}')


display_info("Kevin", 22)
