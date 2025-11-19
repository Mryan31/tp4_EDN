# 🧮 TP4 – Equações Diferenciais Numéricas  
### 🚀 UFMG – Trabalho Prático 4  
**Autor:** Mateus Ryan de Castro Lima  
**Repositório:** https://github.com/Mryan31/tp4_EDN  

---

## 📘 Descrição Geral

Este repositório contém a implementação e análise numérica de duas Equações Diferenciais Parciais fundamentais:

### **1️⃣ Equação do Transporte 1D**
- Implementação dos esquemas:
  - 🔹 Upwind (1ª ordem)  
  - 🔹 Lax–Friedrichs (1ª ordem)  
  - 🔹 Lax–Wendroff (2ª ordem)
- Análise de estabilidade e condição CFL  
- Comportamento para:
  - ✔️ Dados suaves (Gaussiana)  
  - ✔️ Dados descontínuos (onda quadrada)
- Geração automática de gráficos para cada esquema

### **2️⃣ Equação de Laplace no Quadrado**
- Solver numérico por Gauss–Seidel usando o esquema de 5 pontos  
- Comparação com solução analítica fechada  
- Cálculo da ordem de convergência  
- Plotagem da solução numérica, analítica e da curva log–log de erro  

---

## 📂 Estrutura do Projeto

```
tp4_EDN/
│
├── tp4_codigo.py               # Código principal (Transporte + Laplace)
│
├── tp4_output/
│   └── graficos/               # Figuras geradas automaticamente
│
├── Relatorio_Final.pdf
│
└── README.md                   # Este arquivo
```

---

## 🛠️ Requisitos

- Python 3.x  
- Bibliotecas:
  - `numpy`
  - `matplotlib`

Instale via:

```bash
pip install numpy matplotlib
```

---

## ▶️ Como Executar

Na raiz do projeto, rode:

```bash
python tp4_codigo.py
```

Após a execução, os gráficos estarão disponíveis em:

```
tp4_output/graficos/
```

---

## 📊 Gráficos Gerados

### Transporte:
- `transporte_esquema_upwind-<condicao>.png`
- `transporte_esquema_lax_friedrichs-<condicao>.png`
- `transporte_esquema_lax_wendroff-<condicao>.png`

### Laplace:
- `laplace_solucao_numerica_final.png`
- `laplace_solucao_analitica.png`
- `laplace_ordem_convergencia.png`

---

## 📐 Detalhes de Implementação

### ✨ Equação do Transporte
- Fronteiras periódicas implementadas
- Simulador modular reutilizável
- Snapshots registrados ao longo do tempo
- Código organizado por função e estilo claro

### ✨ Equação de Laplace
- Método iterativo de Gauss–Seidel
- Convergência monitorada por erro máximo
- Cálculo automático da ordem por ajuste log–log
- Uso da solução analítica:
  \[
    u(x,y) = rac{\sin(\pi x)\sinh(\pi(1-y))}{\sinh(\pi)}
  \]

---

## 📈 Ordem de Convergência Obtida

| Δx       | Erro Absoluto |
|----------|---------------|
| 0.5000   | 9.90e-03      |
| 0.2500   | 2.53e-03      |
| 0.1250   | 6.38e-04      |
| 0.0625   | 1.60e-04      |

A ordem estimada numérica é aproximadamente **2**, como esperado do método de 5 pontos.

---

## 📚 Relatório em LaTeX

A documentação completa (com gráficos, teoria e código) está em:

```
relatorio/TP4_FINAL.tex
```

---

## 📬 Contato

Dúvidas ou sugestões?  
Abra uma issue no GitHub:  
👉 https://github.com/Mryan31/tp4_EDN/issues

---

## ⭐ Créditos

Trabalho desenvolvido como parte da disciplina  
**Equações Diferenciais Numéricas – UFMG, 2025.**

---
