"""
Dictionary of PID results
"""

from collections import defaultdict


class PIDResults(defaultdict):
    """
    Dictionary of PID results
    """
    def __repr__(self):
        return "PIDResults({})".format(self.size_summary)

    @property
    def size_summary(self):
        """
        Report summary of how often each pattern was used.
        Returns
        -------
        dict
        """
        return {i: len(j) for i, j in self.items()}

    @property
    def context_factory(self):
        """
        Report line by line how each PID pattern was used.
        Returns
        -------
        yield
        """
        for pattern, data in self.items():
            if len(data) > 0:
                yield f"Pattern: {pattern}".format(pattern=pattern)
                for row, column, value in data:
                    yield f"\t'{value}' found at [{row}, {column}]".format(
                        row=row, column=column, value=value
                    )

    def context_to_screen(self):
        """
        Print results of PID match to screen.
        Returns
        -------
        None
        """
        for context in self.context_factory:
            print(context)

    def context_to_file(self, filename):
        """
        Export PID results to file
        Parameters
        ----------
        filename: str
            Target file for export
        Returns
        -------
        None
        """
        with open(filename, "w") as f:
            for context in self.context_factory:
                f.write(context)
