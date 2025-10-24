# Visualizations/visualize_gforce.py

import matplotlib.pyplot as plt
import numpy as np

# --- Dados do Projeto (Resultados da Simulação) ---
g_force_maxima = 10.0
g_force_apos_protecao = 7.00 
g_force_final_sentida = 1.75
limite_toleravel = 5.0 # Linha de segurança para viabilidade

# --- Configuração do Gráfico ---
niveis_g = [g_force_maxima, g_force_apos_protecao, g_force_final_sentida]
rotulos = ['G-Força Inicial (10G)', 'Após Proteção', 'G-Força Final']
cores = ['#FF4500', '#FFD700', '#32CD32'] # Vermelho, Amarelo, Verde

plt.figure(figsize=(10, 6))
plt.bar(rotulos, niveis_g, color=cores)

# Adiciona linha de limite
plt.axhline(limite_toleravel, color='#4682B4', linestyle='--', linewidth=1.5, label='Limite Tolerável (5G)')

plt.ylabel('Força G')
plt.title('Viabilidade de Redução de Força G pela Cápsula')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adiciona o valor G em cima de cada barra
for i, v in enumerate(niveis_g):
    plt.text(i, v + 0.2, f'{v:.2f} G', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylim(0, g_force_maxima * 1.1)
# Salva o gráfico
plt.savefig('g_force_reduction_chart.png') 
print("\nGráfico 'g_force_reduction_chart.png' gerado com sucesso!")
