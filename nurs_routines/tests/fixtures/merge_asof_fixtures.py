import pytest
import pandas as pd
import numpy as np

from nurs_routines.utilities.merge_asof import MergeAsOf


users = "ABCD"


@pytest.fixture
def test_data():
    return pd.DataFrame({
        'user': np.concatenate([3 * list(user) for user in users]),
        'date': 4 * ["2000-01-01", "2017-01-01", "2020-01-01"],
        "extra": 1
    })


@pytest.fixture
def test_data_extra_bodies():
    return pd.DataFrame({
        'user': np.concatenate([3*list(user) for user in users + "12"]),
        'date': 6*["2000-01-01", "2017-01-01", "2020-01-01"]
    })


@pytest.fixture
def test_reference():
    dates = ['2015-01-16', '2015-02-05',
             '2015-05-19', '2016-06-14', '2018-02-25']
    return pd.DataFrame(
        {'user': np.concatenate([5 * list(user) for user in users]),
         'date': 4 * dates, 'value': 4 * list(range(5)),
         "value2": range(20), "extra": 2}
    )


@pytest.fixture
def merge_object(test_data, test_reference):
    return MergeAsOf(
        test_data,
        test_reference,
        "user", "user")


@pytest.fixture
def merged_data(merge_object):
    return merge_object.main("date", "date")


@pytest.fixture
def merged_object_extra_bodies(test_data_extra_bodies, test_reference):
    return MergeAsOf(
        test_data_extra_bodies,
        test_reference,
        "user", "user")


@pytest.fixture
def merged_data_extra_bodies(merged_object_extra_bodies):
    return merged_object_extra_bodies.main("date", "date")
