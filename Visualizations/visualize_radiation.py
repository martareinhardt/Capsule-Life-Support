# Simulations/visualize_radiation.py
#
# Gera o gráfico de barras comparando a dose de radiação inicial, final e o limite seguro.

import matplotlib.pyplot as plt
import numpy as np

# --- Dados do Projeto ---
dose_inicial = 500.0  # Dose esperada no espaço (mSv)
dose_final_absorvida = 47.50 # Dose final calculada (mSv)
limite_seguranca_nasa = 50.0  # Limite máximo seguro (mSv)

# --- Configuração do Gráfico ---

dados = [dose_inicial, dose_final_absorvida, limite_seguranca_nasa]
rotulos = ['Dose Externa', 'Dose Final (Cápsula)', 'Limite de Segurança']
cores = ['#FF4500', '#32CD32', '#4682B4'] # Vermelho, Verde, Azul

plt.figure(figsize=(10, 6))
bars = plt.bar(rotulos, dados, color=cores)

# Adiciona o Limite de Segurança como uma linha para referência visual
plt.axhline(limite_seguranca_nasa, color='#808080', linestyle='--', linewidth=1.5, label='Limite de Segurança (50 mSv)')

# Adiciona o valor mSv em cima de cada barra
for bar, valor in zip(bars, dados):
    plt.text(bar.get_x() + bar.get_width() / 2, valor + 10, f'{valor:.2f} mSv', 
             ha='center', va='bottom', fontsize=10)

plt.ylabel('Dose de Radiação (mSv)')
plt.title('Viabilidade de Proteção contra Radiação da Cápsula')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Salva o gráfico como imagem PNG na raiz do Actions
plt.savefig('radiation_viability_chart.png') 
print("\nGráfico 'radiation_viability_chart.png' gerado com sucesso!")
