"""
Unit tests for remove_pid function
"""
import pytest

from nurs_routines.utilities.remove_pid import remove_pid
from nurs_routines.tests.fixtures.remove_pid_fixtures import frame_with_pid, \
    frame_with_dangerous_pid


def test_remove_pid(frame_with_pid):
    """Check defined PID columns are removed."""
    data = remove_pid(frame_with_pid)
    assert "First Name" not in data.columns


def test_remove_pid_fails(frame_with_dangerous_pid):
    """Check non-defined PID columns are ignored."""
    data = remove_pid(frame_with_dangerous_pid)
    with pytest.raises(AssertionError):
        assert "first name" not in data.columns
