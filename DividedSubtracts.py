import math


class DividedSubtracts:

    def __init__(self, x: list, f_x: list):
        self._step = x

        self._matrix = []
        self._matrix += [f_x]

        self._nSteps = len(x)

    def __getitem__(self, index_offset):
        if type(index_offset) is int:
            return self._matrix[index_offset]
        index, offset = index_offset
        return self.get_value(index=index, offset=offset)

    def get_value(self, index: int, offset: int):

        assert index >= 0, index < self._nSteps
        assert offset >= 0

        while len(self._matrix) <= offset:
            self._matrix.append(list())
        while len(self._matrix[offset]) <= index:
            self._matrix[offset].append(float('nan'))

        if math.isnan(self._matrix[offset][index]):
            self._matrix[offset][index] = (self.get_value(index=index + 1, offset=offset - 1) - self.get_value(
                index=index, offset=offset - 1)) / (self._step[index + offset] - self._step[index])

        return self._matrix[offset][index]
