
# from unittest import assertAlmostEqual

class MatrixImpN(object):
    """Creates a matrix ([[1,0],[0,1]])"""
    #####################
    ####Magic Methods####
    #####################

    def __init__(self, matrix):
        self.width, self.height, self.matrix = self.checkMatrix(matrix)

    def __add__(self, other):
        self.checkBeforeAdding(other)
        old_matrices = zip(self.matrix, other.matrix)
        new_matrix = []
        for self_line, other_line in old_matrices:
            old_lines = zip(self_line, other_line)
            new_line = []
            for self_num, old_num in old_lines:
                new_line.append(self_num+old_num)
            new_matrix.append(new_line)
        com_matrix = MatrixImpN(new_matrix)
        return com_matrix

    def __mul__(self, other):
        tpe = type(other)
        if tpe == int:
            result = self.scalar_mul(other)
        elif tpe == MatrixImpN:
            result = self.dot_product(other)
        else:
            raise Exception("Object type not currently compatible for multiplication with matrices")
        return result

    def __getitem__(self, across, down):
        across = across - 1
        down = down - 1
        matrix = self.matrix
        item = matrix[down][across]
        return item

    def __eq__(self, other):
        t_f = True
        if (self.height == other.height) and (self.width == other.width):
            matrices = zip(self.matrix, other.matrix)
            for self_row, other_row in matrices:
                rows = zip(self_row, other_row)
                for self_num, other_num in rows:
                    if self_num == 0 or other_num == 0:
                        t_f = self_num == other_num
                    else:
                        diff = (self_num-other_num)/other_num
                        t_f = diff < 10**-9 and diff > -10**-9
                    if not(t_f):
                        return t_f
        elif (self.height != other.height) and (self.width != other.width):
            t_f = False
        return t_f


    def __repr__(self):
        string = ""
        for row in self.matrix:
            string += "{}\n".format(row)
        return string

    #######################
    ####custom commands####
    #######################
    def scalar_mul(self, other):
        new_matrix = []
        for row in self.matrix:
            new_row = []
            for value in row:
                new_value = value * other
                new_row.append(new_value)
            new_matrix.append(new_row)
        return MatrixImpN(new_matrix)

    def dot_product(self, other):
        self.checkBeforeMultiplying(other)
        new_matrix = []
        for self_line in self.matrix:
            new_line = []
            for idx in range(0, len(other.matrix[0])):
                other_line = [item[idx] for item in other.matrix]
                old_lines = zip(self_line, other_line)
                new_num = sum([self_num * other_num for self_num, other_num in old_lines])
                new_line.append(new_num)
            new_matrix.append(new_line)
        com_matrix = MatrixImpN(new_matrix)
        return com_matrix

    @staticmethod
    def checkMatrix(matrix):
        widths = [len(row) for row in matrix]
        width = widths[0]
        if all([width == w for w in widths]):
            return width, len(matrix), matrix
        else:
            raise Exception("Matrix not rectangle/square.")

    def checkBeforeAdding(self, other):
        if (self.height == other.height) and (self.width == other.width):
            pass
        else:
            raise Exception("Matrices not compatible for addition.")

    def checkBeforeMultiplying(self, other):
        if self.width == other.height:
            pass
        else:
            raise Exception("Matrices not compatible for multiplication.")

    @classmethod
    def identityMatrix(cls, length):
        """Creates a identity matrix (length)"""
        row = cls([[1]*length])
        return row.diagonal()

    def vector(self):
        """Makes a row vector out of column or row vector"""
        if self.height == 1:
            return self.matrix[0]
        elif self.width == 1:
            row = []
            for i in range(self.height):
                row.append(self.matrix[i][0])
            return row
        else:
            raise Exception("Matrix not vector")

    def diagonal(self):
        """Makes diagonal matrix out of a vector matrix [[1,2,3]] --> [[1,0,0],[0,2,0],[0,0,3]]"""
        vector = self.vector()
        length = len(vector)
        matrix = []
        for i in range(length):
            row = [0]*length
            row[i] = vector[i]
            matrix.append(row)
        return self.__class__(matrix)


# a = MatrixImpN.identityMatrix(3)
# b = MatrixImpN([[1, 2, 3]])# a = MatrixImpN.identityMatrix(3)
# b = MatrixImpN([[1, 2, 3]])
# b = b.diagonal()
# print b*2
# print a

# b = b.diagonal()
# print b*2
# print a
