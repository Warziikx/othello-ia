class Matrix:
    def __init__(self):
        pass

    def new_matrix(self, xSize, ySize, value=None):
        return [[value for x in range(xSize)] for y in range(ySize)]

    def get_size(self, matrix):
        rows_count = len(matrix)

        if rows_count is 0:
            return (0, 0)

        return (len(matrix[0]), rows_count)