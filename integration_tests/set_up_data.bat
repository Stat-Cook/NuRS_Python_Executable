call python integration_tests\generate_merge_shuffle_data_set.py

call python -m integration_tests.end_to_end_merge_test
call python -m integration_tests.end_to_end_merge_shuffle_test
