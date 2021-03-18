"""
Removal of personally identifiable data (PID) columns
from data sets.
"""
import logging

def remove_pid(data, extra_remove=None):
    """
    Remove any columns marked as identifiable data from a data set
    Parameters
    ----------
    data: pandas.DataFrame
        the data set to remove PID columns from
    extra_remove: list
        a list of columns to add on top the default.
        Repetition of the hard coded removal is ignored
    Returns
    -------
    pandas.DataFrame
    """
    default_remove = [
        'Title', 'First Name', 'Middle Name', 'Last Name', 'Person',
        'Home Phone', 'Mobile Phone', "Supervisor",
        'NI Number', 'Assignment Number', 'Employee Number', 'Staff Number',
        'Personal Email Address', 'Email Address',
        'Address Line 1', 'Address Line 2', 'Address Line 3',
        'Town or City', 'County', 'Postal Code', "Census Entered By"
    ]

    extra_remove = extra_remove or []

    to_remove = set(default_remove + extra_remove)
    to_remove = [i for i in to_remove if i in data.columns]

    for col in to_remove:
        logging.info("Removing '%s' from data.", col)

    return data.drop(columns=to_remove)
