def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    sum_even = 0
    for v in data.values():
        if v % 2 == 0:
            sum_even += v
    return sum_even


dic = {
    'a': 1,
    2: 4,
    3: 9,
    5: 11,
    'd': 12
}
print(sum_even_values(dic))
