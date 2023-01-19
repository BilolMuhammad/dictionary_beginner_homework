def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max = 0
    for k in data:
        if k > max:
            max = k
    return max


dic = {
    3.3: 'sdfsd',
    2.2222: 'sdfsd',
    11.111: '',
    -3: 'sdfds',
}
print(find_max_key(dic))
