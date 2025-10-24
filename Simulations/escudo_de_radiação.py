# radiation_shield.py

# --- Parâmetros de Entrada (Configuráveis) ---
# Dose de radiação espacial esperada (ex: em viagem a Marte, 500 mSv)
dose_inicial_mSv = 500.0 

# Eficiência da Deflexão da Camada de Proteção (conforme o seu projeto)
# O seu README diz: "deflects 90% radiation"
eficiencia_deflexao = 0.90 

# Fator de atenuação dos fluidos criogênicos e outros materiais internos
# (Estimativa: os fluidos podem absorver 5% do que sobra)
fator_absorcao_interna = 0.05 

# Limite de segurança anual de radiação da NASA para o corpo humano (mSv)
limite_seguranca = 50.0 

# --- Cálculos ---

# 1. Radiação que passa pela Camada de Proteção
radiacao_que_passa_pela_protecao = dose_inicial_mSv * (1 - eficiencia_deflexao)

# 2. Radiação absorvida internamente
radiacao_absorvida = radiacao_que_passa_pela_protecao * (1 - fator_absorcao_interna)

# Dose FINAL que atinge o astronauta
dose_final_mSv = radiacao_absorvida

# --- Exibir Resultados (Relatório de Radiação) ---

print("--- Relatório de Simulação de Proteção contra Radiação ---")
print(f"Dose Inicial Esperada no Espaço: {dose_inicial_mSv:.2f} mSv")
print(f"Eficiência da Deflexão da Camada Externa: {eficiencia_deflexao*100:.0f}%")
print(f"Radiação após Camada Externa: {radiacao_que_passa_pela_protecao:.2f} mSv")
print(f"Fator de Absorção Interna Adicional: {fator_absorcao_interna*100:.0f}%")
print(f"======================================")
print(f"Dose FINAL no Astronauta: {dose_final_mSv:.2f} mSv")
print(f"Limite de Segurança da Missão (NASA): {limite_seguranca:.2f} mSv")
print(f"======================================")

# Análise de Viabilidade
if dose_final_mSv <= limite_seguranca:
    print("\nVIABILIDADE: SUCESSO. A dose de radiação absorvida está abaixo do limite de segurança.")
else:
    print("\nVIABILIDADE: ALERTA! A dose de radiação excede o limite seguro. Aumente a eficiência da deflexão!")
  
