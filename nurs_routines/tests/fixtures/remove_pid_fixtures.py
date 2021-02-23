"""Fixtures for test_remove_pid"""
import pytest
import pandas as pd


@pytest.fixture
def frame_with_pid():
    """Data frame fixture with removable PID as columns."""
    return pd.DataFrame(
        columns=list("ABCDE") + ["First Name", "Last Name"],
        index=range(20)
    )


@pytest.fixture
def frame_with_dangerous_pid():
    """Data frame fixture with non-removable PID as column."""
    return pd.DataFrame(
        columns=list("ABCDE") + ["first name", "Last Name"],
        index=range(20)
    )
