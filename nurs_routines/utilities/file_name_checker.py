"""
Tools for reporting on file name/ folder structure.
Should match patterns set out in file_structure.py
"""

from collections import Counter
import re
import os
import logging

from .file_structure import START, END, name_dispatch, file_options


class FileNameChecker:
    """
    Check if file names and folder structures match the patterns set.
    Parameters
    ----------
    name: str
        The name of data set being checked.
    style: str - choice of ['Time series', 'Effective date']
        The type of data being analyzed
    windows: str - choice of ['Full', 'Monthly', 'Quarterly']
        The regularity of the data sets.
    path:str
        Expected relative path to the data
    start: str or date
        Date at which data sets start
    end: str or date
        Date at which data sets end

    Attributes
    ----------
    cnts: collections.Counter
        A count of how often each file name is used.
    """

    def __init__(self,
                 name, style, window, path,
                 start=START, end=END, prepend_path="Trust_data"
                 ):
        # pylint: disable=too-many-arguments
        self.name = name
        self.style = style
        self.window = window
        self.path = os.path.join(prepend_path, path)
        self.start = start
        self.end = end
        self.cnts = Counter(self.actual)

    @property
    def target(self):
        """List all files we wish to find."""
        return list(name_dispatch(self.name, self.style, self.window))

    @property
    def actual(self):
        """List all files at 'path'"""
        pattern = re.compile(r"\..*")
        return list(map(lambda x: pattern.sub("", x), os.listdir(self.path)))

    @property
    def extra_files(self):
        """List all files at 'path' that aren't required."""
        return [i for i in self.actual if i not in self.target]

    @property
    def missing_files(self):
        """List files not in 'path' that are required."""
        return [i for i in self.target if i not in self.actual]

    @property
    def duplicate_files(self):
        """List files at 'path' that have duplicated names (excluding file type)."""
        return [i for i, j in self.cnts.items() if j > 1]

    def _report(self, data, report_type, raise_exception=False):
        """
        Utility template for other reports:
        Parameters
        ----------
        data: list or None
            The relevant files to report on.
        report_type: str - one of ['Missing', 'Unexpected', 'Duplicated']
            A name for the report.
        """
        logging.info("%s %s file(s).", len(data), report_type)
        if data:
            logging.info("%s file summary:", report_type)
            for file in data:
                logging.info("\tFile '%s' %s at '%s'", file, report_type, self.path)
            if raise_exception:
                raise raise_exception(data)

    def report_missing(self, raise_exception=False):
        """
        Report which files were missing
        Parameters
        ----------
        raise_exception: bool
            On error - raise an exception.  If false details are logged to file.
        """
        if raise_exception:
            raise_exception = lambda data: FileNotFoundError(
                "Files are missing:\n\t{}".format("\n\t".join(data))
            )
        self._report(
            self.missing_files,
            "Missing",
            raise_exception
        )

    def report_extra(self, raise_exception=False):
        """
        Report which files were unnecessary.
        Parameters
        ----------
        raise_exception: bool
            On error - raise an exception.  If false details are logged to file.
        """
        if raise_exception:
            raise_exception = lambda data: Exception(
                "Files are unexpected:\n\t{}".format("\n\t".join(data))
            )
        self._report(
            self.extra_files,
            "Unexpected",
            raise_exception
        )

    def report_duplicates(self, raise_exception=False):
        """
        Report which files were duplicates.
        Parameters
        ----------
        raise_exception: bool
            On error - raise an exception.  If false details are logged to file.
        """
        if raise_exception:
            raise_exception = lambda data: Exception(
                "Files are duplicated:\n\t{}".format("\n\t".join(data))
            )
        self._report(
            self.duplicate_files,
            "Duplicated",
            raise_exception
        )

    def run_report(self):
        """
        Run all required reports.
        """
        if self.style != "Time series":
            self.report_extra()
        self.report_missing()
        self.report_duplicates()


def check_file_names(name):
    """
    Run a FileNameCheck on a given name
    Parameters
    ----------
    name: str
        The type of file to check names for.
        Needs to be found in file_structure.file_options.
    """
    _dict = file_options[name]
    checker = FileNameChecker(**_dict)
    checker.run_report()
