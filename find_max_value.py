def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    max_val = 0
    for v in data.values():
        if v > max_val:
            max_val = v
    return max_val


dic = {
    'a': 2.4,
    'b': -1,
    'c': 3,
    'd': 2.5
}
print(find_max_value(dic))
