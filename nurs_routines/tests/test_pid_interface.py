"""
Unit tests for pid_interface functions and classes.
"""

import pandas as pd
import pytest

from nurs_routines.pid_detector import PID_DEFAULT_REPORT


@pytest.fixture
def pid_frame():
    """PID Fixture"""
    return pd.DataFrame(dict(
        A=[1, 2, 3, 4],
        B=[5, 4, 5, 3],
        C=[1, 2, "Paul", "McCormick"]
    ))


def test_pid_default_report(pid_frame):
    """
    Check the default reporter can generate a report.
    """
    return PID_DEFAULT_REPORT(pid_frame)
