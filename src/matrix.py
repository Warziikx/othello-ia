class Matrix:
    def __init__(self):
        pass
    def new_matrix(self, xSize, ySize, value=None):
        return [[value for x in range(xSize)] for y in range(ySize)]
