import os

from .io import load_data


class CombineFile:

    def __init__(self, file, path, expected_columns: list = None):
        self.file = file
        self.path = path
        self.expected_columns = expected_columns

    def __repr__(self):
        return f"CombineFile(file={self.file}, path={self.path}, " \
               f"expected_columns={self.expected_columns})"

    def load_data(self):
        file_path = os.path.join(self.path, self.file)
        return load_data(file_path)

    def apply_extract_date_function(self, extract_date_function, data):
        data["Date_stamp"] = extract_date_function(self.file)
        return data

    def compare_column_length(self, proposed_columns):
        len_expected = len(self.expected_columns)
        len_proposed = len(proposed_columns)

        if len_expected != len_proposed:
            raise ValueError(
                f"New data columns  not of same length as expected columns "
                f"({len_proposed} vs {len_expected})."
                f"  Error with file ({self.file})"
            )

    def compare_column_content(self, proposed_columns):
        if any(i != j for i, j in zip(self.expected_columns, proposed_columns)):
            raise AttributeError(
                f"New data columns do not match expected columns, error with file {self.file}"
            )

    def are_columns_consistent(self, proposed_columns: list):
        if isinstance(proposed_columns, str):
            raise TypeError("Argument `proposed_columns` should be a list or tuple.")

        if self.expected_columns is None:
            return True

        self.compare_column_length(proposed_columns)
        self.compare_column_content(proposed_columns)

        return True
    
    def process_file(self, extract_date_function=None, *args, **kwargs):
        data = self.load_data()
        
        if extract_date_function:
            data = self.apply_extract_date_function(extract_date_function, data)

        self.are_columns_consistent(data.columns)

        return data
        