# Visualizations/visualize_thermal.py

import matplotlib.pyplot as plt
import numpy as np

# --- Dados do Projeto (Resultados da Simulação) ---
temp_ambiente_externo = 80.0 # Temperatura em Celsius
temp_final_simulada = 3.28   # Temperatura final calculada
limite_maximo = 5.0          # Limite de segurança superior (°C)
limite_minimo = 0.0          # Limite de segurança inferior (°C)

# --- Configuração do Gráfico ---

plt.figure(figsize=(10, 6))

# 1. Cria a barra para a Temperatura Externa
plt.bar('Temperatura Externa', temp_ambiente_externo, color='#FF4500', label='Temperatura Externa')

# 2. Cria a barra para a Temperatura Final (bars aqui contém a última barra)
bars = plt.bar('Temperatura Final', temp_final_simulada, color='#1E90FF', label='Temperatura Final Simulada')

# 3. Desenha a faixa de segurança (área sombreada)
plt.axhspan(limite_minimo, limite_maximo, color='#32CD32', alpha=0.3, label='Faixa Criogênica Segura (0-5°C)')
plt.axhline(limite_maximo, color='#32CD32', linestyle='--', linewidth=1) 
plt.axhline(limite_minimo, color='#32CD32', linestyle='--', linewidth=1) 

# ADIÇÃO DE TEXTO CORRIGIDA: Usa bars[0] para a última barra criada
plt.text(bars[0].get_x() + bars[0].get_width() / 2, temp_final_simulada + 1, 
         f'{temp_final_simulada:.2f} °C', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.ylim(0, temp_ambiente_externo * 1.1)
plt.ylabel('Temperatura (°C)')
plt.title('Viabilidade de Isolamento Térmico Criogênico')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Salva o gráfico
plt.savefig('thermal_viability_chart.png') 
print("\nGráfico 'thermal_viability_chart.png' gerado com sucesso.")
