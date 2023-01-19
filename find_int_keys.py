def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    list_key = []
    for k in data:
        if type(k) == int:
            list_key.append(k)
    return list_key


dic = {
    '1': 3121,
    2: 'sdf',
    '3': 23423,
    4: 344,
    5: 'sdf'
}
print(find_int_keys(dic))
