from collections import Counter
import re
import os

from .file_structure import START, END, name_dispatch, file_options


class FileNameChecker:

    def __init__(self, name, style, window, path, start=START, end=END):
        self.name = name
        self.style = style
        self.window = window
        self.path = os.path.join("Trust_data", path)
        self.start = start
        self.end = end
        self.cnts = Counter(self.actual)

    @property
    def target(self):
        return list(name_dispatch(self.name, self.style, self.window))

    @property
    def actual(self):
        pattern = re.compile("\..*")
        return list(map(lambda x: pattern.sub("", x), os.listdir(self.path)))

    @property
    def extra_files(self):
        return [i for i in self.actual if i not in self.target]

    @property
    def missing_files(self):
        return [i for i in self.target if i not in self.actual]

    def report_missing(self):
        print("{} files missing.".format(len(self.missing_files)))
        if not self.missing_files:
            return 0

        print("Missing file summary:")
        for file in self.missing_files:
            print("\tFile '{}' not found at '{}'".format(file, self.path))

    def report_extra(self):
        print("{} extra files found.".format(len(self.extra_files)))
        if not self.extra_files:
            return 0

        print("Unnecesary file summary:")
        for file in self.extra_files:
            print("\tFile '{}' found at '{}'".format(file, self.path))

    def report_duplicates(self):
        dupes = [i for i, j in self.cnts.items() if j > 1]
        if dupes:
            print("No duplicates found")
            return 0
        else:
            print("{} duplicate file names found.".format(len(dupes)))
            for name in dupes:
                print("File '{}' duplicated at {}".format(name, self.path))

    def run_report(self):
        if self.style != "Time series":
            self.report_extra()
        self.report_missing()
        self.report_duplicates()


def check_file_names(name):
    _dict = file_options[name]
    checker = FileNameChecker(**_dict)
    checker.run_report()
