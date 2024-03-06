# Bootcamp Python Data Analytics: Dominando Conjuntos em Python

Este módulo do Bootcamp, guiado por Guilherme Artur de Carvalho (@decarvalhogui), explora os conjuntos em Python, uma estrutura de dados essencial para representar coleções únicas e realizar operações de conjuntos matemáticos.

## Introdução aos Conjuntos

Conjuntos (sets) em Python são coleções desordenadas de elementos únicos, ideais para operações matemáticas de conjuntos e eliminação de duplicatas.

- **Criação de Conjuntos**: Utilize chaves `{}` ou a função `set()` para criar conjuntos.
- **Características Únicas**: Conjuntos não suportam indexação e fatiamento. Para acessar os valores, é necessário convertê-los para uma lista.

### Exemplos de Criação de Conjuntos
- `numeros = {1, 2, 3, 4}`
- `letras = set("abacaxi")` resulta em `{'a', 'b', 'c', 'x', 'i'}`

## Operações em Conjuntos

Os conjuntos em Python suportam várias operações que refletem a teoria dos conjuntos matemáticos.

### Métodos e Operações Comuns
- **União (`union`)**: Combina dois conjuntos sem duplicatas.
- **Interseção (`intersection`)**: Retorna os elementos comuns entre dois conjuntos.
- **Diferença (`difference`)**: Retorna os elementos que estão em um conjunto, mas não no outro.
- **Diferença Simétrica (`symmetric_difference`)**: Retorna elementos que estão em um dos conjuntos, mas não em ambos.
- **Subconjunto (`issubset`)**: Verifica se um conjunto é subconjunto de outro.
- **Superconjunto (`issuperset`)**: Verifica se um conjunto é superconjunto de outro.
- **Disjuntos (`isdisjoint`)**: Verifica se dois conjuntos são disjuntos, ou seja, não têm elementos em comum.

### Exemplos Práticos
- `conjuntoA = {1, 2, 3}`
- `conjuntoB = {3, 4, 5}`
- `conjuntoA.union(conjuntoB)` resulta em `{1, 2, 3, 4, 5}`
- `conjuntoA.intersection(conjuntoB)` resulta em `{3}`

## Métodos Específicos de Conjuntos

Além das operações matemáticas, os conjuntos em Python oferecem métodos para manipulação.

- **Adicionar Elementos (`add`)**: Adiciona um elemento ao conjunto.
- **Remover Elementos (`remove`, `discard`)**: Remove um elemento específico do conjunto.
- **Limpar Conjunto (`clear`)**: Remove todos os elementos do conjunto.
- **Copiar Conjunto (`copy`)**: Cria uma cópia do conjunto.

## Iteração em Conjuntos

- **Iteração Simples**: Use um loop `for` para iterar sobre os elementos de um conjunto.
- **Enumerate**: A função `enumerate` pode ser usada para obter índices durante a iteração.

### Exemplo de Iteração
- `for elemento in conjuntoA: print(elemento)`

## Conclusão

Os conjuntos em Python são ferramentas poderosas e versáteis para a manipulação de coleções de elementos únicos, oferecendo uma ampla gama de operações matemáticas e métodos para gestão de dados.

## 👨‍💻 Author

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="H
 

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
