from collections import defaultdict


class PIDResults(defaultdict):

    def __repr__(self):
        return "PIDResults({})".format(self.size_summary)

    @property
    def size_summary(self):
        return {i: len(j) for i, j in self.items()}

    @property
    def context_factory(self):
        for pattern, data in self.items():
            if len(data) > 0:
                yield f"Pattern: {pattern}".format(pattern=pattern)
                for row, column, value in data:
                    yield f"\t'{value}' found at [{row}, {column}]".format(
                        row=row, column=column, value=value
                    )

    def context_to_screen(self):
        for context in self.context_factory:
            print(context)
