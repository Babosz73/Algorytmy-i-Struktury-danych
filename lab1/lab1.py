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