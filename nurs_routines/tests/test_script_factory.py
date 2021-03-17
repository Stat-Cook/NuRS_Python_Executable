import pytest

from nurs_routines.utilities.script_factories.script_factory import ScriptFactory
from nurs_routines.tests.fixtures.scrambler_fixtures import mixed_size_scramble_data


@pytest.fixture
def factory():
    return ScriptFactory("/", "Test_factory", {})


def test_factory_scramble_merge_as_of(factory, mixed_size_scramble_data):

    tasks = {
        "Inject data": dict(
            data=[mixed_size_scramble_data, ["B", "C"]]
        ),
        "Scramble as of": dict(
            aggregate_columns=["A"],
            file_path="mixed_size_scramble_data.csv"
        )
    }
    sff = ScriptFactory("", "Test_factory", tasks)
    result = sff.process_script()
    assert mixed_size_scramble_data.shape[0] == result.Final.shape[0]
