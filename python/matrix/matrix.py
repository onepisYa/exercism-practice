class Matrix:
    def __init__(self, matrix_string):
        self.matrix_li = [i.split(' ') for i in matrix_string.split('\n')]

    def row(self, index):
        return list(map(int, self.matrix_li[index - 1]))

    def column(self, index):
        return [int(i[index - 1]) for i in self.matrix_li]
