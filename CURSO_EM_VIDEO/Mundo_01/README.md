# Mundo 01: Fundamentos do Python com Gustavo Guanabara

## Aula 06: Tipos Primitivos e Saída de Dados

### Tipos Primitivos

| Tipo  | Descrição                     |
|-------|-------------------------------|
| int   | Números inteiros              |
| float | Números reais                 |
| bool  | Valores lógicos (True, False) |
| str   | Cadeia de caracteres (texto)  |

### Saída de Dados

- **print()**: Imprime na tela o conteúdo entre parênteses.
  - **f strings**: Formatação simplificada de strings.
    - Exemplo: `print(f'Olá, {nome}!')`
  - **format()**: Outra maneira de formatar strings.
    - Exemplo: `print('Olá, {}!'.format(nome))`

### Verificando o Tipo de uma Variável

- **type()**: Retorna o tipo da variável.
  - Exemplo: `type(nome)`
- **isinstance()**: Verifica se a variável é de um tipo especificado.
  - Exemplo: `isinstance(nome, str)`

## Aula 07: Operadores Aritméticos

### Operadores Aritméticos

| Operador | Descrição        |
|----------|------------------|
| +        | Soma             |
| -        | Subtração        |
| *        | Multiplicação    |
| /        | Divisão          |
| **       | Potência         |
| //       | Divisão inteira  |
| %        | Resto da divisão |

### Ordem de Precedência

1. Parênteses `()`
2. Potência `**`
3. Multiplicação, divisão, divisão inteira, e resto da divisão `* / // %`
4. Soma e subtração `+ -`

### Macetes

- Concatenação de strings: Usar o operador `+`.
  - Exemplo: `print('Olá, ' + nome + '!')`
- Multiplicação de strings: Usar o operador `*`.
  - Exemplo: `print('-=' * 20)`

## Aula 08: Módulos

### Módulos

Módulos (ou bibliotecas) são arquivos `.py` contendo funções e classes. Para utilizá-los:

- **import**: Importa um módulo inteiro.
  - Exemplo: `import math`
- **from**: Importa uma função específica de um módulo.
  - Exemplo: `from math import sqrt`
- **from** e **\***: Importa todas as funções de um módulo.
  - Exemplo: `from math import *`

## Aula 09: Manipulação de Texto

### Cadeia de Caracteres (string)

- Uma string é uma sequência de caracteres. Para criá-la, use aspas simples ou duplas.
  - Exemplo: `nome = 'Helder'`

### Manipulação de Strings (Fatiamento)

| Ação             | Exemplo                | Resultado |
|------------------|------------------------|-----------|
| Acesso direto    | `nome[0]`              | 'H'       |
| Intervalo        | `nome[0:3]`            | 'Hel'     |
| Índice inicial   | `nome[:3]`             | 'Hel'     |
| Índice final     | `nome[3:]`             | 'der'     |
| Índices negativos| `nome[-1]`             | 'r'       |
| Passo            | `nome[0:5:2]`          | 'Hle'     |
| Inversão         | `nome[::-1]`           | 'redleH'  |

### Análise de Strings

| Método  | Descrição                            | Exemplo             | Resultado |
|---------|--------------------------------------|---------------------|-----------|
| len()   | Tamanho da string                    | `len(nome)`         | 6         |
| count() | Ocorrências de substring             | `nome.count('e')`   | 2         |
| find()  | Índice da primeira ocorrência        | `nome.find('e')`    | 1         |
| in      | Verifica se substring está contida   | `'e' in nome`       | True	   |

### Transformação de Strings

- **replace()**: Substitui partes da string.
- **upper()**: Converte para maiúsculo.
- **lower()**: Converte para minúsculo.
- **capitalize()**: Primeira letra maiúscula.
- **title()**: Primeira letra de cada palavra maiúscula.
- **strip(), rstrip(), lstrip()**: Remove espaços. (início e fim; fim; início respectivamete)

### Divisão e Junção de Strings

- **split()**: Divide uma string em uma lista.
  - Exemplo: `nome.split('e')` retorna `['H', 'ld', 'r']`
- **join()**: Junta elementos de uma lista em uma string.
  - Exemplo: `'-'.join(['Helder', 'Silva'])` retorna 'Helder-Silva'

## Aula 10: Condições (if, else, elif)

### Condições

| Condição | Descrição   |
|----------|-------------|
| if       | Se          |
| else     | Senão       |
| elif     | Senão se    |

### Operadores Relacionais

| Operador | Descrição      |
|----------|----------------|
| ==       | Igual a        |
| !=       | Diferente de   |
| >        | Maior que      |
| <        | Menor que      |
| >=       | Maior ou igual |
| <=       | Menor ou igual |

### Operadores Lógicos

| Operador | Descrição          |
|----------|--------------------|
| and      | E                  |
| or       | Ou                 |
| not      | Não                |
| in       | Está contido em    |
| not in   | Não está contido em|

## Aula 11: Cores no Terminal

### Padrão ANSI (Escape Sequence)

Para colorir textos no terminal, usa-se o padrão ANSI.
Para aplicar, coloque o código de escape no início e o código de reset (`\033[m`) no final da string.
- Exemplo: `\033[0;33;44mOlá, Mundo!\033[m`

### Códigos ANSI para Estilo de Texto, Cor do Texto e Cor de Fundo

| Código | Significado      | Estilo/Cor            |
|--------|------------------|-----------------------|
| 0      | Estilo           | Nenhum (none)         |
| 1      | Estilo           | Negrito (bold)        |
| 4      | Estilo           | Sublinhado (underline)|
| 7      | Estilo           | Invertido (negative)  |
| 30     | Cor do Texto     | Branco                |
| 31     | Cor do Texto     | Vermelho              |
| 32     | Cor do Texto     | Verde                 |
| 33     | Cor do Texto     | Amarelo               |
| 34     | Cor do Texto     | Azul                  |
| 35     | Cor do Texto     | Roxo                  |
| 36     | Cor do Texto     | Ciano                 |
| 37     | Cor do Texto     | Cinza                 |
| 40     | Cor de Fundo     | Branco                |
| 41     | Cor de Fundo     | Vermelho              |
| 42     | Cor de Fundo     | Verde                 |
| 43     | Cor de Fundo     | Amarelo               |
| 44     | Cor de Fundo     | Azul                  |
| 45     | Cor de Fundo     | Roxo                  |
| 46     | Cor de Fundo     | Ciano                 |
| 47     | Cor de Fundo     | Cinza                 |


