import numpy as np

def aplicar_fronteira_periodica(U):
    # Assume que os pontos 'ghost' estão em U[0] e U[-1]
    # Se bem que para os esquemas abaixo, é mais fácil
    # tratar na hora. Vamos usar U[1:-1] como pontos de cálculo.
    
    # Para U[1] (primeiro ponto), U[0] é o 'vizinho'
    # Para U[-2] (último ponto), U[-1] é o 'vizinho'
    U[0] = U[-2] # Ponto fantasma à esquerda é o último ponto real
    U[-1] = U[1] # Ponto fantasma à direita é o primeiro ponto real
    return U

def esquema_upwind(U_n, a, cfl):
    U_nm1 = U_n.copy()
    c = cfl * np.sign(a) # c = a*dt/dx
    
    if a > 0:
        # U_j^{n+1} = U_j^n - cfl * (U_j^n - U_{j-1}^n)
        for j in range(1, len(U_n) - 1):
            U_nm1[j] = U_n[j] - c * (U_n[j] - U_n[j-1])
    else:
        # U_j^{n+1} = U_j^n - cfl * (U_{j+1}^n - U_j^n)
        for j in range(1, len(U_n) - 1):
            U_nm1[j] = U_n[j] - c * (U_n[j+1] - U_n[j])
            
    return U_nm1

def esquema_lax_friedrichs(U_n, a, cfl):
    U_nm1 = U_n.copy()
    c = cfl * np.sign(a) # c = a*dt/dx
    
    # U_j^{n+1} = 0.5*(U_{j+1}^n + U_{j-1}^n) - 0.5*c * (U_{j+1}^n - U_{j-1}^n)
    for j in range(1, len(U_n) - 1):
        U_nm1[j] = 0.5 * (U_n[j+1] + U_n[j-1]) - 0.5 * c * (U_n[j+1] - U_n[j-1])
        
    return U_nm1

def esquema_lax_wendroff(U_n, a, cfl):
    U_nm1 = U_n.copy()
    c = cfl * np.sign(a) # c = a*dt/dx
    c2 = c**2
    
    # U_j^{n+1} = U_j^n - 0.5*c*(...) + 0.5*c^2*(...)
    for j in range(1, len(U_n) - 1):
        U_nm1[j] = U_n[j] \
                   - 0.5 * c * (U_n[j+1] - U_n[j-1]) \
                   + 0.5 * c2 * (U_n[j+1] - 2*U_n[j] + U_n[j-1])
                   
    return U_nm1

def simulador_transporte(cond_inicial_func, esquema_func, L, T_final, a, dx, cfl):
    # Malha espacial (com pontos fantasma nas bordas)
    Nx = int(L / dx) + 1
    x_vec = np.linspace(0 - dx, L + dx, Nx + 2) # Pontos de x[-1] a x[Nx+1]
    
    # Malha temporal
    dt = cfl * dx / np.abs(a)
    Nt = int(T_final / dt)
    t_vec = np.linspace(0, T_final, Nt + 1)
    
    print(f"Simulando com {esquema_func.__name__} e {cond_inicial_func.__name__}")
    print(f"dx={dx:.4f}, dt={dt:.4f}, cfl={cfl:.2f}, Nt={Nt}")
    
    # Condição inicial
    U = cond_inicial_func(x_vec)
    U_solucao = [U.copy()[1:-1]] # Salva a solução (sem pontos fantasma)
    t_solucao = [0.0]
    
    # Pontos de plot
    t_plots = np.linspace(0, T_final, 5)[1:] # 4 snapshots (sem t=0)
    t_idx_prox = 0
    
    for n in range(Nt):
        # Aplica fronteira periódica nos pontos fantasma
        U = aplicar_fronteira_periodica(U)
        
        # Calcula o próximo passo
        U = esquema_func(U, a, cfl)
        
        # Salva snapshots
        if t_vec[n+1] >= t_plots[t_idx_prox]:
            U_solucao.append(U.copy()[1:-1])
            t_solucao.append(t_vec[n+1])
            t_idx_prox += 1
            if t_idx_prox >= len(t_plots):
                break # Já salvamos todos os snapshots
                
    return x_vec[1:-1], U_solucao, t_solucao