# # this demonstrates closures in Python

# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)

#     inner_function()


# print(outer_function())

# this demonstrates a return of the inner function

def outer_function(msg):

    def inner_function():
        print(msg)

    return inner_function


msg = "hi"

# becomes the inner function waiting to be executed
hi_func = outer_function(msg)

print(hi_func())

msg = "bye"

bye_func = outer_function(msg)
