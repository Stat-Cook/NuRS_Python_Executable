import os
from .. import Combiner, remove_pid, find_file, shuffle, \
    split_apply, load_data, MergeAsOf, scramble_to_file, GetMonth, to_file


class ScriptFunctionFactory:

    def __init__(self):
        pass

    def find_file(self, name, path="Trust_data"):
        if not isinstance(path, str):
            path = os.path.join(*path)
        return find_file(path, name)

    def scramble(self, data, keys):
        return split_apply(data, keys, shuffle)

    def load_data(self, name, path="Trust_data"):
        file_path = find_file(path, name)
        return load_data(file_path)

    def find_more_files(self, file, name, path):
        return [file] + [self.find_file(name, path)]

    def merge_as_of(self, paths, left_on, right_on, left_date, right_date):
        assert len(paths) == 2
        merger = MergeAsOf(*paths, left_on, right_on)
        merged_data = merger.main(left_date, right_date)
        return (
            merged_data,
            [i for i in merger.reference.columns if i in merged_data.columns]
        )

    def month_shuffler(self, data, aggregate_columns=None):
        month_shuffler = GetMonth()
        return month_shuffler.grouped_monthly_shuffle(data[0], aggregate_columns, data[1])

    def scramble_merge_as_of(self, data, aggregate_columns=None, file_path=None):
        assert len(data) == 2
        return scramble_to_file(
            data[0],
            aggregate_columns,
            data[1],
            file_path
        )

    def to_file_scripted(self, data, extract_path, file_name):
        if not isinstance(extract_path, str):
            extract_path = os.path.join(*extract_path)

        to_file(data, extract_path, file_name + ".csv")

        print("Complete - data written to {}".format(
            os.path.join(extract_path, file_name + ".csv"))
        )

        return data

    def manipulate_column(self, data, new_column, old_column, function):
        data[new_column] = data[old_column].apply(function)
        return data

    def combine_datasets(self, path, extract_date_function=None):
        return Combiner(path).main(extract_date_function=extract_date_function)

    @property
    def script_functions(self):
        return {
            "Apply function": lambda data, function: function(data),
            "Join file names": lambda file: os.path.join("Trust_data", file),
            "Find files": self.find_file,
            "Find more files": self.find_more_files,
            "Load data": self.load_data,
            "Combine datasets": self.combine_datasets,
            "Manipulate column": self.manipulate_column,
            "Reset index": lambda x: x.reset_index(drop=True),
            "Merge as of": self.merge_as_of,
            "Scramble": self.scramble,
            "Scramble as of": self.scramble_merge_as_of,
            "Scramble in months": self.month_shuffler,
            "Remove PID": remove_pid,
            "To file": self.to_file_scripted
        }
