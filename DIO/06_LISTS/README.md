# Bootcamp Python Data Analytics: Trabalhando com Listas

Este módulo do Bootcamp, conduzido por Guilherme Artur de Carvalho (@decarvalhogui), foca no uso de listas em Python, uma das estruturas de dados mais versáteis e fundamentais na linguagem.

## Introdução às Listas

Listas em Python são coleções ordenadas e mutáveis que podem armazenar diferentes tipos de objetos. Elas são ideais para armazenar e manipular coleções de itens.

- **Criação de Listas**: Podem ser criadas usando colchetes `[]`, o construtor `list()`, ou a função `range()`.

### Exemplos Básicos de Criação de Listas
- `frutas = ["laranja", "maçã", "uva"]`
- `letras = list("python")`
- `numeros = list(range(10))`
- `carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]`

## Acessando Elementos da Lista

Os elementos das listas podem ser acessados utilizando índices, iniciando do zero.

### Exemplo de Acesso
- `frutas[0]` resulta em `"laranja"`
- `frutas[-1]` resulta em `"uva"`

## Listas Aninhadas

Listas podem conter outras listas, permitindo a criação de estruturas complexas como tabelas.

### Exemplo de Lista Aninhada
- `matriz = [[1, "a", 2], ["b", 3, 4], [6, 5, "c"]]`

## Fatiamento de Listas

O fatiamento permite extrair subconjuntos de uma lista, especificando os índices de início, fim e o passo.

### Exemplo de Fatiamento
- `lista = ["p", "y", "t", "h", "o", "n"]`
- `lista[1:3]` resulta em `["y", "t"]`

## Iteração e Enumerate em Listas

A iteração sobre listas é comumente feita usando loops `for`, e a função `enumerate` pode ser usada para obter índices.

### Exemplos de Iteração
- `for fruta in frutas: print(fruta)`
- `for indice, fruta in enumerate(frutas): print(f"{indice}: {fruta}")`

## Compreensão de Listas

A compreensão de listas é uma maneira concisa de criar novas listas a partir de listas existentes, aplicando filtros ou modificando seus elementos.

### Exemplo de Compreensão de Lista
- `pares = [n for n in numeros if n % 2 == 0]`

## Métodos da Classe Lista

As listas em Python possuem uma série de métodos úteis para manipulação e consulta dos seus elementos.

### Métodos Comuns de Lista
- **Adicionar Elementos**: `lista.append(elemento)` adiciona um elemento ao final da lista.
- **Limpar Lista**: `lista.clear()` remove todos os elementos da lista.
- **Copiar Lista**: `lista.copy()` cria uma cópia da lista.
- **Contar Elementos**: `lista.count(elemento)` conta quantas vezes um elemento aparece.
- **Estender Lista**: `lista.extend(outra_lista)` adiciona elementos de outra lista ao final.
- **Encontrar Índice**: `lista.index(elemento)` retorna o índice do primeiro elemento encontrado.
- **Remover e Retornar**: `lista.pop(indice)` remove e retorna o elemento no índice fornecido.
- **Remover Elemento**: `lista.remove(elemento)` remove a primeira ocorrência do elemento.
- **Reverter Lista**: `lista.reverse()` inverte a ordem dos elementos.
- **Ordenar Lista**: `lista.sort()` ordena os elementos da lista.

## Conclusão

Este módulo aborda os conceitos essenciais de listas em Python, proporcionando um entendimento abrangente de como criar, acessar, modificar e utilizar listas em diversos contextos.

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
