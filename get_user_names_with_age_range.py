def get_user_names_with_age_range(data: list, min_age: int, max_age: int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    idx = []
    names = []
    for n in range(len(data)):
        if data[n]['age'] > min_age and data[n]['age'] < max_age:
            idx.append(n)
    for i in idx:
        names.append(data[i]['name'])
    return names


data = [
    {
        'name': 'Sardor',
        'age': 29
    },
    {
        'name': 'Sarvar',
        'age': 16
    },
    {
        'name': 'Jasur',
        'age': 19
    },
    {
        'name': 'Mavlon',
        'age': 33
    },
    {
        'name': 'Toyir',
        'age': 17
    }

]
min_age = 16
max_age = 30
print(get_user_names_with_age_range(data, min_age, max_age))
