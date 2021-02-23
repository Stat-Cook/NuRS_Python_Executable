"""
Unit tests for functions in nurs_routines.utilities.utilities
"""
import pandas as pd
import pytest

from nurs_routines.utilities.utilities import shuffle


@pytest.fixture
def small_shuffling_frame():
    """Shuffling fixture - too small to shuffle"""
    return pd.DataFrame([[1, 2]])


@pytest.fixture
def shuffling_frame():
    """Shuffling fixture"""
    return pd.DataFrame(dict(
        A=range(20),
        B=range(20, 40)
    ))


def test_shuffle_fails(small_shuffling_frame):
    """Check shuffler doesn't shuffle small data sets if size_check False."""
    shuffled = shuffle(small_shuffling_frame, size_check=False)

    assert (shuffled == small_shuffling_frame).values.all()


def test_shuffle_logs_message(small_shuffling_frame, caplog):
    """Check shuffler raises message when shuffle small data sets if size_check True."""
    shuffle(small_shuffling_frame, True)
    assert caplog.records


def test_shuffle_logs_warning(small_shuffling_frame, caplog):
    """Check shuffler raises Warning when shuffle small data sets if size_check True."""
    shuffle(small_shuffling_frame, True)
    assert all(record.levelname == "WARNING" for record in caplog.records)


def test_shuffle_returns_nans(small_shuffling_frame):
    """Check shuffler returns nans when shuffling small data sets if size_check True."""
    frm = shuffle(small_shuffling_frame, True)
    assert frm.isna().values.all()


def test_shuffle_retains_averages(shuffling_frame):
    """Check shuffler doesn't change mean values"""
    frm = shuffle(shuffling_frame, True)
    assert (frm.mean() == shuffling_frame.mean()).values.all()


def test_shuffle_breaks_correlations(shuffling_frame):
    """Check shuffler does change covariances"""
    while True:
        frm = shuffle(shuffling_frame, True)
        if (frm != shuffling_frame).values.any():
            break

    assert (frm.corr() != shuffling_frame.corr()).values.any()
