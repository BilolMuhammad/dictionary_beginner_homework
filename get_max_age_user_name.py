def get_max_age_user_name(data: list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    max = data[0]['age']
    idx = 0
    for n in range(1, len(data)):
        if data[n]['age'] > max:
            max = data[n]['age']
            idx = n
    return data[idx]['name']


users = [
    {
        'name': 'Sarvinoz',
        'age': 16
    },
    {
        'name': 'Ozoda',
        'age': 18
    },
    {
        'name': 'Madina',
        'age': 17
    }
]
print(get_max_age_user_name(data=users))
