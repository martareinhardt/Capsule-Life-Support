# g_force_calculator.py

# --- Parâmetros de Entrada ---
# Força G máxima de aceleração na cápsula (ex: 10g para 10 vezes a gravidade da Terra)
g_force_maxima = 10.0

# Redução percentual da Força G pela CAMADA DE PROTEÇÃO (Carbono-Graphene)
# O seu README diz: "Reduces 10g by 30%"
percentual_reducao_protecao = 0.30 

# Redução percentual da Força G pela CAMADA CRIOGÊNICA (perfluorocarbon fluid)
# O seu README diz: "Reduces 75% G"
percentual_reducao_criogenica = 0.75

# --- Cálculos ---

# 1. G-Force após a Camada de Proteção
g_force_apos_protecao = g_force_maxima * (1 - percentual_reducao_protecao)

# 2. G-Force após a Camada Criogênica (a criogênica reduz sobre o que SOBROU da proteção)
g_force_final_sentida = g_force_apos_protecao * (1 - percentual_reducao_criogenica)

# --- Exibir Resultados ---
print(f"--- Relatório de Força G para a Cápsula ---")
print(f"Força G Máxima de Aceleração (entrada): {g_force_maxima} G")
print(f"Redução pela Camada de Proteção: {percentual_reducao_protecao*100:.0f}%")
print(f"G-Force após a Camada de Proteção: {g_force_apos_protecao:.2f} G")
print(f"Redução pela Camada Criogênica: {percentual_reducao_criogenica*100:.0f}%")
print(f"======================================")
print(f"Força G FINAL sentida pelo astronauta: {g_force_final_sentida:.2f} G")

# Para sobrevivência, a Força G deve ser o menor possível, tipicamente < 5G
if g_force_final_sentida <= 5.0:
    print("\nSUCESSO: A G-Force final está dentro de limites toleráveis para o corpo humano.")
else:
    print("\nALERTA: A G-Force final pode ser perigosa para a sobrevivência a longo prazo.")
