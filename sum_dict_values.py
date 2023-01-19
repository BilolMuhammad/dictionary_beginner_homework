def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    sum = 0
    for v in data.values():
        sum += v
    return sum


dic = {
    'a': 2.2,
    'b': 3.3,
    'c': 4
}
print(sum_dict_values(dic))
