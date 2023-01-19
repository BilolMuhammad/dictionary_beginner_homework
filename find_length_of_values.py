def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    sum = 0
    for v in data.values():
        sum += len(v)
    return sum


dic = {
    1: 'sdf',
    2: 'sdfsd',
    -2: '32'
}
print(find_length_of_values(dic))
