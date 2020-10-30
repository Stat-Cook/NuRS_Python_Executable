"""
General utility functions.
New implementations are inserted here during development phase.
"""
import logging
import numpy as np
import pandas as pd


def shuffle(frm, size_check, name=None):
    """
    Shuffle elements within a data set.
    With size_check=True, if there is not enough data to
        shuffle (<2 cases) a blank line is returned
    Parameters
    ----------
    frm: pandas.DataFrame
        the data set to shuffle
    size_check: bool
        Boolean flag - if true check there is enough data for shuffle to work
    name: str
        a name that represents the data set

    Returns
    -------
    pandas.DataFrame
    """
    n_cases, width = frm.shape
    if size_check:
        if n_cases < 1:
            logging.warning("Not enough data to shuffle %s", name)
            return pd.DataFrame([width * [None]], columns=[1, 2, 3])
    return frm.apply(lambda x: np.random.choice(x, frm.shape[0], replace=False))
