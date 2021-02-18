import pytest
import pandas as pd


@pytest.fixture
def frame_with_pid():
    return pd.DataFrame(
        columns=list("ABCDE") + ["First Name", "Last Name"],
        index=range(20)
    )

@pytest.fixture
def frame_with_dangerous_pid():
    return pd.DataFrame(
        columns=list("ABCDE") + ["first name", "Last Name"],
        index=range(20)
    )
