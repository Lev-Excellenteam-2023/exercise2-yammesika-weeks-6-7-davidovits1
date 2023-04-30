
import time


def timer(func, *args, **kwargs):
    """
    The function accepts a function and iterable runs the function on the Iterable
     and prints the time it took for the function
    :param func: function
    :param args: iterable
    :param kwargs: dictionary
    :return result: func returns
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"the time of {func.__name__}{args}{kwargs}: {end - start}")
    return result


def main():
    timer(print, "Hello")
    timer(zip, [1, 2, 3], [4, 5, 6])
    timer("Hi {name}".format, name="Bug")


if __name__ == "__main__":
    # Call the main handler function
    main()
