import matplotlib.pyplot as plt
import numpy as np
import os # 1. Importar a biblioteca 'os'

# 2. Definir o caminho da pasta onde os gráficos serão salvos
# O caminho 'tp4/graficos' é relativo ao local de onde você roda o script (C:\EDN)
SAVE_DIR = os.path.join('tp4', 'graficos')

# 3. Criar a pasta, se ela não existir (o 'exist_ok=True' evita erros)
os.makedirs(SAVE_DIR, exist_ok=True)


def plot_transporte_snapshots(x, U_lista, t_lista, titulo):
    """
    Plota a solução u(x) em diferentes instantes de tempo.
    """
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    
    for i in range(len(t_lista)):
        ax.plot(x, U_lista[i], label=f't = {t_lista[i]:.2f}s')
            
    ax.set_title(titulo)
    ax.set_xlabel('x (espaço)')
    ax.set_ylabel('u(x,t)')
    ax.legend()
    ax.grid(True)
    
    # 4. Modificar o 'savefig' para usar o caminho completo
    save_name = f"tp4_transporte_{titulo.replace(' ', '_').lower()}.png"
    save_path = os.path.join(SAVE_DIR, save_name) # Junta 'tp4/graficos/' + 'nome_arquivo.png'
    
    plt.savefig(save_path)
    print(f"Gráfico de transporte salvo em {save_path}")
    plt.close(fig)

def plot_laplace_solucao(X, Y, U, titulo):
    """
    Plota a solução 2D u(x,y) da Eq. de Laplace.
    """
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111)
    
    contour = ax.contourf(X, Y, U, 50, cmap='viridis')
    ax.set_aspect('equal', 'box')
    ax.set_title(titulo)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.colorbar(contour, ax=ax, shrink=0.7)
    
    # 4. Modificar o 'savefig'
    save_name = f"tp4_laplace_{titulo.replace(' ', '_').lower()}.png"
    save_path = os.path.join(SAVE_DIR, save_name)
    
    plt.savefig(save_path)
    print(f"Gráfico de Laplace salvo em {save_path}")
    plt.close(fig)

def plot_convergencia_laplace(dx_lista, erro_lista):
    """
    Plota o erro em função de dx em escala log-log para achar a ordem.
    """
    dx_array = np.array(dx_lista)
    erro_array = np.array(erro_lista)
    
    coeffs = np.polyfit(np.log(dx_array), np.log(erro_array), 1)
    ordem_p = coeffs[0]
    
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    
    ax.plot(dx_array, erro_array, 'o-', label=f'Erro no centro (0.5, 0.5)')
    ax.plot(dx_array, np.exp(coeffs[1]) * (dx_array**ordem_p), 'r--', 
            label=f'Ajuste (ordem p = {ordem_p:.2f})')
            
    ax.set_title('Ordem de Convergência (Laplace)')
    ax.set_xlabel('$\Delta x = \Delta y$')
    ax.set_ylabel('Erro Absoluto')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True, which="both", ls="--")
    ax.legend()
    
    # 4. Modificar o 'savefig'
    save_name = "tp4_laplace_ordem_convergencia.png"
    save_path = os.path.join(SAVE_DIR, save_name)
    
    plt.savefig(save_path)
    print(f"Gráfico de convergência salvo em {save_path}")
    plt.close(fig)