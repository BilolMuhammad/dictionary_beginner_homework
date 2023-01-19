def get_min_age_user_name(data: list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    idx = 0
    min = data[0]['age']
    for n in range(1, len(data)):
        if data[n]['age'] < min:
            min = data[n]['age']
            idx = n
    return data[idx]['name']


data = [
    {
        'name': 'Ozoda',
        'age': 18
    },
    {
        'name': 'Madina',
        'age': 16
    },
    {
        'name': 'Dilfuza',
        'age': 17
    }
]
print(get_min_age_user_name(data))
