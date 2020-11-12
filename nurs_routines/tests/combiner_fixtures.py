import os
import pytest

from nurs_routines.utilities import Combiner


@pytest.fixture
def combine_data_path():
    return os.path.join(
        "nurs_routines", "tests",
        "test_data", "combine_data"
    )


@pytest.fixture
def combine(combine_data_path):
    return Combiner(combine_data_path)
