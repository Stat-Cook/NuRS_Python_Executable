import pandas as pd
import os


class Combiner:

    def __init__(self, path):
        self.path = path
        self.data = None
        self.columns = None

    @property
    def path_content(self):
        return os.listdir(self.path)

    def read_data(self, file):
        if ("xls" in file) or ("xlsx" in file):
            return pd.read_excel(file)
        else:
            return pd.read_csv(file)

    def iterate_through_path(self, extract_date_function):
        for file in self.path_content:
            file_path = os.path.join(self.path, file)
            new_data = self.read_data(file_path)

            if extract_date_function:
                new_data["Date_stamp"] = extract_date_function(file)

            if self.columns is None:
                self.columns = new_data.columns

            # Check that the new files have the same headings as the first
            if any(self.columns != new_data.columns):
                raise Exception(
                    "New data headings do not match first, error with file {}".format(file)

                )
            yield new_data

    def read_and_combine(self, extract_date_function):
        _iter = self.iterate_through_path(extract_date_function=extract_date_function)
        return pd.concat(_iter)

    def check_file_types(self):
        for file in self.path_content:
            file_type = any([i in file for i in ["xlsx", "xls", "csv"]])

            if not file_type:
                raise Exception(
                    "Incorrect file type found (not xlsx, xls, or csv) for file {}.  "
                    "Please remove from folder {}".format(file, self.path)
                )

    def main(self, extract_date_function=None):
        print("Checking file types in {}".format(self.path))
        self.check_file_types()
        print("File types - Passed")
        print("Opening and combining files in {}".format(self.path))
        result = self.read_and_combine(extract_date_function)
        print("Combination - Succesful")
        return result

    def __repr__(self):
        return "Combiner(path={}, number_of_files={})".format(
            self.path, len(self.path_content)
        )
