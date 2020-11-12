import pandas as pd


START = "2015-07"
END = "2020-06"
file_options = {
    "ESR_Leavers": {"name": "ESR_Leavers", "style": "Time series",
                    "window": "Full", "path": ""},
    "ESR_Sickness": {"name": "ESR_Sickness", "style": "Time series",
                     "window": "Full", "path": ""},
    "ESR_Mandatory_Training": {"name": "ESR_Mandatory_Training", "style": "Effective date",
                                    "window": "Monthly", "path": "ESR_Mandatory_Training"},
    "ESR_Demographics": {"name": "ESR_Demographics", "style": "Effective date",
                     "window": "Monthly", "path": "ESR_Demographics"},
    "Allocate_Accuity": {"name": "Allocate_Accuity", "style": "Time Series",
                         "window": "Quarterly", "path": "Allocate_Accuity"},
    "Allocate_Assignment": {"name": "Allocate_Assignment", "style": "Time Series",
                            "window": "Quarterly", "path": "Allocate_Assignment"},
    "Allocate_Shifts_Worked": {"name": "Allocate_Shifts_Worked", "style": "Time Series",
                               "window": "Quarterly", "path": "Allocate_Shifts_Worked"}
}


def time_series_names(name, start=START, end=END):
    return name


def monthly_names(name, start=START, end=END):
    dates = pd.date_range(start, end, freq="MS")
    dates = map(lambda date: date.strftime("%y%m%d"), dates)
    return map(lambda date: "{} {}".format(name, date), dates)


def quarterly_names(name, start=START, end=END):
    dates = pd.date_range(start, end, freq="3MS")
    dates = map(lambda date: date.strftime("%y%m%d"), dates)
    return map(lambda date: "{} {}".format(name, date), dates)


def name_dispatch(name, style, window, start=START, end=END):
    functions = {
        "Full": monthly_names,
        "Monthly": monthly_names,
        "Quarterly": quarterly_names
    }

    f = functions[window]
    return f(name, start, end)