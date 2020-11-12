import pytest
from nurs_routines.utilities.grouped_frame import GroupedFrame

def test_grouped_frame_init():
    groups = GroupedFrame("nurs_routines/tests/test_data/grouping_data.csv", "A")
    assert len(groups.columns) == 2
