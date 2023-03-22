"""
# Conditional Execution


@ Boolean expressions
% Uma expressão booleana é uma expressão de True (verdadeiro) ou False (falso), um exemplo é utilizando o sinal "==" para comparar dois número se eles são iguais ou não:

* Ex:
print(5 == 5)
print(5 == 9)

$ True e False são valores especiais que são da classe "bool", elas não são "strings".
* Ex:
print(type(True))
print(type(False))
print(type("True"))
print(type("False"))


@ Comparison Operators
% Apesar desses operadores seram familiares, em Python eles são simbolos diferentes dos simbolos matemáticos usados para as mesmas operações.

$ Operadores de comparação
% (x == y)       --->       'x' é igual a 'y'
% (x != y)       --->       'x' não é igual a 'y'
% (x > y)        --->       'x é maior que y'
% (x < y)        --->       'x é menor que y'
% (x >= y)       --->       'x é maior ou igual a y'
% (x <= y)       --->       'x é menor ou igual a y'
% (x is y)       --->       'x é igual a y'
% (x is not y)   --->       'x é igual a y'


@ Logical Operators
% Há três tipos de operadores lógicos, "AND", "OR"e e "NOT". A semântica (significado) desses operadores são similares ao significado de suas definições em inglês.

* Ex: x > 0 and x < 10
$ É verdade apenas se 'x' for maior que '0' 'E' menor que '10'.

! IMPORTANTE: O operador "NOT" nega a expressão booleana, então se expressão é 4 < 10 é 'TRUE', com o 'NOT 4 < 10' a expressão se torna 'FALSE'.



@ Conditional Execution
% Para que seja possível escrever programas úteis, sempre é necessário checar as condições e a habilidade de mudar o 'comportamento' do programa. A forma mais simples e conhecida é o "if" (se).

* Ex:
if x > 0 :
    print('x is positive)

% A expressão booleana após o if é chamada de condição, se a condição "Se x for maior que 0 então" (O 'então' é representado pelo ':') então o comando "print" será executado. Caso a condição seja falsa, o comando será pulado. A declaração "if" tem uma estrutura similar ao ciclo "for". Ela consiste de um "cabeçalho" que termina com o ":" seguido por um bloco indentado.
$ Não há limites para o número de declarações após o ":", só é obrigátorio have ao menos uma declaração.


@ Alternative Execution
% Similar a estrutura anterior, mas agora temos após o "if" o "else" que serve como alternativa de caso a declaração do "if" seja "False". Pense no "else" como o "False" e o "if" como um boolean.
* Ex:
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

    

@ Chained Conditionals
% Novamente similar ao "if" mas além do "else" temos o "elif", o mesmo serve como um segundo "if", que em caso do "if" não ser verdadeiro e o melhor é que podem ser adicionados quantos "elif" sejam necessários, eles funcinam igual um "if" então eles devem ter uma declaração que para sua execução tem de ser "True".
* Ex:
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

$ O "elif" é uma abreviação de "else if".



@ Nested Conditionals
% Uma condição também pode ser agrupada a outra, podendo escrever um condicional de 3 ramos, por exemplo:
* Ex:
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

$ A condicional externa contém duas ramificações. A primeira ramificação contém uma instrução simples. A segunda ramificação contém outra instrução "if", que possui duas ramificações próprias. Essas duas ramificações são declarações simples, embora também possam ter sido declarações condicionais.



@ Catching exceptions using try and except
% Vimos anteiormente que um segmento de código onde usamos as funções "input" e "int" para ler e analisar um número inteiro digitado pelo usuário. 
* Ex:
>>> prompt = "What is the air velocity of an unladen swallow?\n"
>>> speed = input(prompt)
What is the air velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10:
>>>

% Quando tentamos executar um erro é apresentado, mas o problema é que o código para de executar na hora e não executa a próxima declaração. Para resolver este problema podemos usar uma outra estrutura de condicional para lidar com esses tipos de erros esperados e não esperados, o "Try" e "Except". 

% A ideia do "Try" e "Except" é que você talvez saiba que a sequência de instruções tenha um problema e que você queria adicionar algumas declarações para serem executadas sabendo que os erros irão ocorrer.
$ O bloco "except" serve para declarações que são feitas se não ocorrer nenhum erro.

* Ex:
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')



@ Short-circuit evaluation of logical expressions
% Quando o Python está processando uma expressão lógica como x >= 2 e (x/y) > 2, ele avalia a expressão da esquerda para a direita. Quando o Python detecta que não há nada a ser obtido avaliando o restante de uma expressão lógica, ele interrompe sua avaliação e não faz os cálculos no restante da expressão lógica. Quando a avaliação de uma expressão lógica é interrompida porque o valor geral já é conhecido, isso é chamado de curto-circuito na avaliação.

% Embora isso possa parecer um ponto delicado, o comportamento de curto-circuito leva a uma técnica inteligente chamada "guardian pattern". Considere a seguinte sequência de código no interpretador Python:

* Ex:
x = 6
y = 2
x >= 2 and (x/y) > 2


x = 1
y = 0
x >= 2 and (x/y) > 2


x = 6
y = 0
x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

   
% O terceiro cálculo falhou porque o Python estava avaliando (x/y) e y era zero, o que causa um erro de tempo de execução. Mas o primeiro e o segundo exemplos não falharam porque no primeiro cálculo y era diferente de zero e no segundo a primeira parte dessas expressões "x >= 2" avaliada como False então o "(x/y)" nunca foi executado devido a a regra do curto-circuito e não houve erro.

* Ex:
>>> x = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x = 6
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2
False
>>> x >= 2 and (x/y) > 2 and y != 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero


% Na primeira expressão lógica, x >= 2 é False, então a avaliação para no e. Na segunda expressão lógica, x >= 2 é Verdadeiro, mas y != 0 é Falso, então nunca alcançamos (x/y).

% Na terceira expressão lógica, o y != 0 está após o cálculo (x/y), então a expressão falha com um erro.

% Na segunda expressão, dizemos que y != 0 atua como um guarda para garantir que somente executemos (x/y) se y for diferente de zero.

"""
