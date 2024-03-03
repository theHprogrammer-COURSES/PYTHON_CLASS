# Bootcamp Python Data Analytics: Fundamentos Básicos

Neste módulo do Bootcamp, orientado pelo tutor Guilherme Artur de Carvalho (@decarvalhogui), mergulharemos em aspectos bśicos, porém essenciais da linguagem. Este módulo abrange desde tipos de dados, variáveis e constantes até funções de entrada e saída, preparando você para um entendimento mais profundo e prático do Python.

## Tipos de Dados em Python

| Categoria | Tipo de Dado | Descrição |
|-----------|--------------|-----------|
| Texto     | `str`        | Cadeias de caracteres. |
| Numéricos | `int`        | Números inteiros. |
|           | `float`      | Números de ponto flutuante. |
|           | `complex`    | Números complexos. |
| Sequência | `list`       | Listas ordenadas e mutáveis. |
|           | `tuple`      | Tuplas ordenadas e imutáveis. |
|           | `range`      | Sequências imutáveis de números. |
| Mapa      | `dict`       | Dicionários com pares chave-valor. |
| Coleção   | `set`        | Conjuntos não ordenados e sem elementos duplicados. |
|           | `frozenset`  | Versão imutável do conjunto. |
| Booleano  | `bool`       | Representa verdadeiro (`True`) ou falso (`False`). |
| Binário   | `bytes`      | Sequências de bytes. |
|           | `bytearray`  | Arrays de bytes mutáveis. |
|           | `memoryview` | Views de memória de objetos binários. |

Cada tipo de dado possui características e aplicações próprias, tornando-se essencial para a manipulação eficaz de dados e construção de algoritmos em Python.
## Variáveis e Constantes

Python utiliza variáveis e constantes para armazenar dados, cada um com suas peculiaridades:

### Variáveis
- **Definição**: Valores que podem mudar ao longo da execução do programa.
- **Tipagem Dinâmica**: O tipo de dado da variável é inferido pelo valor atribuído.
- **Exemplos de Uso**: Armazenar dados de entrada do usuário, resultados de cálculos, etc.
- **Mudança de Valor**: O valor de uma variável pode ser alterado facilmente através de uma nova atribuição.

### Constantes
- **Definição**: Valores imutáveis que não devem ser alterados durante a execução do programa.
- **Convenção em Python**: Embora Python não tenha constantes no sentido estrito, a convenção é usar nomes em letras maiúsculas para indicar constantes.
- **Exemplos de Uso**: Definir configurações, valores que não devem ser alterados, como taxas fixas, nomes de configuração, etc.

### Boas Práticas
- **Nomeação de Variáveis**: Utilizar nomes sugestivos e seguir o padrão snake_case.
- **Nomeação de Constantes**: Nomes em maiúsculas para diferenciar de variáveis.

As variáveis e constantes são fundamentais na programação Python, permitindo que dados sejam armazenados e manipulados de forma eficiente e organizada.

## Conversão de Tipos

Em Python, a conversão de tipos é um recurso essencial que permite manipular dados em diferentes formatos. Entender como e quando converter tipos é crucial para evitar erros e realizar operações eficientes.

### Conversões Comuns

- **Inteiro para Float**: Útil em cálculos que requerem precisão decimal.
- **Float para Inteiro**: Utilizado quando precisamos de números inteiros, descartando a parte decimal.
- **Numérico para String**: Importante para concatenação com outras strings ou para exibição formatada.
- **String para Numérico**: Essencial quando recebemos números em formato de texto que precisam ser calculados.

### Considerações Importantes

- **Erros de Conversão**: Tentar converter um tipo incompatível resultará em erro. Por exemplo, converter uma string que não representa um número em um tipo numérico.
- **Perda de Informação**: Ao converter de float para int, a parte decimal é descartada, resultando em possível perda de informação.

### Exemplos Práticos

- Conversão para realizar operações matemáticas em strings que representam números.
- Uso de conversões em entradas de usuário para garantir o tipo de dado correto.

Conversões de tipos são ferramentas poderosas no Python, permitindo que você manipule dados de maneira flexível e eficaz.

## Funções de Entrada e Saída

Em Python, a interação com o usuário é essencial, e isso é facilitado pelas funções `input()` e `print()`.

### `input()`
- **Propósito**: Ler dados da entrada padrão (geralmente o teclado).
- **Funcionamento**: Exibe uma mensagem para o usuário e aguarda pela entrada de dados.
- **Retorno**: Retorna os dados inseridos como uma string.
- **Exemplo de Uso**: `nome = input("Informe o seu nome: ")`

### `print()`
- **Propósito**: Exibir dados na saída padrão (geralmente a tela).
- **Funcionalidades**: Pode exibir múltiplos itens, separados por um delimitador e terminar com um caractere específico.
- **Argumentos Opcionais**: Inclui `end` (para definir o caractere final), `sep` (para definir o separador entre os objetos), entre outros.
- **Exemplo de Uso**: `print("Olá", nome)`, onde `nome` é uma variável previamente definida.

Essas funções são cruciais para qualquer programa que necessite de interação com o usuário, desde a coleta de informações até a exibição de resultados.

## Modo Interativo Python

- **Modo Interativo**: Ideal para testes rápidos e aprendizado. Execute comandos Python e veja os resultados imediatamente.
- **Funções `dir()` e `help()`**: Ferramentas poderosas para explorar propriedades de objetos e obter ajuda/documentação.

## Conclusão

Este módulo aprofunda seu conhecimento em Python, preparando-o para desafios mais complexos. Lembre-se de praticar regularmente e explorar as funcionalidades apresentadas.


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
