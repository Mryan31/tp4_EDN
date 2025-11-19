from .p1_transporte import run_transporte
from .p2_laplace import run_laplace

def executar_tp4_completo():
    print("============================================")
    print("   INICIANDO TRABALHO PRÁTICO 4 (EDN)   ")
    print("============================================")
    
    run_transporte.executar_parte1()
    
    run_laplace.executar_parte2()
    
    print("\n============================================")
    print("     TRABALHO PRÁTICO 4 FINALIZADO     ")
    print("============================================")
    print("Verifique os arquivos .png gerados no diretório.")

if __name__ == "__main__":
    executar_tp4_completo()