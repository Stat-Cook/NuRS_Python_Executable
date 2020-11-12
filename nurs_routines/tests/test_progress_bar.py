from nurs_routines.utilities.progress_bar import ProgressBar

@pytest.fixture
def progress_bar():
    return ProgressBar(20, 10)
