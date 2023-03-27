def type_check(correct_type):
    """
    decorator function, checks if the variable is of the required type
    :param correct_type: required type of variable
    :return: fun with var or a message if the variable is not of the appropriate type
    """
    def decorator(fun):
        def inner(var):
            if correct_type == type(var):
                return fun(var)
            return "No access to the function"
        return inner
    return decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def times1(st):
    return st * 2


assert times2(2) == 4, "The result is not correct"
assert times2('2') == "No access to the function", "The result is not correct"
assert times1('2') == '22', "The result is not correct"
assert times1(2) == "No access to the function", "The result is not correct"


