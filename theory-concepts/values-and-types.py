"""
@ Constants / Constantes
% Variáveis de valores fixos (caracteres, números ou uma string [cadeia de caracteres]), seus valores não se alteram durante a execução do código.

    $ Não se pode utilizar certas palavras (Palavras Reservadas) como nome de variaveis/identificadores :
    * Ex: False, class, return is, finally, none, if, for, lambda, continue, true, def, etc...

    

@ Variables / Variáveis
% Uma variável é um nome inserido na memória onde o programador pode armazenar dados e recuperar esses dados mais tarde utilizando o nome desta variável. Os programadores podems escolher o nome da variável e o mesmo também pode alterar o valor em declarações durante o código.

    $ Regras para nomes de variáveis:
    % Tem que começar começar com uma letra ou com um underscore (_);
    % Pode incluir apenas letras, numeros e underscores;
    % Case sensitive, trata letras maiúsculas e minúsculas de forma diferente.


    
@ Mnemonic Variable Names
% Nós nomeamos variáveis para nos ajudar a lembrar o que queremos armazenar
* Ex: "mnemonic" = "memory aid"



@ Sentences or Lines

% x = 2
$ Declaração de atribuição

% x = x + 2
$ Declaração com expressão

% print(x)
$ Atribuição de impressão (print)



@ Assignment Statements
% Para atribuir um valor há uma variável utilizamos o sinal "=". Uma declaração de cessão consiste em uam expressão no lado direito e uma variável para armazenar o valor do resultado.

% A varíavel nada mais é do que um espaço alocado na memória para armazenar um valor, o mesmo pode ser atualizado removendo o antigo valor por um novo.



@ Numeric Expressions
% Devido a falta de expressões matemáticas em nossos teclados, nós utilizamos a "linguagem do computador" para expressar a classes e operações matemáticas.

$ Quando for escrever expressões matemáticas, sempre escreva-as de maneira simples o bastante para serem facilmente compreendidas pelo computador.


    @ Operators - Operation
    % "+" ---> Addition / Adição

    % "-" ---> Subtraction / Subtração

    % "*" ---> Multiplication / Multiplicação

    % "/" ---> Division / Divisão

    % "**" --> Power / Exponenciação

    % "%" ---> Remainder / Resto da divisão


    @ Examples of Numeric Expressions
    
    * Ex:
        xx = 2
        xx = xx + 2
        print(xx)

        --

        yy = 440 * 12
        print(yy)

        --

        zz = yy / 1000
        print(zz)

        --

        jj = 23
        kk = jj % 5
        print(kk)


    $ Order of Evaluation
    % 1°: Parentheses / Parenteses
    % 2°: Exponentiation
    % 3°: Multiplication, Divison and Remainder
    % 4°: Addition and Subtraction
    % 5°: Left to Right

    

# What does "Type" mean?
% Em Python todas a variáveis possuem um tipo, por exemplo, Python sabe a diferença entre um "integer number" (número inteiro) e um string (conjunto de caracteres). Se tentarmos por exemplo, somar duas palavras:

* Ex:  ddd = 'hello' + 'there'
% O resultado será equivalente há: "hello there". Isso por quê se colocassemos números ao ínves de palavras, ocorreria uma conta matemática, mas pelo Python conseguir identificar que no exemplo os elementos da expressão são strings, ele na verdade efetuou um operação chamada "concatenação" que soma duas strings em uma só.

! NOTA IMPORTANTE: Se colocassemos os números entre aspas (Ex: "4"), ele iriá realizar a operação de concatenação, pois quando um expressão está entre aspas, o Python reconhece ela como um string e não como um número.


@ Types of "Type"
% Números tem dois tipos primários de divisão:

    
@ Integers
% São números inteiros, sejam eles positivos ou negativos.
* Ex: -14, -2, 0, 1, 100, 401233.


@ Floating Point Numbers
% Números de casa decimais.
* Ex: -2.5, 0.0, 98.6, 14.0
! NOTA IMPORTANTE: Perceba que não é utilizado "," para dividir as casa decimais e sim ".", caso utilize uma virgúla o python não vai reconhecer o número como um número tipo "float".


@ Conversions "Types"
% Você consegue controlar o tipo da variável quando inserido o tipo de váriavel antes do valor.
* Ex: f = float (i)



@ User Input
% Ao ínves de nós programadores definirmos os valores de nossas váriaveis, podemos permitir o usuário inserir o valor que ele desejar com o comando "input".



@ Comments
% Comentários são bastante importantes em Python, você pode descrever o que o trecho do código se refere, documentar quem escreveu o código e até mesmo usar o mecanismo de comentário para desativar um trecho do código, há duas maneiras de comentar:
* Ex: Utilizando o (") com dois pares de 3 cada, com isso você pode ter um parágrafo inteiro de comentário. Também é possível usar o (#) que no caso vai comentar a linha que ele tenha sido inserido (desde que ele seja o primeiro caractere na linha).







"""