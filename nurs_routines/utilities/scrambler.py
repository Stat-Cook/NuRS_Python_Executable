from .utilities import split_apply, shuffle


def scramble(data, aggregate_cols, scrambling_cols):
    data = data.sort_values(aggregate_cols).reset_index(drop=True)

    shuffled_data = split_apply(
        data[scrambling_cols + aggregate_cols],
        aggregate_cols,
        shuffle
    )
    shuffled_data = shuffled_data.reset_index(drop=True)

    data[shuffled_data.columns] = shuffled_data
    return data
