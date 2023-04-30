
def group_by(func, iterable):
    """
    get a function and an iterable and returns a dictionary whose keys are
     the activation of the function on each member and the values are the members
    :param func: function for key
    :param iterable: iterable
    :return: group dictionary by function
    """
    group_dictionary = {}
    for item in iterable:
        if func(item) in group_dictionary:
            group_dictionary[func(item)].append(item)
        else:
            group_dictionary[func(item)] = [item]

    return group_dictionary


def main():
    assert group_by(len, ["hi", "bye", "yo", "try"]) == {2: ['hi', 'yo'], 3: ['bye', 'try']}, "Not the expected result"
    assert group_by(len, ["", "", "", ""]) == {0: ['', '', '', '']}, "Not the expected result"


if __name__ == "__main__":
    # Call the main handler function
    main()
