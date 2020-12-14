import os
from collections import namedtuple

from utilities import define_logger, to_file
from .script_functions import script_functions

ScriptState = namedtuple("ScriptState", ("Initial", "Final", "Full"))


class ScriptFactory:

    def __init__(self, extract_path="", file_name="", tasks: dict = None):
        self.extract_path = extract_path
        self.file_name = file_name
        self.tasks = tasks or {}
        define_logger(extract_path, file_name)

    def process_script(self, state):
        states = [state]
        for task, arguments in self.tasks.items():
            arguments = arguments or []
            task = script_functions[task]
            states += [task(states[-1], *arguments)]

        return ScriptState(state, states[-1], states)
