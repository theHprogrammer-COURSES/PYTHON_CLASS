# Bootcamp Python Data Analytics: String e Fatiamento

Este módulo do Bootcamp, conduzido por Guilherme Artur de Carvalho (@decarvalhogui), foca na manipulação de strings em Python, uma habilidade fundamental para qualquer desenvolvedor. Exploramos métodos úteis de strings, técnicas de interpolação e fatiamento.

## Métodos Úteis da Classe String

Python oferece uma variedade de métodos para manipular strings, tornando-as ferramentas versáteis para qualquer programador.

### Transformações Básicas
Manipulação de strings é uma operação comum em Python, e a linguagem oferece métodos convenientes para várias transformações básicas.

- **Maiúsculas e Minúsculas**: 
  - `.upper()` converte uma string para maiúsculas. Ex: `"pYtHon".upper()` resulta em `"PYTHON"`.
  - `.lower()` converte para minúsculas. Ex: `"pYtHon".lower()` resulta em `"python"`.
  - `.title()` converte a primeira letra de cada palavra para maiúscula. Ex: `"pYtHon".title()` resulta em `"Python"`.

- **Eliminação de Espaços**: 
  - `.strip()` remove espaços no início e no fim da string. Ex: `" Python ".strip()` resulta em `"Python"`.
  - `.lstrip()` remove espaços à esquerda. Ex: `" Python ".lstrip()` resulta em `"Python "`.
  - `.rstrip()` remove espaços à direita. Ex: `" Python ".rstrip()` resulta em `" Python"`.

### Junção e Centralização
Esses métodos são úteis para formatar strings para exibição ou processamento.

- **Centralização**: `.center(largura, [fillchar])` centraliza uma string em um campo de um determinado tamanho, opcionalmente preenchendo com um caractere específico. 
  - Ex: `"Python".center(10, "#")` resulta em `"##Python##"`.

- **Junção**: `.join(iterável)` concatena uma sequência de strings, inserindo uma string entre cada elemento.
  - Ex: `".".join("Python")` resulta em `"P.y.t.h.o.n"`.

### Métodos de Interpolação

A interpolação de strings é uma técnica poderosa em Python para incorporar variáveis e expressões dentro de strings.

#### Método `format()`
- **Uso**: Permite inserir valores em uma string usando `{}` como placeholders.
- **Exemplos**:
  - Com índices implícitos: `"Olá me chamo {}. Trabalho como {}.".format("Guilherme", "Programador")` resulta em `"Olá me chamo Guilherme. Trabalho como Programador."`
  - Com índices explícitos: `"Olá me chamo {3}. Trabalho como {1}.".format(linguagem, profissao, idade, nome)` permite reordenar e reutilizar as variáveis.
  - Com nomes de variáveis: `"Olá me chamo {nome}. Tenho {idade} anos.".format(nome=nome, idade=idade)` para uma leitura mais clara.

#### f-strings
- **Descrição**: Uma forma moderna e concisa de interpolação usando a sintaxe `f"{var}"`.
- **Vantagens**: Diretas, legíveis e menos propensas a erros em comparação com métodos anteriores.
- **Exemplos**:
  - Básico: `f"Olá me chamo {nome}. Trabalho como {profissao}."` para uma interpolação direta.
  - Com formatação: `f"Valor de PI: {PI:.2f}"` formata o valor de PI como uma string com duas casas decimais.

#### Old Style (`%`)
- **Descrição**: Método mais antigo de interpolação de strings, utilizando um estilo similar ao da linguagem C.
- **Uso**: `%` seguido por especificadores de formato, como `%s` para strings e `%d` para números inteiros.
- **Exemplo**: `"Olá me chamo %s. Eu tenho %d anos de idade trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem)` resulta em uma string com valores interpolados.

Esses métodos de interpolação oferecem diversas opções para incorporar dados dinâmicos em strings, dependendo das necessidades e preferências do programador.

## Fatiamento de String

Fatiamento é uma técnica para extrair subconjuntos de uma string em Python, permitindo acessar partes específicas da string de forma eficiente.

- **Sintaxe**: `string[start:stop:step]` para especificar o início, fim e passo do fatiamento.
- **Exemplos Práticos**:
  - `nome[0]`: Acessa o primeiro caractere. Exemplo: Para `nome = "Guilherme Arthur de Carvalho"`, retorna `"G"`.
  - `nome[:9]`: Retorna os primeiros 9 caracteres. Exemplo: Retorna `"Guilherme"`.
  - `nome[10:]`: Extrai a substring a partir do caractere 11 até o final. Exemplo: Retorna `"Arthur de Carvalho"`.
  - `nome[10:16]`: Retorna os caracteres da posição 11 até 16. Exemplo: Retorna `"Arthur"`.
  - `nome[10:16:2]`: Retorna caracteres da posição 11 até 16, com passo 2. Exemplo: Retorna `"Atu"`.
  - `nome[:]`: Cria uma cópia da string. Retorna `"Guilherme Arthur de Carvalho"`.
  - `nome[::-1]`: Inverte a string. Retorna `"ohlavraC ed ruhtrA emrehliuG"`.

Essa técnica é especialmente útil para manipulação de strings em diversas aplicações, como análise de dados, processamento de texto e mais.

## Strings de Múltiplas Linhas

Strings de múltiplas linhas no Python são definidas com aspas triplas (simples `'''` ou duplas `"""`). Elas são úteis para armazenar textos longos e manter a formatação.

- **Uso de Aspas Triplas**: `'''` ou `"""` são usadas para definir strings que ocupam múltiplas linhas.
- **Preservação da Formatação**: Mantém a formatação original com quebras de linha, espaços e recuos.
- **Exemplos**:
  - Com aspas triplas duplas: 
    ```python
    mensagem = f"""
    Olá meu nome é {nome}
    Eu estou aprendendo Python
    """
    ```
    Retorna uma mensagem formatada com o nome e a informação sobre o aprendizado.
  - Com aspas triplas simples:
    ```python
    mensagem = f'''
    Olá meu nome é {nome}.
    Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
    '''
    ```
    Preserva a formatação e os recuos na string final.

A utilização de strings de múltiplas linhas facilita o trabalho com textos grandes e a preservação de formatos específicos em Python.


## Conclusão

A compreensão de como manipular strings é vital para o desenvolvimento em Python. Este módulo fornece as ferramentas e técnicas necessárias para lidar com strings de forma eficiente e eficaz.

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
