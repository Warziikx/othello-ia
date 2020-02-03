from itertools import product
import operator

class Vector:
    def __init__(self):
        pass

    def get_directionnal_vectors(self):
        """ Return an iterator of directinnal vectors (N, NE, E, SE, ..)"""

        directionnal_vectors = product((-1, 0, 1), (-1, 0, 1))
        return (vectors for vectors in directionnal_vectors if not vectors == (0, 0))


    def vector_add(self, v1, v2):
        return tuple(map(operator.add, v1, v2))


    def get_vector_add_generator(self, base_vector, vector):
        modified_vector = base_vector
        while True:
            modified_vector = self.vector_add(modified_vector, vector)
            yield modified_vector