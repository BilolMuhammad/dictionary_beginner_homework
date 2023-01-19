def get_user_names(data: list, country: str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    idx = []
    for n in range(len(data)):
        if data[n]['country'] == country:
            idx.append(n)
    names = []
    for i in idx:
        names.append(data[i]['name'])
    return names


country = 'Rus'
data = [
    {
        'name': 'Shamshod',
        'country': 'Rus'
    },
    {
        'name': 'dilshod',
        'country': 'France'
    },
    {
        'name': 'sardor',
        'country': 'UK'
    },
    {
        'name': 'Abu',
        'country': 'Rus'
    },
]
print(get_user_names(data, country))
