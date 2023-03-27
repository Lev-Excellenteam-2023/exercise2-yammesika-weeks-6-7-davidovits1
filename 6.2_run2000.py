import time


def timer(f, *args, **kwargs):
    """
    The function accepts a function and iterable runs the function on the Iterable
     and prints the time it took for the function
    :param f: function
    :param args: iterable
    :param kwargs: dictionary
    :return result: f returns
    """
    start = time.time()
    result = f(*args, **kwargs)
    end = time.time()
    print(f"the time of {f.__name__}{args}{kwargs}: {end - start}")
    return result


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")
