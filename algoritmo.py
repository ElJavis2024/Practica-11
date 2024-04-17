def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0[:]
    for k in range(max_iter):
        x_old = x[:]
        for i in range(n):
            sum_1 = sum(A[i][j] * x[j] for j in range(i))
            sum_2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_1 - sum_2) / A[i][i]
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            break
    return x

A = [[4, 1, 2],
     [2, 4, -1],
     [1, 1, -3]]
b = [9, -5, -9]

x0 = [0, 0, 0]

sol = gauss_seidel(A, b, x0)

print("La solución es:", sol)

