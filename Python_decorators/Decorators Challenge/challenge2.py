# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")#CALLS THE NAMES AND ARGS OF THE FUNCTION
        result = function(*args, **kwargs)
        print(f"The output of the function: {result}")
        return result
    return wrapper


# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)