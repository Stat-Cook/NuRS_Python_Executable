import pytest
import pandas as pd

@pytest.fixture
def shuffled():
    return pd.read_csv("integration_tests/test_data/shuffled.csv")

@pytest.fixture
def merged():
    return pd.read_csv("integration_tests/test_data/merged.csv")


def test_unshuffled_columns(shuffled, merged):
    merged_raw_corr = merged[["raw_value1", "raw_value2"]].corr().round(10)
    shuffled_raw_corr = shuffled[["raw_value1", "raw_value2"]].corr().round(10)
    assert (merged_raw_corr.values == shuffled_raw_corr.values).all()

def test_shuffled_columns(shuffled, merged):
    merged_corr = merged[["demographic1", "demographic2"]].corr().round(10)
    shuffled_corr = shuffled[["demographic1", "demographic2"]].corr().round(10)
    assert not (merged_corr.values == shuffled_corr.values).all()
