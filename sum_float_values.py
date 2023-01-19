def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    sum_float = 0
    for v in data.values():
        if type(v) == float:
            sum_float += v
    return sum_float


dic = {
    1.1: 2,
    3: 4.4,
    1.7: 3,
    2.9: 4,
    7: 6.6,
    3.3: 1.1
}
print(sum_float_values(dic))
