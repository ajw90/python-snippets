#################################################################################
# A small project to assure myself that I have grasped how Python decorators work
#################################################################################

# Function-based decorator:
#
# x = decorator(x) : x is a function or class


def my_decorator_function (x):
    def decorated_x ():
    	print("Decorating {}.".format(x))
    	return x()
    return decorated_x


@my_decorator_function
def my_decorated_function ():
	print("Calling.")


@my_decorator_function
class My_Decorated_Class (object):
    def __init__ (self):
        print("{} created.".format(self))


# Test:
print("\nFunction-based decorator test:\n")
my_decorated_function()
My_Decorated_Class()


# Function-based decorator with arguments:
#
# inner_decorator = decorator(<arguments>)
# x = inner_decorator(x) : x is a function or class


def my_decorator_function_wa (*args, **kwargs):
    def inner_decorator (x):
        def decorated_x ():
            print("Decorating {}.".format(x))
            print(args)
            print(kwargs)
            return x()
        return decorated_x
    return inner_decorator


@my_decorator_function_wa(1, 2, 3, some_boolean=True, some_string="abc")  
def my_decorated_function2 ():
    print("Calling.")


@my_decorator_function_wa(1, 2, 3, some_boolean=True, some_string="abc")  
class My_Decorated_Class2 (object):
    def __init__ (self):
        print("{} created.".format(self))


# Test:
print("\nFunction-based decorator test with arguments:\n")
my_decorated_function2()
My_Decorated_Class2()

