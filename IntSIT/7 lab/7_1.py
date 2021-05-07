class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, m):
        self.m = m.copy()

    def __str__(self):
        str_ = ""
        k_lines = len(self.m)
        k_el = len(self.m[0])
        for line in range(k_lines):
            for el in range(k_el):
                str_ += str(self.m[line][el])
                if el < k_el - 1:
                    str_ += "\t"
                elif line < k_lines:
                    str_ += "\n"
        return str_

    def __add__(self, other):
        if len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0]):
            add_m = []
            k_lines = len(self.m)
            k_el = len(self.m[0])
            for line in range(k_lines):
                add_m.append([])
                for el in range(k_el):
                    add_m[line].append(self.m[line][el] + other.m[line][el])
        else:
            raise MatrixError(self, other)
        return Matrix(add_m)

    def __mul__(self, a):
        k_lines = len(self.m)
        k_el = len(self.m[0])
        if isinstance(a, int) or isinstance(a, float):
            mul_m = []
            for line in range(k_lines):
                mul_m.append([])
                for el in range(k_el):
                    mul_m[line].append(self.m[line][el] * a)
        elif len(self.m[0]) == len(a.m):
            mul_m = Matrix([[0 for i in range(len(a.m[0]))] for j in range(len(self.m))])
            for i in range(len(self.m)):  # 3
                for j in range(len(a.m[0])):  # 1
                    for k in range(len(a.m)):  # 3
                        mul_m.m[i][j] += self.m[i][k] * a.m[k][j]
        else:
            print(self.m[0], a.m)
            raise MatrixError(self, a)
        return mul_m

    def __rmul__(self, a):
        return self.__mul__(a)

    def transpose(self):
        trans_m = list(zip(*self.m))
        self.m = trans_m
        return Matrix(trans_m)

    def transposed(self):
        trans_m = list(zip(*self.m))
        return Matrix(trans_m)


def main():
    """Start the main function."""
    m1 = Matrix([[3, -1, 2], [4, 2, 0], [-5, 6, 1]])
    m2 = Matrix([[8], [7], [2]])
    print(m1 * m2)


if __name__ == '__main__':
    main()
