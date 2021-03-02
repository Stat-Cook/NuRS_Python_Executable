"""
Tools for applying a function to a divided data set.
"""
import os
import pandas as pd

from .io import merge_in_file
from .progress_bar import progress_bar_iter


def split_apply(frm, groupby, func, sort_index=False):
    """
    Divide a data set based on a column and apply a function to each chunk
    Parameters
    ----------
    frm: pandas.DataFrame
        data set to be grouped
    groupby: str or List[str]
        column to group on
    func: function
        function to apply to each chunk of data
    size_check: bool
        boolean flag - if True check each chunk has more than 1 case.
    sort_index: bool
        if True sort index before returning data

    Returns
    -------
    pandas.DataFrame
    """
    #grps = frm.groupby(groupby)
    groups = frm.set_index(groupby).groupby(lambda x: x)

    merged = pd.concat(progress_bar_iter(groups, func))

    if sort_index:
        return merged.sort_index()

    return merged


def cached_split_apply(frm, groupby, func, file):
    """
    Divide a data set based on a column and apply a function to each chunk.
    Recombine the data by caching to a temporary file.
    Parameters
    ----------
    frm: pandas.DataFrame
        data set to be grouped
    groupby: str or List[str]
        column to group on
    func: function
        function to apply to each chunk of data
    size_check: bool
        boolean flag - if True check each chunk has more than 1 case.
    file: str or IOStream
        the file to combine the data in.

    Returns
    -------
    pandas.DataFrame
    """
    # groups = frm.groupby(groupby)
    groups = frm.set_index(groupby).groupby(lambda x: x)

    if os.path.isfile(file):
        os.remove(file)

    _iter = progress_bar_iter(groups, func)
    with open(file, "a") as output_file:
        merge_in_file(output_file, _iter)

    result = pd.read_csv(file)
    os.remove(file)

    return result
