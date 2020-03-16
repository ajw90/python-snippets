#################################################################################
# A small project to assure myself that I have grasped how Python decorators work
#################################################################################

# Function-based decorator:
#
# x = decorator_function(x) : x is a function or class


def my_decorator_function (x):
    def wrapper ():
    	print("Function-decorated {}.".format(x))
    	return x()
    return wrapper


@my_decorator_function
def my_decorated_function ():
	print("1 Called.")


@my_decorator_function
class My_Decorated_Class (object):
    def __init__ (self):
        print("{} created.".format(self))


# Test:
print("\n# Function-based decorator test:\n")
my_decorated_function()
My_Decorated_Class()


# Function-based decorator with arguments:
#
# temp = decorator_function(<arguments>)
# x = temp(x) : x is a function or class


def my_decorator_function_wa (*args, **kwargs):
    def inner_decorator (x):
        def wrapper ():
            print("Function-decorated {}.".format(x))
            print("Arguments passed:")
            print(args)
            print(kwargs)
            return x()
        return wrapper
    return inner_decorator


@my_decorator_function_wa(1, 2, 3, some_boolean=True, some_string="abc")  
def my_decorated_function2 ():
    print("2 Called.")


@my_decorator_function_wa(1, 2, 3, some_boolean=True, some_string="abc")  
class My_Decorated_Class2 (object):
    def __init__ (self):
        print("{} created.".format(self))


# Test:
print("\n# Function-based decorator test with arguments:\n")
my_decorated_function2()
My_Decorated_Class2()


# Class-based decorator: 
#
# x = Decorator_Class(x) : x is a function or class


class My_Decorator_Class (object):
    def __init__ (self, x):
        self.x = x

    def __call__ (self):
        print("Class-decorated {}.".format(self.x))
        return self.x()


@My_Decorator_Class
def my_decorated_function3 ():
    print("3 Called.")


@My_Decorator_Class
class My_Decorated_Class3 (object):
    def __init__ (self):
        print("{} created.".format(self))    


# Test    
print("\n# Class-based decorator test:\n")
my_decorated_function3()
My_Decorated_Class3()


# Class based decorator with arguments:
#
# temp = Decorator_Class(<arguments>)
# x = temp(x) : x is a function or class


class My_Decorator_Class_WA (object):
    def __init__ (self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__ (self, x):
        def wrapper ():
            print("Class-decorated {}.".format(x))
            print("Arguments passed:")
            print(self.args)
            print(self.kwargs)
            return x()
        return wrapper


@My_Decorator_Class_WA(1, 2, 3, some_boolean=True, some_string="abc")
def my_decorated_function4 ():
    print("4 Called.")


@My_Decorator_Class_WA(1, 2, 3, some_boolean=True, some_string="abc")
class My_Decorated_Class4 (object):
    def __init__ (self):
        print("{} created.".format(self))  


# Test    
print("\n# Class-based decorator test with arguments:\n")
my_decorated_function4()
My_Decorated_Class4()        