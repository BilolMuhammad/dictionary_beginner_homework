def count_jobs(data: list, job: str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    num = 0
    for n in range(len(data)):
        if data[n]['job'] == job:
            num += 1
    return num


job = 'Doctor'
users = [
    {
        'name': 'Ozoda',
        'job': 'Student'
    },
    {
        'name': 'Sevinch',
        'job': 'Doctor'
    },
    {
        'name': 'Madina',
        'job': 'Doctor'
    }
]
print(count_jobs(users, job))
