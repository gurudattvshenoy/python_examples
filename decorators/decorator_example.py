from functools import wraps
import time

class Decorator_Exec_Log:
    
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Started Executing {}".format(self.original_function.__name__))
        ret_val = self.original_function(*args, **kwargs)
        print("Completed Executing {}".format(self.original_function.__name__))
        return ret_val

def decorator_exec_log(original_function):
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        print("Started Executing {} function.".format(original_function.__name__))
        ret_val = original_function(*args, **kwargs)
        print("Completed Executing {} function.".format(original_function.__name__))
        return ret_val
    return wrapper

def decorator_exec_time(original_function):
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        ret_val = original_function(*args, **kwargs)
        end_time = time.time()
        print("{} function took {} time to execute.".format(original_function.__name__, end_time-start_time))
        return ret_val
    return wrapper

@decorator_exec_time
@decorator_exec_log
def greet_user(name):
    print("Hello,{}".format(name))

greet_user("guru")
print(greet_user.__name__)

