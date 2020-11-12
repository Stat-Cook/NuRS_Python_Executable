import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def test_data_path():
    return "nurs_routines/tests/test_data"


@pytest.fixture
def data_generator():
    def generate(i, n, k):
        for _ in range(i):
            yield pd.DataFrame(
                np.random.normal(size=[n, k])
            )
    return generate


@pytest.fixture
def to_file_frame():
    return pd.DataFrame(dict(
        A=[1, 2, 3],
        B=[4, 5, 6,]
    ))
