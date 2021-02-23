"""Fixtures for test_split_apply.py"""
import pytest
import pandas as pd


@pytest.fixture
def split_apply_frm():
    """Data frame fixture for testing function application"""
    return pd.DataFrame(dict(
        ID=10*["A"] + 10*["B"],
        ID2=2*(5*["A"] + 5*["B"]),
        Value=range(20)
    ))


@pytest.fixture
def split_apply_increment_frm():
    """Data frame fixture for testing function application"""
    return pd.DataFrame(dict(
        ID=10*["A"] + 10*["B"],
        ID2=2*(5*["A"] + 5*["B"]),
        Value=range(1, 21)
    ))
