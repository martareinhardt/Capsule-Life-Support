# thermal_simulator.py
#
# Simula a eficiência do isolamento térmico da camada criogênica.

# --- Parâmetros de Entrada (Configuráveis) ---
# Temperatura média do ambiente espacial (pode variar muito, usaremos um valor alto de 80°C)
temp_ambiente_externo = 80.0 # Temperatura em Celsius (Exemplo de ambiente muito quente)

# Temperatura alvo interna (média)
temp_alvo_interna = 2.5 # Média entre 0°C e 5°C

# Diferencial de temperatura que o isolamento precisa cobrir
delta_T_inicial = temp_ambiente_externo - temp_alvo_interna

# Eficiência do isolamento da camada criogênica (conforme o seu projeto)
# Seu README diz: "insulates 99% heat"
eficiencia_isolamento = 0.99 

# Limites de segurança do projeto (conforme o seu README)
limite_maximo = 5.0 # °C
limite_minimo = 0.0 # °C

# --- Cálculos ---

# 1. Calor que 'vaza' através do isolamento (1% do Delta T)
calor_que_vaza = delta_T_inicial * (1 - eficiencia_isolamento)

# 2. Temperatura Interna Final (em relação à temperatura alvo)
# Assumimos que a temperatura interna do sistema criogênico é ajustada, 
# mas o calor vazante representa o desvio em relação ao alvo.
temp_final_simulada = temp_alvo_interna + calor_que_vaza

# --- Exibir Resultados (Relatório Térmico) ---

print("--- Relatório de Simulação de Eficiência Térmica ---")
print(f"Temperatura Externa de Simulação: {temp_ambiente_externo:.1f} °C")
print(f"Temperatura Interna Alvo (Média): {temp_alvo_interna:.1f} °C")
print(f"Eficiência do Isolamento Criogênico: {eficiencia_isolamento*100:.0f}%")
print(f"Desvio de Temperatura (Vazamento de Calor): {calor_que_vaza:.2f} °C")
print(f"======================================")
print(f"Temperatura INTERNA Final Simulada: {temp_final_simulada:.2f} °C")
print(f"Faixa de Segurança do Projeto: {limite_minimo:.1f}°C a {limite_maximo:.1f}°C")
print(f"======================================")

# Análise de Viabilidade
if limite_minimo <= temp_final_simulada <= limite_maximo:
    print("\nVIABILIDADE: SUCESSO. A temperatura final simulada está dentro da faixa criogênica de segurança.")
else:
    print("\nVIABILIDADE: ALERTA! A temperatura final está fora do limite seguro. Aumente a eficiência de isolamento!")
  
