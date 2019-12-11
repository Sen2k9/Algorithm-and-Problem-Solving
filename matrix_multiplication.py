import pdb

i = 0
j = 0
k = 0


def recursive_mul(rowx, colx, X, rowy, coly, Y, N, M):

    global i
    global j
    global k

    if i >= rowx:
        return
    if i < rowx:
        if j < coly:
            if k < N:
                M[i][j] = M[i][j] + X[i][k] * Y[k][j]
                k += 1
                recursive_mul(rowx, colx, X, rowy, coly, Y, N, M)

            j += 1
            k = 0
            recursive_mul(rowx, colx, X, rowy, coly, Y, N, M)
        i += 1
        j = 0

        recursive_mul(rowx, colx, X, rowy, coly, Y, N, M)
    return M


def matrix_mul(rowx, colx, X, rowy, coly, Y, N):
    # pdb.set_trace()

    M = [[0] * coly for _ in range(rowx)]
    return recursive_mul(rowx, colx, X, rowy, coly, Y, N, M)


def main(X, Y):
    rowx = len(X)
    colx = len(X[0])
    rowy = len(Y)
    coly = len(Y[0])

    if rowx != coly:
        print("Matrix Multiplication not possible. Need same size of X and Y")
    else:
        print(matrix_mul(rowx, colx, X, rowy, coly, Y, len(X)))


x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]

main(x, y)
