import pytest

from nurs_routines.tests.combiner_fixtures import *
from nurs_routines.utilities import Combiner


def test_combiner(combine):
    data = combine.main()
    n, k = data.shape
    assert n == 100
    assert k == 5


def test_init_fails():
    path = os.path.join("nurs_routines", "tests",
                        "test_data", "no_folder")

    with pytest.raises(FileNotFoundError):
        Combiner(path)


def test_path(combine):
    path = combine.path_content
    assert len(path) == 5
