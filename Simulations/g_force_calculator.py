# g_force_calculator.py
#
# Calcula a Força G sentida por um astronauta dentro da Cápsula Multi-Camada
# considerando as reduções de cada camada, conforme o projeto.

# --- Parâmetros de Entrada (Configuráveis) ---
# Força G máxima de aceleração na cápsula (10g conforme o projeto)
g_force_maxima = 10.0

# Redução percentual da Força G pela CAMADA DE PROTEÇÃO (Carbono-Graphene)
percentual_reducao_protecao = 0.30 

# Redução percentual da Força G pela CAMADA CRIOGÊNICA (perfluorocarbon fluid)
percentual_reducao_criogenica = 0.75

# --- Cálculos ---

# 1. G-Force após a Camada de Proteção
# A Força G é reduzida em 30% da original (10G * 0.70)
g_force_apos_protecao = g_force_maxima * (1 - percentual_reducao_protecao)

# 2. G-Force após a Camada Criogênica
# A Força G é reduzida em 75% do que SOBROU da primeira camada
g_force_final_sentida = g_force_apos_protecao * (1 - percentual_reducao_criogenica)

# --- Exibir Resultados (Relatório de Engenharia) ---

print("--- Relatório de Simulação de Força G para a Cápsula ---")
print(f"Força G Máxima de Aceleração (entrada): {g_force_maxima:.2f} G")
print(f"Redução da Camada de Proteção (30%): {percentual_reducao_protecao*100:.0f}%")
print(f"G-Force após a Camada de Proteção: {g_force_apos_protecao:.2f} G")
print(f"Redução da Camada Criogênica (75%): {percentual_reducao_criogenica*100:.0f}%")
print(f"======================================")
print(f"Força G FINAL sentida pelo astronauta: {g_force_final_sentida:.2f} G")
print(f"======================================")

# Análise de Viabilidade
if g_force_final_sentida <= 5.0:
    print("\nVIABILIDADE: SUCESSO. A G-Force final está dentro de limites toleráveis para o corpo humano.")
elif g_force_final_sentida <= 8.0:
    print("\nVIABILIDADE: ATENÇÃO. A G-Force final é alta, mas tolerável por curtos períodos. Requer monitoramento.")
else:
    print("\nVIABILIDADE: ALERTA. A G-Force final é perigosa para a sobrevivência a longo prazo. Requer revisão.")
