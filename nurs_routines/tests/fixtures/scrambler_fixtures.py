"""Fixtures for test_scrambler."""
import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def scrambling_data():
    """Data frame fixture for testing scrambler."""
    return pd.DataFrame(dict(
        ID=10*["A"] + 10*["B"],
        ID2=2*(5*["A"] + 5*["B"]),
        value=range(20)
    ))


@pytest.fixture
def scrambled_averages():
    """pandas.series fixture for summarizing scrambling_data fixture."""
    return pd.Series(
        {"A": np.mean(range(10)), "B": np.mean(range(10, 20))}
    )


@pytest.fixture
def scrambled_averages_id_id2():
    """pandas.series fixture for summarizing scrambling_data fixture"""
    return pd.Series(
        {("A", "A"): np.mean(range(5)), ("A", "B"): np.mean(range(5, 10)),
         ("B", "A"): np.mean(range(10, 15)), ("B", "B"): np.mean(range(15, 20))}
    )
