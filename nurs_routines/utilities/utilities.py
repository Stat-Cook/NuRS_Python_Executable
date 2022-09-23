"""
General utility functions.
New implementations are inserted here during development phase.
"""
import os
import logging
import numpy as np
import pandas as pd


def shuffle(frm, name=None):
    """
    Shuffle elements within a data set.
    With size_check=True, if there is not enough data to
        shuffle (<2 cases) a blank line is returned
    Parameters
    ----------
    frm: pandas.DataFrame
        the data set to shuffle
    name: str
        a name that represents the data set

    Returns
    -------
    pandas.DataFrame
    """
    n_cases, width = frm.shape

    if n_cases < 2:
        logging.info("Not enough data to shuffle %s", name)
        return pd.DataFrame(columns=frm.columns, index=frm.index)

    return frm.apply(lambda x: np.random.choice(x, frm.shape[0], replace=False))


trust_data_path_join = lambda x: os.path.join("Trust_data", x)


def main_routine(instance):
    """
    Run the .main() method of the object given.
    Parameters
    ----------
    instance: object

    Returns
    -------
    Any
    """
    result = instance.main()
    if isinstance(result, pd.DataFrame):
        return result.reset_index(drop=True)
    return result
