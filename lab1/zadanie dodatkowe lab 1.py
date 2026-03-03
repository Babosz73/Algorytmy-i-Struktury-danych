class Matrix:
    def __init__(self, matrix, a = 0):
        if isinstance(matrix, tuple):
            self.__matrix = [[a for i in range(matrix[1])] for j in range(matrix[0])]
        else:
            self.__matrix = matrix
    
    def size(self):
        return (len(self.__matrix), len(self.__matrix[0]))
    
    def __add__(self, other):
        if self.size() != other.size():
            return None

        result = Matrix(self.size())
        
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                result.__matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
        return result
    
    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            return None
        
        result = Matrix((self.size()[0], other.size()[1]))

        for i in range(self.size()[0]):
            for j in range(other.size()[1]):
                for k in range(self.size()[1]):
                    result.__matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
        return result
        
    def __eq__(self, other):
        if self.size() != other.size():
            return False
        
        for i in range (self.size()[0]):
            for j in range (self.size()[1]):
                if self.__matrix[i][j] != other.__matrix[i][j]:
                    return False
        return True

    def __getitem__(self, row):
        return self.__matrix[row]
    
    def __str__(self):
        s = ""
        for i in self.__matrix:
            s += "|"
            for j in i:
                s += f" {j}"
            s += " |\n"
        return s
    
    def det(self):
        if self.size()[0] != self.size()[1]:
            return None
        
        if self.size() == (1, 1):
            return self.__matrix[0][0]
        
        if self.size() == (2, 2):
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]
        
        n = self.size()[0]
        znak = 1

        if self.__matrix[0][0] == 0:
            for i in range(1,n):
                if self.__matrix[i][0] != 0:
                    self.__matrix[0], self.__matrix[i] = self.__matrix[i], self.__matrix[0]
                    znak *= -1
                    break
            else:
                for j in range(1, n):
                    if self.__matrix[0][j] != 0:
                        for r in range(n):
                            self.__matrix[r][0], self.__matrix[r][j] = self.__matrix[r][j], self.__matrix[r][0]
                        znak *= -1
                        break
                else:
                    return 0

        elem11 = self.__matrix[0][0]
        if elem11 == 0:
            return 0
        MP = Matrix((n-1, n-1), a = 0)

        for i in range(1,n):
            for j in range(1,n):
                MP[i-1][j-1] = elem11 * self.__matrix[i][j] - self.__matrix[0][j] * self.__matrix[i][0]
        return znak*( MP.det() // (elem11 ** (n - 2)))

def transpos(m):
    row, cols = m.size()
    new = Matrix((cols, row))
    for i in range(row):
        for j in range(cols):
            new[j][i] = m[i][j]
    return new


if __name__ == "__main__":
    A1 = Matrix([
        [5 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
    ])
    print(A1.det())  #  -1396

    A2 = Matrix([
        [0 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
    ])
    print(A2.det())  #-236

    A3 = Matrix([
        [0 , 0 , 0 , 0 , 0],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
    ])
    print(A3.det())  # sero

    A4 = Matrix([
        [0 , 1 , 1 , 2 , 3],
        [0 , 2 , 1 , 7 , 3],
        [0 , 1 , 2 , 4 , 7],
        [0 , 1 , 0 , 7 , 0],
        [0 , 4 , 7 , 2 , 2]
    ])
    print(A4.det())  # mniej niż zero