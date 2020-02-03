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
    
    def get_cell(self, matrix, xPos, yPos, default=None):
    # Return cell value, return default if no one is find
        try:
            # Disable negative index functionnality
            if yPos < 0 or xPos < 0:
                raise IndexError
            return matrix[yPos][xPos]
        except LookupError:
            return default
