def get_num_of_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_num_of_each_char(text):
    """
    Counts the occurrences of each character in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_dict_by_value(d):
    """
    Sorts a dictionary by its values in descending order.

    Args:
        d (dict): The dictionary to sort.

    Returns:
        list: A list of tuples sorted by value in descending order.
    """
    new_list = []
    bla =sorted(d.items(), key=lambda item: item[1], reverse=True)
    for key, value in bla:
        if key.isalpha():
            new_list.append({"char":key, "num":value})
    return new_list
