
MY_TEXT = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""


def count_words(text):
    """
    The function accepts text and returns a dictionary where the key is a word and the value is the length of the word.
    using generator expression to clean the text from signs that are not letters
    and using dictionary comprehension to generate the dictionary
    :param text: text
    :return: dictionary_text
    """
    generator_text = (char for char in text if char.isalpha() or char == " ")  # generator expression
    new_text = "".join((list(generator_text)))
    dictionary_text = {word: len(word) for word in new_text.split(' ') if word != ""}  # dictionary comprehension
    return dictionary_text


def main():
    print(count_words(MY_TEXT))


if __name__ == "__main__":
    # Call the main handler function
    main()
