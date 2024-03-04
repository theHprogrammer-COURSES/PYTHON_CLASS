# Bootcamp Python Data Analytics: Tipos de Operadores

Este módulo do Bootcamp, guiado por Guilherme Artur de Carvalho (@decarvalhogui), se aprofunda nos operadores em Python, abrangendo desde operadores aritméticos até operadores de associação. Este módulo é crucial para entender como manipular dados e lógica em Python de forma eficaz.

## Operadores Aritméticos e Precedência

Os operadores aritméticos são fundamentais para realizar cálculos matemáticos em Python. Além de entender esses operadores, é crucial conhecer a precedência deles, que determina a ordem na qual as operações são realizadas em uma expressão.

### Tabela de Operadores Aritméticos

| Operador | Nome           | Descrição                         | Exemplo de Uso |
|----------|----------------|-----------------------------------|----------------|
| `+`      | Adição         | Soma dois valores                 | `3 + 2` resulta `5` |
| `-`      | Subtração      | Subtrai um valor de outro         | `5 - 2` resulta `3` |
| `*`      | Multiplicação  | Multiplica dois valores           | `3 * 2` resulta `6` |
| `/`      | Divisão        | Divide um valor pelo outro        | `6 / 2` resulta `3.0` |
| `//`     | Divisão Inteira| Divide e retorna a parte inteira  | `7 // 2` resulta `3` |
| `%`      | Módulo         | Retorna o resto de uma divisão    | `7 % 2` resulta `1` |
| `**`     | Exponenciação  | Eleva um número a uma potência    | `2 ** 3` resulta `8` |

### Precedência dos Operadores

A precedência de operadores em Python segue a ordem:

1. Parênteses: `( )`
2. Exponenciação: `**`
3. Multiplicação, Divisão, Divisão Inteira, e Módulo: `*`, `/`, `//`, `%`
4. Adição e Subtração: `+`, `-`

> OBS: A leitura é sempre feita da esquerda para a direita.

A precedência define como as expressões são avaliadas. Por exemplo, em `10 - 5 * 2`, a multiplicação é realizada primeiro, resultando em `0`.

## Operadores de Comparação

Os operadores de comparação são usados para comparar dois valores. Eles são fundamentais para a lógica de decisão em Python, permitindo construir expressões condicionais.

### Tabela de Operadores de Comparação

| Operador | Descrição                     | Exemplo de Uso            |
|----------|-------------------------------|---------------------------|
| `==`     | Igual a                       | `a == b` retorna `True` se `a` é igual a `b` |
| `!=`     | Diferente de                  | `a != b` retorna `True` se `a` é diferente de `b` |
| `>`      | Maior que                     | `a > b` retorna `True` se `a` é maior que `b` |
| `<`      | Menor que                     | `a < b` retorna `True` se `a` é menor que `b` |
| `>=`     | Maior ou igual a              | `a >= b` retorna `True` se `a` é maior ou igual a `b` |
| `<=`     | Menor ou igual a              | `a <= b` retorna `True` se `a` é menor ou igual a `b` |

Estes operadores são amplamente utilizados em estruturas de decisão como instruções `if`, `while` e em loops `for` para controlar o fluxo do programa.

## Operadores de Atribuição

Operadores de atribuição são usados para designar valores às variáveis. Além do operador básico de atribuição (`=`), Python oferece operadores de atribuição combinados que realizam uma operação e atribuição simultaneamente.

### Tabela de Operadores de Atribuição

| Operador | Descrição                           | Exemplo de Uso           |
|----------|-------------------------------------|--------------------------|
| `=`      | Atribuição simples                  | `x = 5`                  |
| `+=`     | Atribuição com adição               | `x += 3` (equivalente a `x = x + 3`) |
| `-=`     | Atribuição com subtração            | `x -= 2` (equivalente a `x = x - 2`) |
| `*=`     | Atribuição com multiplicação        | `x *= 3` (equivalente a `x = x * 3`) |
| `/=`     | Atribuição com divisão              | `x /= 4` (equivalente a `x = x / 4`) |
| `//=`    | Atribuição com divisão inteira      | `x //= 2` (equivalente a `x = x // 2`) |
| `%=`     | Atribuição com módulo               | `x %= 7` (equivalente a `x = x % 7`) |
| `**=`    | Atribuição com exponenciação        | `x **= 3` (equivalente a `x = x ** 3`) |

Esses operadores proporcionam uma forma concisa de atualizar o valor de uma variável com base em sua valor atual, sendo muito úteis para operações matemáticas e lógicas frequentes em programação.

## Operadores Lógicos

Os operadores lógicos são usados para combinar expressões booleanas em Python. Eles são cruciais para construir condições complexas em estruturas de controle, como `if`, `while` e `for`.

### Principais Operadores Lógicos

| Operador | Descrição                                                  | Exemplo de Uso          |
|----------|------------------------------------------------------------|-------------------------|
| `and`    | Retorna `True` se ambas as expressões forem verdadeiras    | `x > 5 and x < 10`      |
| `or`     | Retorna `True` se pelo menos uma das expressões for verdadeira | `x < 5 or x > 10`      |
| `not`    | Inverte o valor booleano da expressão                      | `not(x > 5 and x < 10)` |

### Utilização e Exemplos

- **`and`**: Usado quando todas as condições devem ser verdadeiras para que o resultado final seja verdadeiro.
- **`or`**: Utilizado quando pelo menos uma das condições deve ser verdadeira para o resultado final ser verdadeiro.
- **`not`**: Serve para inverter o resultado de uma expressão lógica.

### Precedência dos Operadores Lógicos

A precedência dos operadores lógicos, do mais alto para o mais baixo, é: `not`, `and`, `or`. Parênteses podem ser usados para alterar a ordem de avaliação.

## Operadores de Identidade

Os operadores de identidade em Python são usados para determinar se duas variáveis se referem ao mesmo objeto na memória. Eles são particularmente úteis em situações onde a comparação de identidade é mais relevante do que a comparação de igualdade de valores.

### Principais Operadores de Identidade

| Operador | Descrição                                                   | Exemplo de Uso            |
|----------|-------------------------------------------------------------|---------------------------|
| `is`     | Retorna `True` se ambas as variáveis se referem ao mesmo objeto | `a is b`                  |
| `is not` | Retorna `True` se as variáveis se referem a objetos diferentes  | `a is not b`              |

### Exemplos Práticos

- `a = 3`
- `b = 3`
- `a is b` retorna `True`, pois `a` e `b` referem-se ao mesmo objeto inteiro na memória.
- `list1 = []`
- `list2 = []`
- `list1 is list2` retorna `False`, mesmo que `list1` e `list2` sejam iguais, eles são objetos distintos na memória.

Os operadores de identidade são especialmente importantes em Python devido ao seu modelo de gestão de memória e a maneira como trata objetos imutáveis e mutáveis.

## Operadores de Associação

Os operadores de associação em Python são usados para testar se um valor ou variável está presente em uma sequência, como uma string, lista ou tupla.

### Principais Operadores de Associação

| Operador | Descrição                                  | Exemplo de Uso            |
|----------|--------------------------------------------|---------------------------|
| `in`     | Retorna `True` se o valor está na sequência | `x in [1, 2, 3]` retorna `True` se `x` é um dos elementos da lista |
| `not in` | Retorna `True` se o valor não está na sequência | `x not in [1, 2, 3]` retorna `True` se `x` não é um dos elementos da lista |

### Exemplos Práticos

- Checar se um item está presente em uma lista: `if 'maçã' in frutas:`
- Verificar se uma chave está em um dicionário: `if 'nome' in dados_usuario:`
- Testar a presença de um caractere ou substring em uma string: `if 'a' in 'banana':`

Os operadores de associação são simples, mas poderosos, e são frequentemente utilizados em condicionais e loops para tomar decisões baseadas na presença de elementos em sequências.

## 👨‍💻 Author

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>
