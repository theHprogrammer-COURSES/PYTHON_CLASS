# Bootcamp Python Data Analytics: Dominando Dicionários em Python

Neste módulo, conduzido por Guilherme Artur de Carvalho (@decarvalhogui), exploramos dicionários em Python, uma estrutura de dados versátil e essencial para armazenar e organizar dados de forma eficiente.

## Introdução aos Dicionários

Dicionários são estruturas de dados em Python que armazenam pares de chave-valor. São coleções desordenadas, mas podem ser ordenadas pela chave se necessário.

- **Criação de Dicionários**: Podem ser criados com chaves `{}` ou com a função `dict()`.
- **Exemplo**:
  - `pessoa = {"nome": "Guilherme", "idade": 28}`
  - `dados = dict(nome="Guilherme", idade=28)`

## Acessando e Modificando Dicionários

Os valores dos dicionários são acessados e modificados usando suas chaves.

- **Acesso aos Dados**: Acessa-se um valor através de sua chave usando a sintaxe `dicionario[chave]`.
- **Modificação de Dados**: Atualiza-se um valor atribuindo um novo valor à sua chave.
- **Exemplo**:
  - `pessoa["idade"] = 30` atualiza a idade da pessoa para 30.

## Dicionários Aninhados

Dicionários podem conter outros dicionários, permitindo a criação de estruturas de dados complexas.

- **Exemplo de Dicionário Aninhado**:
  - `contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}`

## Iterando sobre Dicionários

A iteração sobre dicionários pode ser feita de diversas formas, incluindo percorrer chaves, valores ou pares chave-valor.

- **Iteração Sobre Chaves**: `for chave in dicionario:`
- **Iteração Sobre Valores**: `for valor in dicionario.values():`
- **Iteração Sobre Itens**: `for chave, valor in dicionario.items():`

## Métodos Comuns em Dicionários

Dicionários possuem vários métodos úteis para manipulação de dados.

- **`.clear()`**: Limpa todos os itens do dicionário.
- **`.copy()`**: Retorna uma cópia do dicionário.
- **`.fromkeys()`**: Cria um novo dicionário com chaves especificadas.
- **`.get()`**: Retorna o valor para uma chave especificada, evitando erros se a chave não existir.
- **`.items()`**: Retorna uma visualização dos pares chave-valor.
- **`.keys()`**: Retorna uma visualização das chaves.
- **`.pop()`**: Remove o item com a chave especificada e retorna seu valor.
- **`.popitem()`**: Remove e retorna um par chave-valor.
- **`.setdefault()`**: Retorna o valor de uma chave, definindo um valor padrão se ela não existir.
- **`.update()`**: Atualiza o dicionário com elementos de outro dicionário.
- **`.values()`**: Retorna uma visualização dos valores.

## Conclusão

Este módulo fornece uma compreensão profunda dos dicionários em Python, abordando sua criação, manipulação e técnicas para lidar com estruturas de dados complexas. Compreender dicionários é vital para qualquer desenvolvedor Python, dada a sua flexibilidade e utilidade em diversos cenários de programação.

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
