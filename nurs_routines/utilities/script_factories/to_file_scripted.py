import os
from utilities import to_file


def to_file_scripted(data, extract_path, file_name):
    extract_path = os.path.join(*extract_path)

    to_file(data, extract_path, file_name + ".csv")

    print("Complete - data written to {}".format(
        os.path.join(extract_path, file_name + ".csv"))
    )

    return data
