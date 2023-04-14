# a decorator accepts a function as an argument.

def decorator_function(f):

    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before: ', f.__name__)
        return f(*args, **kwargs)

    return wrapper_function

# class decorator_class(object):


@decorator_function  # is: decorated_display = decorator_function(display)
def display():
    print("display function ran")


@decorator_function  # will not work due to wrong number of args
def display_info(name, age):
    print(f'display info ran with 2 arguments {name} and {age}')


display_info("Kevin", 22)

display()
