
# Fundamentos de Python para Machine Learning

Este documento reúne todos os conceitos fundamentais de Python vistos durante o curso, com foco em Programação Funcional, Expressões Regulares, Estruturas de Dados e Boas Práticas.

---

## 1. Programação Funcional

A Programação Funcional é um paradigma que trata a computação como a avaliação de funções matemáticas, evitando estado mutável e efeitos colaterais.

### 1.1 Funções Puras

Uma função é considerada pura quando:
* Para os mesmos argumentos de entrada, produz sempre o mesmo resultado.
* Não causa efeitos colaterais (não altera variáveis externas, não faz I/O, etc.).

**Exemplo (Função pura):**
```python
# Função pura
def soma(a, b):
    return a + b

print(soma(2, 3))  # 5
print(soma(2, 3))  # 5 (sempre o mesmo)

Exemplo (Função impura com efeito colateral):

contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

print(incrementar())  # 1
print(incrementar())  # 2 (resultado muda)

1.2 Funções Anônimas (lambda)
Funções sem nome, definidas em uma única linha. São usadas para tarefas simples e descartáveis.

Sintaxe:

lambda argumentos: expressão

**Exemplo**
# Função lambda que dobra um número
dobrar = lambda x: x * 2
print(dobrar(5))  # 10


1.3 Função map()
Aplica uma função a cada elemento de um iterável (lista, tupla, etc.) e retorna um novo iterável com os resultados.

Sintaxe:

map(funcao, iteravel)
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]

1.4 Função filter()
Filtra elementos de um iterável com base em uma condição (função que retorna True ou False). Retorna apenas os elementos que atendem à condição.

Sintaxe:

filter(funcao_booleana, iteravel)

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

1.5 Função any()
Retorna True se pelo menos um elemento do iterável for verdadeiro.

Exemplo:
numeros = [1, 2, 3, 4]
existe_maior_que_3 = any(map(lambda x: x > 3, numeros))
print(existe_maior_que_3)  # True
