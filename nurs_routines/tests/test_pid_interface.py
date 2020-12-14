import pandas as pd

from nurs_routines.pid_detector import PID_DEFAULT_REPORT

import pytest


@pytest.fixture
def pid_frame():
    return pd.DataFrame(dict(
        A = [1,2,3,4],
        B = [5,4,5,3],
        C= [1,2, "Paul", "McCormick"]
    ))


def test_pid_default_report(pid_frame):

    return PID_DEFAULT_REPORT(pid_frame)
