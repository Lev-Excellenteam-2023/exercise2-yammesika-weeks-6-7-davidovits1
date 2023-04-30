def type_check(correct_type):
    """
    decorator function, checks if the variable is of the required type
    :param correct_type: required type of variable
    :return: fun with var or a message if the variable is not of the appropriate type
    """
    def decorator(func):
        def inner(var):
            if correct_type == type(var):
                return func(var)
            return "No access to the function"
        return inner
    return decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def times1(string):
    return string * 2


def main():
    assert times2(2) == 4, "The result is not correct"
    assert times2('2') == "No access to the function", "The result is not correct"
    assert times1('2') == '22', "The result is not correct"
    assert times1(2) == "No access to the function", "The result is not correct"


if __name__ == "__main__":
    # Call the main handler function
    main()
