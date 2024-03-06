# Bootcamp Python Data Analytics: Trabalhando com Tuplas

Neste módulo do Bootcamp, orientado por Guilherme Artur de Carvalho (@decarvalhogui), exploramos as tuplas em Python, uma estrutura de dados importante e imutável.

## Introdução às Tuplas

As tuplas são sequências ordenadas e imutáveis em Python. São similares às listas, mas uma vez criadas, seus elementos não podem ser modificados.

- **Criação de Tuplas**: Podem ser criadas usando parênteses `()` ou simplesmente separando os elementos por vírgulas.

### Exemplos de Criação de Tuplas
- `cores = ("vermelho", "azul", "verde")`
- `numeros = (1, 2, 3, 4, 5)`
- `dados_pessoais = "João", 30, "Engenheiro"`

## Acessando Elementos da Tupla

Os elementos das tuplas podem ser acessados através de índices, da mesma forma que listas.

### Exemplo de Acesso
- `cores[0]` resulta em `"vermelho"`
- `cores[-1]` resulta em `"verde"`

## Tuplas Aninhadas

As tuplas podem conter outras tuplas, criando estruturas aninhadas complexas.

### Exemplo de Tupla Aninhada
- `tupla_aninhada = (1, 2, (3, 4), (5, 6, (7, 8)))`

## Imutabilidade das Tuplas

A principal característica das tuplas é sua imutabilidade, significando que não é possível adicionar, remover ou alterar seus elementos após a criação.

- **Implicações da Imutabilidade**: Oferece segurança de dados, pois os elementos não podem ser alterados acidentalmente.

## Fatiamento de Tuplas

Assim como listas, tuplas podem ser fatiadas para obter subconjuntos.

### Exemplo de Fatiamento
- `numeros[1:4]` resulta em `(2, 3, 4)`

## Desempacotamento de Tuplas

O desempacotamento permite atribuir os elementos de uma tupla a variáveis separadas.

### Exemplo de Desempacotamento
- `nome, idade, profissao = dados_pessoais`

## Métodos da Classe Tupla

Apesar de sua imutabilidade, tuplas têm alguns métodos úteis.

### Métodos Comuns de Tupla
- **Contar Elementos**: `tupla.count(elemento)` retorna o número de vezes que um elemento aparece.
- **Encontrar Índice**: `tupla.index(elemento)` retorna o índice do primeiro elemento encontrado.

## Tuplas vs. Listas

Tuplas são usadas em situações onde a imutabilidade é desejada. Elas são mais rápidas que as listas e protegem os dados contra alterações.

## Conclusão

As tuplas são fundamentais em Python, proporcionando uma maneira segura e eficiente de trabalhar com coleções de dados imutáveis.

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
