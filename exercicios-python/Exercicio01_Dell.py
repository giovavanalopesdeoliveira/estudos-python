
#RESUMO DO PROBLEMA — ANÁLISE DE AVALIAÇÕES DO SPOTIFY
# Contexto: Você é programador Python do Spotify e precisa analisar avaliações de músicas dos gêneros Rock e Pop.
# Dados: Cada usuário deu uma nota de 0 a 5 estrelas para cada música.
# Notas fornecidas:
# notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
# notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]
# Classificação das notas em categorias:
# 0 a 1 estrela = Ruim
# 2 a 3 estrelas = Mediana
# 4 a 5 estrelas = Boa
# Perguntas do chefe:
# a) Quantas músicas ruins, medianas e boas existem em cada gênero (Rock e Pop)?
# b) Existe alguma música mediana no Rock?
# c) Todas as músicas de Pop são boas?
# d) Qual gênero teve mais músicas boas?
#Objetivos
# 1)Classificar notas em categorias e contar;
# 2)Verificar se há pelo menos uma nota 2 ou 3 no Rock;
# 3)Verificar se todas as notas do Pop são 4 ou 5;
# 4)Comparar a quantidade de notas 4 e 5 em cada gênero;
# Usar conceitos:
# 1)  map() [nota numérica para sua categoria textual ('ruim', 'mediana', 'boa');
# 2) filter() / any()	Verifica se existe alguma música mediana de Rock;
# 3) all()	Verifica se todas as músicas de Pop são boas;

#Conceitos visto na aula:
#PROGRAMAÇÃO FUNCIONAL
#│
#├── Funções Puras (mesma entrada → mesma saída, sem efeitos colaterais)
#│
#├── Funções Anônimas (lambda)
#│
#├── Funções de Alta Ordem
#│   ├── map → transforma todos
#│   ├── filter → seleciona alguns
#│   ├── any → pelo menos um True
#│   └── all → todos True
#│
#└── Composição de funções (funções pequenas combinadas)


# Lambda Funções anônimas puras

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop  = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]
# ---------- FUNÇÕES PURAS ----------

classificar = lambda nota: 'ruim'    if nota <= 1 else \
                           'mediana' if nota <= 3 else \
                           'boa'

is_ruim    = lambda c: c == 'ruim'
is_mediana = lambda c: c == 'mediana'
is_boa     = lambda c: c == 'boa'

# def nome_da_funcao(parametros):
    #bloco de código
    # return resultado
    
    # Funções auxiliares (puras)
def contar_categoria(categoria, notas):
    return len(list(filter(lambda x: classificar(x) == categoria, notas)))

def total_boas(notas):
    return len(list(filter(lambda x: x >= 4, notas)))

# Respostas funcionais
boas_rock = total_boas(notas_rock)
boas_pop = total_boas(notas_pop)

# Resultados
print("=" * 50)
print("RESULTADOS - VERSÃO FUNCIONAL")
print("=" * 50)

print("\n ROCK:")
print(f"   Ruins: {contar_categoria('ruim', notas_rock)}")
print(f"   Medianas: {contar_categoria('mediana', notas_rock)}")
print(f"   Boas: {boas_rock}")

print("\n POP:")
print(f"   Ruins: {contar_categoria('ruim', notas_pop)}")
print(f"   Medianas: {contar_categoria('mediana', notas_pop)}")
print(f"   Boas: {boas_pop}")

print("\n PERGUNTAS DO CHEFE (funcional):")
print(f"1. Existe música mediana no Rock? {any(map(lambda x: 2 <= x <= 3, notas_rock))}")
print(f"2. Todas as músicas de Pop são boas? {all(map(lambda x: x >= 4, notas_pop))}")

print("\n MAIOR QUANTIDADE DE MÚSICAS BOAS:")
# Usando expressão ternária (funcional)
resultado = " ROCK" if boas_rock > boas_pop else "🎤 POP" if boas_pop > boas_rock else "EMPATE"
print(f"   {resultado} venceu!")














