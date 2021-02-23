"""
Unit tests for ProgressBar class
"""
import pytest

from nurs_routines.utilities.progress_bar import ProgressBar


@pytest.fixture
def progress_bar():
    """ProgressBar Fixture"""
    # pb = ProgressBar(20, 10)
    # pb.max_steps
    return ProgressBar(20, 10)


def test_progress_bar_update(progress_bar):
    """Check update method performs as expected"""
    progress_bar.update(2, 10)


def test_progress_bar_update_fails(progress_bar):
    """Check error raises if setting progress above 100%"""
    with pytest.raises(ValueError):
        progress_bar.update(2, 120)


def test_progress_bar_steps(progress_bar):
    """Check progress bar can reach the max."""
    for _ in range(progress_bar.max_steps):
        progress_bar.step()


def test_progress_bar_exceed_max_steps(progress_bar):
    """Check for an error when too many steps are taken."""
    with pytest.raises(ValueError):
        for _ in range(11):
            progress_bar.step()
