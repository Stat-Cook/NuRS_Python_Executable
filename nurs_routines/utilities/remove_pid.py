def remove_pid(data, extra_remove=None):
    default_remove = [
        'Title', 'First Name', 'Middle Name', 'Last Name', 'Person',
        'Home Phone', 'Mobile Phone',
        'NI Number', 'Assignment Number', 'Employee Number', 'Staff Number',
        'Personal Email Address', 'Email Address',
        'Address Line 1', 'Address Line 2', 'Address Line 3', 'Town or City', 'County', 'Postal Code',
    ]

    extra_remove = extra_remove or []

    to_remove = set(default_remove + extra_remove)
    to_remove = [i for i in to_remove if i in data.columns]

    return data.drop(columns=to_remove)
