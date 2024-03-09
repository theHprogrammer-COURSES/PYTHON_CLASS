# Bootcamp Python Data Analytics: Dominando Funções em Python

Este módulo, apresentado por Guilherme Artur de Carvalho (@decarvalhogui), foca na compreensão aprofundada das funções em Python, elementos cruciais para a programação estruturada e modular.

## O que são Funções?

Funções são blocos de código identificados por um nome, que podem receber uma lista de parâmetros e possuem a capacidade de retornar valores. Elas são fundamentais para tornar o código mais legível, facilitar o reaproveitamento e programar de maneira estruturada.

### Criação de Funções
- **Sintaxe Básica**: `def nome_da_funcao(parametros):`
- **Exemplo Simples**: 
  ```python
  def exibir_mensagem():
      print("Olá mundo!")
  ```

## Retornando Valores

Funções em Python podem retornar valores utilizando a palavra-chave `return`. Diferentemente de outras linguagens, uma função em Python pode retornar mais de um valor, facilitando operações complexas.

### Exemplos de Funções com Retorno
- **Retornando Soma**: 
  ```python
  def somar(a, b):
      return a + b
  ```
- **Retornando Múltiplos Valores**:
  ```python
  def obter_dimensoes(largura, altura):
      return largura, altura
  ```

## Argumentos Nomeados e `kwargs`

Funções em Python podem ser chamadas com argumentos nomeados e também aceitam `**kwargs` para um número arbitrário de argumentos nomeados.

### Uso de `**kwargs`
- **Exemplo**: 
  ```python
  def criar_perfil(**dados):
      print(dados)
  ```

## `args` e `kwargs`

Python permite combinar parâmetros obrigatórios com `*args` e `**kwargs`, recebendo valores como tupla e dicionário respectivamente, para maior versatilidade em funções.

### Exemplo com `*args` e `**kwargs`
- **Função Versátil**:
  ```python
  def registrar_usuario(nome, email, *hobbies, **dados_adicionais):
      # Lógica da função
  ```

## Parâmetros Especiais

Python suporta restringir como os argumentos podem ser passados para uma função: por posição, por nome ou ambos, proporcionando maior legibilidade e controle sobre a passagem de argumentos.

### Uso de Parâmetros Posicionais e Nomeados
- **Exemplo**:
  ```python
  def configurar_servidor(servidor, /, *, porta):
      # Configuração do servidor
  ```

## Funções como Objetos de Primeira Classe

Funções em Python são consideradas objetos de primeira classe, permitindo que sejam atribuídas a variáveis, passadas como parâmetros, usadas como valores em estruturas de dados e retornadas como valor em outras funções (closures).

### Exemplo de Função como Objeto
- **Passando Funções**:
  ```python
  def processar(dados, funcao):
      return funcao(dados)
  ```

## Escopo Local e Global

Python diferencia o escopo local do global dentro de funções, e alterações feitas em objetos imutáveis no escopo local são perdidas após a execução da função. Para manipular variáveis globais dentro de uma função, utiliza-se a palavra-chave `global`.

### Exemplo de Escopo
- **Alterando Escopo Global**:
  ```python
  def alterar_global():
      global variavel_global
      variavel_global = "novo valor"
  ```

## Conclusão

Este módulo explora as funções em Python em profundidade, oferecendo compreensão sobre sua criação, parâmetros, escopo e flexibilidade. Entender funções é fundamental para qualquer desenvolvedor Python.


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
