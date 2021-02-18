import pytest


from nurs_routines.utilities.progress_bar import ProgressBar

@pytest.fixture
def progress_bar():
    return ProgressBar(20, 10)

def test_progress_bar_update(progress_bar):
    progress_bar.update(2, 10)

def test_progress_bar_update_fails(progress_bar):
    with pytest.raises(ValueError):
        progress_bar.update(2, 120)

def test_progress_bar_steps(progress_bar):
    for _ in range(10):
        progress_bar.step()

def test_progress_bar_exceed_max_steps(progress_bar):
    with pytest.raises(ValueError):
        for _ in range(11):
            progress_bar.step()
