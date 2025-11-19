import numpy as np
from . import solucao_laplace as lap
from .. import plot_utils

def executar_parte2():
    print("\n--- Executando TP4 - Parte 2: Equação de Laplace ---")
    
    malhas_h = [0.5, 0.25, 0.125, 0.0625]
    
    erros_centro = []
    dxs_lista = []
    
    print("Calculando erros no ponto (0.5, 0.5)...")
    
    for h in malhas_h:
        dx = h
        dy = h
        dxs_lista.append(h)
        
        # 1. Solução Numérica
        X_num, Y_num, U_num = lap.solver_numerico_laplace(dx, dy)
        
        # 2. Solução Analítica
        U_exata = lap.solucao_analitica_laplace(X_num, Y_num)
        
        # 3. Encontrar o ponto (0.5, 0.5) [cite: 25]
        idx_i_centro = int(X_num.shape[1] / 2) # Índice x=0.5
        idx_j_centro = int(X_num.shape[0] / 2) # Índice y=0.5
        
        ponto_num = U_num[idx_j_centro, idx_i_centro]
        ponto_exato = U_exata[idx_j_centro, idx_i_centro]
        
        erro_abs = np.abs(ponto_num - ponto_exato)
        erros_centro.append(erro_abs)
        
        print(f"  h = {h:.4f} | Num: {ponto_num:.6f} | Exato: {ponto_exato:.6f} | Erro: {erro_abs:.2e}")

        if h == malhas_h[-1]:
            plot_utils.plot_laplace_solucao(X_num, Y_num, U_num, 
                                            f"Solucao Numerica (h={h})")
            plot_utils.plot_laplace_solucao(X_num, Y_num, U_exata, 
                                            "Solucao Analitica")
            plot_utils.plot_laplace_solucao(X_num, Y_num, np.abs(U_num - U_exata), 
                                            f"Erro Absoluto (h={h})")

    plot_utils.plot_convergencia_laplace(dxs_lista, erros_centro)
    
    print("--- Parte 2 Concluída ---")

if __name__ == "__main__":
    executar_parte2()