import time


def timer(f, *argu, name=''):
    start = time.time()
    if argu != ():
        f(argu)
    else:
        f(name)
    end = time.time()
    print("the time of " + f.__name__ + str(argu) + ' : ' + str(end - start))


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")
