from . import esquemas_transporte as esq
from . import condicoes_iniciais as ci
from .. import plot_utils # Importa do diretório pai

def executar_parte1():
    print("--- Executando TP4 - Parte 1: Equação do Transporte ---")
    
    # --- Parâmetros da Simulação ---
    L = 1.0       # Tamanho do domínio
    a = 1.0       # Velocidade
    T_final = 1.0 # Tempo final (dá 1 volta completa se L=1, a=1)
    
    # Parâmetros de estabilidade
    DX = 0.01     # Resolução espacial
    CFL = 0.8     # Número CFL (deve ser <= 1 para estabilidade) [cite: 5]
    
    # Lista de esquemas e condições iniciais
    esquemas = [
        esq.esquema_upwind, 
        esq.esquema_lax_friedrichs, 
        esq.esquema_lax_wendroff
    ]
    
    condicoes = [
        ci.gaussiana,        # Suave 
        ci.onda_quadrada     # Descontinuidade 
    ]
    
    for cond_func in condicoes:
        for esq_func in esquemas:
            
            x, U_snaps, t_snaps = esq.simulador_transporte(
                cond_inicial_func=cond_func,
                esquema_func=esq_func,
                L=L, T_final=T_final, a=a, dx=DX, cfl=CFL
            )
            
            titulo = f"{esq_func.__name__} com {cond_func.__name__}"
            plot_utils.plot_transporte_snapshots(x, U_snaps, t_snaps, titulo)

    print("--- Parte 1 Concluída ---")

if __name__ == "__main__":
    executar_parte1()