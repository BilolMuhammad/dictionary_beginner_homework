def sum_age_values(data: list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    sum = 0
    for n in range(len(data)):
        sum += data[n]['age']
    return sum


data = [
    {
        'name': 'Madina',
        'age': 17
    },
    {
        'name': 'Sevinch',
        'age': 16
    }
]
print(sum_age_values(data))
