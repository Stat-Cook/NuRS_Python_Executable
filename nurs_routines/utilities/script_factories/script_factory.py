from collections import namedtuple

from .. import define_logger
from .script_functions import ScriptFunctionFactory


ScriptState = namedtuple("ScriptState", ("Final", "Full"))


class ScriptFactory:

    """
    Bind all functions used from utilities to a pipe-able design pattern and
    human readable names.
    """

    def __init__(self, extract_path="", file_name="", tasks: dict = None):
        self.extract_path = extract_path
        self.file_name = file_name
        self.tasks = tasks or {}
        self.functions = ScriptFunctionFactory().script_functions
        define_logger(extract_path, file_name)

    def process_script(self):
        """
        Run through all commands in self.tasks applying them in order.
        Parameters
        ----------
        Returns
        -------
        """
        states = []
        for task, arguments in self.tasks.items():
            arguments = arguments or {}
            task = self.functions[task]
            if not states:
                states += [task(**arguments)]
            else:
                states += [task(states[-1], **arguments)]

        return ScriptState(states[-1], states)
