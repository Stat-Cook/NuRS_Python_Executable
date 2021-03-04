"""
Tools for scrambling demographics in data sets.
"""
from .utilities import shuffle
from .split_apply import split_apply, cached_split_apply


def scramble(data, aggregate_cols, scrambling_cols):
    """
    Scramble columns while data is aggregated
    Parameters
    ----------
    data: pandas.DataFrame
        the data set to aggregate and scramble
    aggregate_cols: List[str]
        the columns of 'data' to aggregate on
    scrambling_cols: List[str]
        the columns of 'data' to scramble
    Returns
    -------
    pandas.DataFrame
    """
    data = data.sort_values(aggregate_cols).reset_index(drop=True)

    shuffled_data = split_apply(
        data[set(scrambling_cols + aggregate_cols)],
        aggregate_cols,
        shuffle
    )
    shuffled_data = shuffled_data.reset_index(drop=True)

    data[shuffled_data.columns] = shuffled_data
    return data


def scramble_to_file(data, aggregate_cols, scrambling_cols, file):
    """
    Scramble columns while data is aggregated using file cache to concatenate
    Parameters
    ----------
    data: pandas.DataFrame
        the data set to aggregate and scramble
    aggregate_cols: List[str]
        the columns of 'data' to aggregate on
    scrambling_cols: List[str]
        the columns of 'data' to scramble
    file: str or IOStream
        the file to cache the data to
    Returns
    -------
    pandas.DataFrame
    """
    data = data.sort_values(aggregate_cols).reset_index(drop=True)

    shuffled_data = cached_split_apply(
        data[set(scrambling_cols + aggregate_cols)],
        aggregate_cols,
        shuffle,
        file
    )
    shuffled_data = shuffled_data.reset_index(drop=True)

    data[shuffled_data.columns] = shuffled_data
    return data
