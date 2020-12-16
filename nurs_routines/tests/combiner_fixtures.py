import os
import pytest

from nurs_routines.utilities import Combiner


@pytest.fixture
def combine_data_path():
    """
    Test fixture for data path.
    Returns
    -------
    str
    """
    return os.path.join(
        "nurs_routines", "tests",
        "test_data", "combine_data"
    )


@pytest.fixture
def combine(combine_data_path):
    """
    Test fixture Combiner class
    Parameters
    ----------
    combine_data_path: str
        path to files for combination.
    Returns
    -------
    Combiner
    """
    return Combiner(combine_data_path)
