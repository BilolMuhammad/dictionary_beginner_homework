def get_user_names_with_age(data: list, age: int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    idx = 0
    for n in range(len(data)):
        if data[n]['age'] == age:
            idx = n
    return data[idx]['name']


age = 17
data = [
    {
        'name': 'Dilfuza',
        'age': 18
    },
    {
        'name': 'Madina',
        'age': 17
    }
]
print(get_user_names_with_age(data, age))
