import numpy as np


class SampleClass:
    @staticmethod
    def sample_method(a, b):
        return a + b

    @staticmethod
    def sum_a_list(list_of_numbers):
        array_of_numbers = np.array(list_of_numbers)
        return array_of_numbers.sum()
