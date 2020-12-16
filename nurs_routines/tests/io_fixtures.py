import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def test_data_path():
    """
    Test fixture of data path
    Returns
    -------
    str
    """
    return "nurs_routines/tests/test_data"


@pytest.fixture
def data_generator():
    """
    Test fixture to generate data samples.
    Returns
    -------
    yield
    """
    def generate(i, n, k):
        for _ in range(i):
            yield pd.DataFrame(
                np.random.normal(size=[n, k])
            )
    return generate


@pytest.fixture
def to_file_frame():
    """
    Text fixture - small data set to save to frame.
    Returns
    -------
    pandas.DataFrame
    """
    return pd.DataFrame(dict(
        A=[1, 2, 3],
        B=[4, 5, 6,]
    ))
