def get_user_country(data: list, name: str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    for n in range(len(data)):
        if data[n]['name'] == name:
            return data[n]['country']


name = 'Shamshod'
data = [
    {
        'name': 'Bobobek',
        'country': 'USA'
    },
    {
        'name': 'Shamshod',
        'country': 'Russia'
    },
    {
        'name': 'Nortoy',
        'country': 'UK'
    }
]
print(get_user_country(data, name))
