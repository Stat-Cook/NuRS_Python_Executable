import numpy as np
import pandas as pd
from .pid_result import PIDResults
from .pid_pattern import PIDPattern


class PIDReporter:

    def __init__(self, pattern_list):
        self.pattern_list = pattern_list
        self.melted = None
        self.results_dict = PIDResults(dict)

    def melt_data(self, data: pd.DataFrame):
        self.melted = data.melt(ignore_index=False)

    def check_pattern(self, pattern):
        if self.melted is None:
            raise AttributeError("Data not loaded yet.")

        compiled_pattern = PIDPattern(pattern)
        sel = self.melted[self.melted["value"].apply(str).apply(compiled_pattern.match).apply(bool)]
        pid_location = np.transpose([sel.index, sel["variable"], sel["value"]])
        return pid_location

    def check_data(self):
        results_dict = PIDResults(dict)

        for pattern in self.pattern_list:
            results_dict[pattern] = self.check_pattern(pattern)

        return results_dict

    def check_data_set(self, data):

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        self.melt_data(data)
        return self.check_data()

    def report_data_set_to_file(self, data, filename):
        results = self.check_data_set(data)
        results.context_to_screen()
        results.context_to_file(filename)
        return results
