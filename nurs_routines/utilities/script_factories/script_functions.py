import os
from .. import Combiner, remove_pid
from .to_file_scripted import to_file_scripted


script_functions = {
    "Join file names": lambda file: os.path.join("Trust_data", file),
    "Combine data": Combiner,
    "Main routine": lambda x: x.main(),
    "Reset index": lambda x: x.reset_index(drop=True),
    "Remove PID": remove_pid,
    "To file": to_file_scripted
}