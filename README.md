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
