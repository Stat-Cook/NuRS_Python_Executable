"""
Tools for applying scripts in a uniform human readable manner.
"""
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

    def check_method_exists(self, string):
        """
        Check that the method has been implemented in the ScriptFunctionFactory
        Parameters
        ----------
        string: str
            method name to check
        Returns
        -------
        bool
        """
        return string in self.functions

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
            assert self.check_method_exists(task)

            arguments = arguments or {}
            task = self.functions[task]
            if not states:
                states += [task(**arguments)]
            else:
                states += [task(states[-1], **arguments)]

        return ScriptState(states[-1], states)
