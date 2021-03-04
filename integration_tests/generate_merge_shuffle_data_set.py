import pandas as pd
import numpy as np

if __name__ == '__main__':
    dates = list(pd.date_range("2015-01-01", "2016-01-01"))
    ID = list("ABCDE")
    K = 10
    ward = dict(A="W1", B="W1", C="W1",
                D="W2", E="W2")

    data_frame = pd.DataFrame(dict(
        ID=np.concatenate([len(dates) * [i] for i in ID]),
        dates=len(ID) * dates,
        raw_value1=np.random.normal(size=len(ID) * len(dates)),
        raw_value2=np.random.normal(size=len(ID) * len(dates))
    ))
    data_frame["Ward"] = data_frame["ID"].apply(ward.get)
    data_frame.to_csv("integration_tests/test_data/data.csv", index=False)

    reference_frame = pd.DataFrame(dict(
        ID=np.concatenate([K * [i] for i in ID]),
        dates=np.concatenate([sorted(np.random.choice(dates, K)) for _ in range(len(ID))]),
        demographic1=np.random.normal(size=K * len(ID)),
        demographic2=np.random.normal(size=K * len(ID))
    )).to_csv("integration_tests/test_data/reference.csv", index=False)
