import os
import pandas as pd
import numpy as np


def find_file(path, name):
    _dir = os.listdir(path)
    files = [i for i in _dir if name in i]
    files = [i for i in files if (".xls" in i) or (".csv" in i)]
    if not files:
        raise Exception(
            "File not found of correct file type (csv, xls, or xlsx) for file {}".format(name)
        )
    if len(files) == 1:
        return os.path.join(path, files[0])
    else:
        return [os.path.join(path, file) for file in files]


def load_data(file_path):
    if ".csv" in file_path:
        return pd.read_csv(file_path)
    else:
        return pd.read_excel(file_path)


def shuffle(frm, size_check, name=None, *args):
    n = frm.shape[0]
    if size_check:
        if not name:
            assert n > 1, "Not enough data to shuffle."
        else:
            assert n > 1, "Not enough data for {} to shuffle".format(name)
    return frm.apply(lambda x: np.random.choice(x, frm.shape[0]))


def split_apply(frm, groupby, func, size_check=False):
    grps = frm.groupby(groupby)
    return pd.concat([func(j, size_check, i) for i,j in grps])
