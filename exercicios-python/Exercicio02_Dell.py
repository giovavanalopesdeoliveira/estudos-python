# Geralmente, os logs são configurados para registrar as mensagens de maior gravidade. Em contrapartida, o modo debug é utilizado somente quando o programa apresenta falhas e é necessário fazer uma auditoria para encontrar o problema.
# A seguir, considere o caso descrito para resolver a questão.
# Imagine que você é o cientista de dados de uma grande empresa e, como um bom colaborador, decidiu analisar os dados de log de um programa essencial da empresa, com o intuito de avaliar como o programa se comportou durante um ano de funcionamento.
# Ao receber o arquivo de log, você percebeu que há dados de pelo menos um ano inteiro e que o arquivo possui 4 Gigabytes de tamanho. Então, você decidiu utilizar expressão regular para avaliar aquele comportamento.
# Para isso, você precisou construir um código que informasse a quantidade de erros ocorridos e quais os horários em que mais ocorrem erro. Estas informações serão uteis para lhe ajudar a investigar a causa do problema.

# Sabendo que o log possui uma formatação clara (Dia-Mês-Ano Hora:Minuto:Segundo:Milesimos_de_segundos | Nivel_de_gravidade -> Mensagem), utilize a string a seguir como exemplo para fazer o seu código. Ao final, envie seu código em Python, ou seja, um arquivo com a extensão ‘py’, para avaliarmos como você resolveu esse problema.

# 2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
# 2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
# 2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
# 2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
# 2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
# 2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
# 2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
# 2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
# 2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
# 2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
# 2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
# 2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
#2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida

# Estratégia de solução:
# Etapa	O que fazer
# 1.	Usar re.findall() para extrair todas as linhas com ERROR
# 2.	Extrair a data/hora de cada erro
# 3.	Contar os erros por hora (ou por dia/hora)
# 4.	Exibir os resultados


import re
from collections import Counter

# ============================================
# DADOS DE LOG (exemplo fornecido)
# ============================================

log_data = """2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida"""

# ============================================
# 1. CONTAGEM DE ERROS
# ============================================

# Padrão: captura linhas inteiras que contêm "ERROR" no campo de nível
# Uso do re.MULTILINE para que ^ e $ funcionem no início/fim de cada linha
padrao_error = r'^.*?\|\s*ERROR\s*->.*$'
erros = re.findall(padrao_error, log_data, re.MULTILINE)

# total_erros é usado para estatística básica; pode ser expandido depois
total_erros = len(erros)

print("=" * 60)
print("ANALISE DO ARQUIVO DE LOG")
print("=" * 60)
print(f"\nTotal de erros encontrados: {total_erros}")

# ============================================
# 2. EXTRAÇÃO DA HORA DE CADA ERRO
# ============================================

# Extraímos apenas a hora (HH) porque o requisito é "horários em que mais ocorrem erros"
# Caso no futuro precise de minuto ou segundo, basta ajustar o grupo de captura
horas_erros = []

for linha in erros:
    # O grupo (\d{2}) captura a hora; os dois pontos e os segundos são ignorados
    match = re.search(r'(\d{2}):\d{2}:\d{2}', linha)
    if match:
        horas_erros.append(match.group(1))

# ============================================
# 3. CONTAGEM DE ERROS POR HORA
# ============================================

# Counter é útil para contagens rápidas; poderia ser feito com dicionário manual
contador_horas = Counter(horas_erros)

print("\nHORARIOS COM MAIS OCORRENCIAS DE ERROS:")

if contador_horas:
    # most_common() já retorna ordenado do maior para o menor
    for hora, quantidade in contador_horas.most_common():
        print(f"   {hora}:00h -> {quantidade} erro(s)")
    
    # Isola o horário de pico para exibição destacada
    hora_mais_comum, qtd_mais_comum = contador_horas.most_common(1)[0]
    print(f"\nHorario com mais erros: {hora_mais_comum}:00h -> {qtd_mais_comum} erro(s)")
else:
    print("   Nenhum erro encontrado para analise.")

# ============================================
# 4. LISTA COMPLETA DOS ERROS (PARA AUDITORIA)
# ============================================

# Esta listagem é útil para debug e para validar se a extração foi correta
# Em um arquivo real de 4GB, esta listagem pode ser inviável; considerar remover em produção
print("\nLISTA COMPLETA DOS ERROS ENCONTRADOS:")
for i, erro in enumerate(erros, 1):
    print(f"   {i}. {erro}")

print("\n" + "=" * 60)
print("ANALISE CONCLUIDA")
print("=" * 60)



# Possível solução para realidade 
# import re
# from collections import Counter

Inicializa estruturas de dados
# contador_horas = Counter()
# total_erros = 0

Leitura linha por linha para não sobrecarregar memória (arquivo de 4GB)
# with open('log_empresa.txt', 'r', encoding='utf-8') as arquivo:
    # for linha in arquivo:
        Filtro rápido: só processa linhas com "ERROR"
        Isso é mais eficiente do que aplicar regex em todas as linhas
        # if 'ERROR' in linha:
            # total_erros += 1
            
            Extrai apenas a hora (HH) do timestamp
            Formato esperado: YYYY-MM-DD HH:MM:SS,mmm
            # match = re.search(r'(\d{2}):\d{2}:\d{2}', linha)
            # if match:
                # contador_horas[match.group(1)] += 1

Exibição dos resultados
# print(f"Total de erros: {total_erros}")
# print("Erros por hora:")
# for hora, qtd in contador_horas.most_common():
    # print(f"   {hora}:00h -> {qtd} erro(s)")