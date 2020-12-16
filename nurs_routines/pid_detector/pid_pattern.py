"""
PID tool for compiling pattern to regex.
"""
import re


class PIDPattern:
    """
    Automated compilation of regex pattern for finding names.
    """

    def __init__(self, string: str):
        assert isinstance(string, str)
        self.start = string[0]
        self.body = string[1:]
        self.compiled = re.compile(self.to_pattern)

    @property
    def to_pattern(self):
        """
        Convert the string to a regex pattern
        Returns
        -------
        regex string
        """
        return r".*({upper}|{lower}){body}".format(
            upper=self.start.upper(),
            lower=self.start.lower(),
            body=self.body
        )

    def match(self, string):
        """
        Check if a given word contains the pattern
        Parameters
        ----------
        string: str
            Free text to check for match.
        Returns
        -------
        bool
        """
        return bool(self.compiled.match(string))
