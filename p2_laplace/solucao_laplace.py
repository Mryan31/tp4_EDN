import numpy as np

def solucao_analitica_laplace(x, y):
    """
    Derivada por separação de variáveis:
    u(x,y) = sin(pi*x) * sinh(pi*(1-y)) / sinh(pi)
    """
    term1 = np.sin(np.pi * x)
    term2 = np.sinh(np.pi * (1.0 - y))
    denom = np.sinh(np.pi)
    
    return term1 * term2 / denom

def solver_numerico_laplace(dx, dy, tol=1e-6):
    """
    Resolve a Equação de Laplace (Delta u = 0) [cite: 13]
    em Omega = (0,1)x(0,1) [cite: 22] usando o método iterativo 
    de Gauss-Seidel (que é uma forma do método das diferenças finitas).
    """
    M = int(1.0 / dx) + 1
    N = int(1.0 / dy) + 1
    
    x_vec = np.linspace(0, 1, M)
    y_vec = np.linspace(0, 1, N)
    X, Y = np.meshgrid(x_vec, y_vec)
    
    U = np.zeros((N, M)) # U(y, x) -> U[j, i]
    
    # u(x,0) = sin(pi*x)
    U[-1, :] = np.sin(np.pi * x_vec) # y=0 é o último índice (N-1) no meshgrid
    
    # u(x,1) = 0
    U[0, :] = 0.0                    # y=1 é o primeiro índice (0)
    
    # u(0,y) = 0
    U[:, 0] = 0.0
    
    # u(1,y) = 0
    U[:, -1] = 0.0
    
    # (Assume dx = dy = h)
    h2 = dx * dx
    erro = tol + 1.0 # Garante entrada no loop
    it = 0
    max_it = 10000
    
    while erro > tol and it < max_it:
        U_antigo = U.copy()
        erro = 0.0
        
        for j in range(1, N - 1):
            for i in range(1, M - 1):
                U[j, i] = 0.25 * (U[j, i+1] + U[j, i-1] + U[j+1, i] + U[j-1, i])

        # Calcula o erro máximo na malha
        erro = np.max(np.abs(U - U_antigo))
        it += 1
        
    if it == max_it:
        print(f"Aviso: Solver de Laplace atingiu {max_it} iterações.")
        
    print(f"Solver Laplace (dx={dx:.4f}): Convergiu em {it} iterações.")
    
    return X, Y, U