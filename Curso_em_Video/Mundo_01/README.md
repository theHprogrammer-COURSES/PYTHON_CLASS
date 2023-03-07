# Fundamentos do Python

## Aula 06: Tipos Primitivos e Saída de Dados 
### Tipos Primitivos
- int: números inteiros
- float: números reais
- bool: valores lógicos (True ou False)
- str: cadeia de caracteres (texto)

### Saída de Dados
- print(): imprime na tela o que está entre os parênteses
  - f strings: permite formatar strings de forma mais simples
    - Exemplo: print(f'Olá, {nome}!')
  - format(): permite formatar strings de forma mais simples
    - Exemplo: print('Olá, {}!'.format(nome))

### Verificando o tipo de uma variável
- type(): retorna o tipo da variável
  - Exemplo: type(nome)
- isinstance(): verifica se a variável é do tipo especificado
  - Exemplo: isinstance(nome, str)

## Aula 07: Operadores Aritméticos
### Operadores Aritméticos
- +: soma
- -: subtração
- *: multiplicação
- /: divisão
- **: potência
- //: divisão inteira
- %: resto da divisão

### Ordem de Precedência
- 1º: ()
- 2º: **
- 3º: * / // %
- 4º: + -

### Macetes
- Concatenação de strings: basta usar o operador +
  - Exemplo: print('Olá, ' + nome + '!')
- Multiplicação de strings: basta usar o operador *
  - Exemplo: print('-=' * 20)

## Aula 08: Módulos
### Módulos
- Módulos (bibliotecas) são arquivos .py que contém funções e classes 
- Para importar um módulo, basta usar a palavra reservada import
  - Exemplo: import math
- Para importar uma função específica de um módulo, basta usar a palavra reservada from
  - Exemplo: from math import sqrt
- Para importar todas as funções de um módulo, basta usar a palavra reservada from e o asterisco
  - Exemplo: from math import *

## Aula 09: Manipulação de Texto
### Cadeia de Caracteres (string)
- Uma string é uma sequência de caracteres
- Para criar uma string, basta colocar o texto entre aspas simples ou duplas
  - Exemplo: nome = 'Helder'

### Manipulação de Strings (Fatiamento)
- Para acessar um caractere específico de uma string, basta usar o índice do caractere
  - Exemplo: nome[0] retorna 'H'
- Para acessar um intervalo de caracteres de uma string, basta usar o índice inicial e o índice final
  - Exemplo: nome[0:3] retorna 'Hel'
- Podemos omitir o índice inicial ou o índice final
  - Exemplo: nome[:3] retorna 'Hel'
  - Exemplo: nome[3:] retorna 'der'
- Para acessar os caracteres de uma string de trás para frente, basta usar índices negativos
  - Exemplo: nome[-1] retorna 'r'
  - Exemplo: nome[-3:] retorna 'der'
- Pode-se passar um terceiro parâmetro no fatiamento, que é o passo
  - Exemplo: nome[0:5:2] retorna 'Hle'
  - Exemplo: nome[1:6:2] retorna 'eld'
  - Exemplo: nome[::2] retorna 'Hle'
  - Exemplo: nome[::-1] retorna 'redleH'

### Análise de Strings (len, count, find, in)
- len(): retorna o tamanho da string
  - Exemplo: len(nome) retorna 6
- count(): retorna o número de ocorrências de uma substring na string
  - Exemplo: nome.count('e') retorna 2
- find(): retorna o índice da primeira ocorrência de uma substring na string
  - Exemplo: nome.find('e') retorna 1
- in: verifica se uma substring está contida na string
  - Exemplo: 'e' in nome retorna True
- Esses métodos também podem ser usados com strings literais
  - Exemplo: 'Helder'.count('e') retorna 2
- O fatiamento também pode ser usado com os métodos
  - Exemplo: nome.count('e', 0, 3) retorna 1
- Quando o método não encontra a substring, retorna -1
  - Exemplo: nome.find('x') retorna -1

### Transformação de Strings (replace, upper, lower, capitalize, title, strip, junct)
- Strings são imutáveis, ou seja, não podem ser modificadas
- Para modificar uma string, é necessário criar uma nova string
- replace(): substitui uma substring por outra substring
  - Exemplo: nome.replace('H', 'J') retorna 'Jelder'
- upper(): converte todos os caracteres para maiúsculo
  - Exemplo: nome.upper() retorna 'HELDER'
- lower(): converte todos os caracteres para minúsculo
  - Exemplo: nome.lower() retorna 'helder'
- capitalize(): converte o primeiro caractere para maiúsculo
  - Exemplo: nome.capitalize() retorna 'Helder'
- title(): converte o primeiro caractere de cada palavra para maiúsculo
  - Exemplo: nome.title() retorna 'Helder'
- strip(): remove os espaços no início e no fim da string
  - Exemplo: nome.strip() retorna 'Helder'
  - rsstrip(): remove os espaços no fim da string
  - lstrip(): remove os espaços no início da string

### Divisão de Strings (split)
- split(): divide uma string em uma lista de substrings
  - Exemplo: nome.split() retorna ['Helder']
  - Exemplo: nome.split('e') retorna ['H', 'ld', 'r']

### Junção de Strings (join)
- join(): junta os elementos de uma lista em uma string
  - Exemplo: '-'.join(['Helder', 'Silva']) retorna 'Helder-Silva'

## Aula 10: Condições (if, else, elif)
### Condições
- if: se
- else: senão
- elif: senão se

### Operadores Relacionais
- ==: igual a
- !=: diferente de
- >: maior que
- <: menor que
- >=: maior ou igual a
- <=: menor ou igual a

### Operadores Lógicos
- and: e
- or: ou
- not: não
- in: está contido em
- not in: não está contido em

## Aula 11: Cores no terminal
### Padrão ANSI (escape sequence)
- Padrão ANSI é um padrão de escape sequence para formatar texto no terminal
- Exemplo: \033[0;33;44m onde:
  - \033 é o código de escape
  - 0 é o estilo (0 = none, 1 = bold, 4 = underline, 7 = negative)
  - 33 é a cor do texto (30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = ciano, 37 = cinza)
  - 44 é a cor do fundo (40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = roxo, 46 = ciano, 47 = cinza)
- Para aplicar o estilo, basta colocar o código de escape no início da string e o código de reset no final da string
  - Exemplo: print('\033[0;33;44mOlá, Mundo!\033[m')