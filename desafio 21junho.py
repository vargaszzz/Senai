#variaveis
def quadrado_magico(mat):
    n = len(mat)
    soma = sum(mat[0])
#linhas
    for i in range(n):
        if sum (mat[i]) != soma or sum(mat[i][j] for j in range (n)) != soma:
            return False

    if sum(mat[i][i] for i in range (n)) != soma or  sum(mat[i][n - 1 - i]for i in range(n)) != soma:
        return False
    
    return True

def main():
    n = int(input("Digite  a dimensao da matriz N:"))

    matriz = []
    for i in range(n):
    print("Digite os valores da matriz:")

