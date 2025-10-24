# Simulations/g_force_calculator.py
#
# Calcula a Força G sentida por um astronauta dentro da Cápsula Multi-Camada
# e gera o gráfico de redução.

import matplotlib.pyplot as plt # Necessário para gráficos
import numpy as np # Necessário para cálculos (e usado por matplotlib)

# --- Parâmetros de Entrada (Configuráveis) ---
g_force_maxima = 10.0
percentual_reducao_protecao = 0.30 
percentual_reducao_criogenica = 0.75

# --- Cálculos ---
g_force_apos_protecao = g_force_maxima * (1 - percentual_reducao_protecao)
g_force_final_sentida = g_force_apos_protecao * (1 - percentual_reducao_criogenica)

# --- Exibir Resultados (Relatório de Engenharia) ---
print("--- Relatório de Simulação de Força G para a Cápsula ---")
print(f"Força G Máxima de Aceleração (entrada): {g_force_maxima:.2f} G")
print(f"G-Force após a Camada de Proteção: {g_force_apos_protecao:.2f} G")
print(f"Força G FINAL sentida pelo astronauta: {g_force_final_sentida:.2f} G")
print("======================================")

# Análise de Viabilidade (simplificada)
if g_force_final_sentida <= 5.0:
    print("\nVIABILIDADE: SUCESSO. G-Force final tolerável.")
else:
    print("\nVIABILIDADE: ALERTA.")

# --- Gerar Gráfico ---
niveis_g = [g_force_maxima, g_force_apos_protecao, g_force_final_sentida]
rotulos = ['G-Força Inicial (10G)', 'Após Proteção (30%)', 'G-Força Final (75%)']
cores = ['#FF4500', '#FFD700', '#32CD32'] # Vermelho, Amarelo, Verde
limite_toleravel = 5.0 # Linha de segurança

plt.figure(figsize=(10, 6))
plt.bar(rotulos, niveis_g, color=cores)

# Adiciona linha de limite
plt.axhline(limite_toleravel, color='#4682B4', linestyle='--', linewidth=1.5, label='Limite Tolerável (5G)')

plt.ylabel('Força G')
plt.title('Redução de Força G pela Cápsula Multi-Camada')
plt.legend()

# Adiciona o valor G em cima de cada barra
for i, v in enumerate(niveis_g):
    plt.text(i, v + 0.2, f'{v:.2f} G', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylim(0, g_force_maxima * 1.1)
plt.savefig('g_force_reduction_chart.png') 
print("\nGráfico 'g_force_reduction_chart.png' gerado com sucesso!")
