# NuRS_Python_Executable
A test of python executable formats for testing machines in the NHS.

This repository contains the implementations for:

* Alignment
* Scrambling
* Combining

of data sets extracted inside NHS Trusts.

To the reader - the core python implementation is in the [nurs_routine](nurs_routines) folder.  Each python script inside is a single standalone routine to produce a data set, using the tools implemeted in the [utilities](nurs_routines/utilities) sub-directory.

## Shuffling algorithm:

The data shuffling commands are implemented via the numpy.random.choice command.  Each column of the data set is exhaustively sampled without replacement.  If the frame is too small for shuffling to make a change, i.e. if there is only one case, an equivalent sized data set is returned with data removed i.e. a row of None values.

The implementation can be found [here](nurs_routines/utilities/utilities.py).

## Local level shuffle:

The shuffling algorithm is applied to data while it is clustered by features, e.g. ward and shift.  This is done via a call to a scramble function - either `scramble` or `scramble_to_file` as implemented [here](nurs_routines/utilities/scrambler.py).  This function in turn calls a handler function that divides the data into chunks and then applies `shuffle` - the functions for dividing the data are `split_apply` and `cached_split_apply` as implemented [here](nurs_routines/utilities/split_apply.py).  The difference between the two implementations being the choice to concatenate the chunks of shuffled data together either via appending to a temporary file or as a call to pandas.concat at the end.
