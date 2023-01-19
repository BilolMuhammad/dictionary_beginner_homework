def count_users_with_age(data: list, age: int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    sum_age = 0
    for n in range(len(data)):
        if data[n]['age'] == age:
            sum_age += 1
    return sum_age


age = 17
users = [
    {
        'name': 'Madina',
        'age': 17
    },
    {
        'name': 'Ozoda',
        'age': 18
    },
    {
        'name': 'Sevinch',
        'age': 17
    }
]
print(count_users_with_age(users, age))
