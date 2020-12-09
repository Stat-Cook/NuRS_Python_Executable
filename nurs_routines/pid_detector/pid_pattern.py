import re


class PIDPattern:

    def __init__(self, string: str):
        assert isinstance(string, str)
        self.start = string[0]
        self.body = string[1:]
        self.compiled = re.compile(self.to_pattern)

    @property
    def to_pattern(self):
        return ".*({upper}|{lower}){body}".format(
            upper=self.start.upper(),
            lower=self.start.lower(),
            body=self.body
        )

    def match(self, string):
        return bool(self.compiled.match(string))
