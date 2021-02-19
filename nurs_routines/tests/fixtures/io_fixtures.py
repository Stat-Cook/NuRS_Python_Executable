"""Fixtures for test_io"""
import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def test_data_path():
    """
    Test fixture of data path
    """
    return "nurs_routines/tests/test_data"


@pytest.fixture
def data_generator():
    """
    Test fixture to generate data samples.
    """
    def generate(i, n_cases, k):
        for _ in range(i):
            yield pd.DataFrame(
                np.random.normal(size=[n_cases, k])
            )
    return generate


@pytest.fixture
def to_file_frame():
    """
    Text fixture - small data set to save to frame.
    """
    return pd.DataFrame(dict(
        A=[1, 2, 3],
        B=[4, 5, 6,]
    ))
