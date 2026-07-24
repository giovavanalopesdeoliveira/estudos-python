# Exercícios de Python e Machine Learning

Este diretório contém a resolução de exercícios práticos desenvolvidos durante os estudos de Python aplicados à Análise de Dados, Tratamento de Textos e RegEx.

---

## Exercício 01: Análise de Avaliações do Spotify

### Contexto
Análise de avaliações de músicas dos gêneros Rock e Pop. Cada usuário atribuiu uma nota de 0 a 5 estrelas.

### Dados de Entrada
* **Notas Rock:** `[5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]`
* **Notas Pop:** `[3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]`

### Objetivos e Conceitos Aplicados
1. **Classificação:** Mapear notas numéricas para categorias textuais usando `map()`.
2. **Busca de Medianas:** Verificar se existe alguma música mediana de Rock utilizando `filter()` / `any()`.
3. **Validação Global:** Verificar se todas as músicas de Pop são boas utilizando `all()`.
4. **Comparação:** Contar e comparar a quantidade de músicas boas entre os dois gêneros.

**Código-fonte:** [`Exercicio01_Dell.py`](./Exercicio01_Dell.py)

---

## Exercício 02: Análise de Logs com Expressões Regulares (RegEx)

### Contexto
Auditoria de um arquivo de log de grande escala (4 GB) para identificar falhas do sistema, contabilizar a quantidade total de erros do tipo `ERROR` e mapear os horários de maior incidência.

### Formato do Log
`Ano-Mês-Dia Hora:Minuto:Segundo,Ms | Nivel_de_gravidade -> Mensagem`

**Exemplo:**
```text
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado

Código-fonte: Exercicio02_Dell.py