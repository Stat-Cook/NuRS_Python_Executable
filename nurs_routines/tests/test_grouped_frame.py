"""
Unit tests for GroupedFrame
"""
from nurs_routines.utilities.grouped_frame import GroupedFrame

def test_grouped_frame_init():
    """
    Check GroupedFrame can be initialized as expected.
    """
    groups = GroupedFrame("nurs_routines/tests/test_data/grouping_data.csv", "A")
    assert len(groups.columns) == 2
