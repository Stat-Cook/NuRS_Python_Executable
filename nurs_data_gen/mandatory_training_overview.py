import pandas as pd
import numpy as np

columns = ["Organisation", "Achieved", "Required"]
orgs = list("ABCDEFGH")


def generate_data(orgs=orgs, columns=columns):
    required = np.random.randint(10, 15, len(orgs))
    achieved = required - np.random.randint(0, 5, len(orgs))

    return pd.DataFrame(
        np.transpose([orgs, required, achieved]),
        columns=columns
    )


if __name__ == '__main__':

    dates = pd.date_range("2015-01-01", "2020-01-01", freq="MS")
    for date in dates:
        data = generate_data()
        data.to_csv(
            f"Trust_data/ESR_Mandatory_Training/Mandatory_Training_Overview {date.date()}.csv",
            index=False
        )
