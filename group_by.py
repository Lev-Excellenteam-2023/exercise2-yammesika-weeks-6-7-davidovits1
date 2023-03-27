def group_by(f, iterable):
    """
    get a function and an iterable and returns a dictionary whose keys are
     the activation of the function on each member and the values are the members
    :param f: function for key
    :param iterable: iterable
    :return: group dictionary by function
    """
    group_dictionary = {}
    for i in iterable:
        if f(i) in group_dictionary:
            group_dictionary[f(i)].append(i)
        else:
            group_dictionary[f(i)] = [i]

    return group_dictionary


assert group_by(len, ["hi", "bye", "yo", "try"]) == {2: ['hi', 'yo'], 3: ['bye', 'try']}, "Not the expected result"
assert group_by(len, ["", "", "", ""]) == {0: ['', '', '', '']}, "Not the expected result"
