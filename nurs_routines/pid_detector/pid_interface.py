import os
import pandas as pd
from .pid_report import PIDReporter


PATH = os.path.dirname(os.path.realpath(__file__))
PATTERNS = pd.read_table(os.path.join(PATH, "names.txt"), header=None).values.flatten()

PID_INTERFACE = PIDReporter(PATTERNS)
PID_DEFAULT_REPORT = PID_INTERFACE.check_data_set
