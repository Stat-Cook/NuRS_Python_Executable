"""
Unit tests for Combiner class.
"""
import os
import pytest

from nurs_routines.tests.fixtures.combiner_fixtures import combine, \
    combine_data_path  # pylint: disable=unused-import
from nurs_routines.utilities import Combiner


def test_combiner(combine):
    """
    Test - combiner makes correct shape data
    Parameters
    ----------
    combine: Combiner
    """
    data = combine.main()
    size, width = data.shape
    assert size == 100
    assert width == 5


def test_init_fails():
    """
    Test - assert Combiner fails if data folder doesnt exist.
    """
    path = os.path.join("nurs_routines", "tests",
                        "test_data", "no_folder")

    with pytest.raises(FileNotFoundError):
        Combiner(path)


def test_path(combine):
    """
    Test - assert combiner finds all files.
    Parameters
    ----------
    combine: Combiner
    """
    path = combine.path_content
    assert len(path) == 5
