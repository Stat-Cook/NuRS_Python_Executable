import pytest

from nurs_routines.utilities.script_factories.script_functions import ScriptFunctionFactory
from nurs_routines.tests.fixtures.scrambler_fixtures import scrambling_data, \
    scrambled_averages, scrambled_averages_id_id2, mixed_size_scramble_data, \
    mixed_size_scramble_data2
from nurs_routines.tests.fixtures.split_apply_fixtures import split_apply_frm

@pytest.fixture
def sff():
    return ScriptFunctionFactory()

def test_sff_scramble_merge_as_of(sff, mixed_size_scramble_data):
    data = [mixed_size_scramble_data, ["B"]]
    scrambled = sff.scramble_merge_as_of(data, ["A"], "temp")
    assert scrambled.shape[0] == mixed_size_scramble_data.shape[0]
