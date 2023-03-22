"""
# Por que programar?
% Pois os computadores foram criados para nos auxiliar e fazer coisas por nós! Mas para isso precisamos falar a lingua deles e descrever o que queremos que seja feito. Para os usuários é mais fácil, pois as opções já são inseridas (no front-end) de maneira que eles apenas escolhem e o programa reconhece a opção escolhida (a estratura e código por trás está no back-end).



@ Usuários vs Programadores
% Os usuários veem o computador como um conjunto de ferramentas como o processador de texto, mapas, listas de afazeres e etc. Já os programadores conseguem aprender os "meios" e a linguagem da computação.




# Por que ser um programador?
% Para as nossas tasks serem realizadas e para criar ferramentas que outros possam utilizar.




@ Arquitetura de Hardware
% O mesmo é divido em Input/Output devices, Central Processing Unit, Main Memory and Secondary Memory.

   @ Central Processing Unit:
   % Executa o programa, a CPU está sempre perguntado "O que fazer a seguir?".

   @ Input Devices
   % Teclados, Mouses, Tela Touch, Microfone e etc.

   @ Output Devices
   % Tela, Caixas de Som, Impressoras e etc.

   @ Main Memory
   % Memória rápida e com armazenamento temporário e pequeno, perdido após o reboot.
   * Ex: Memória RAM.

   @ Secondary Memory
   % Memória devagar e de grande armazenamento, arquivos duram até serem excluídos.
   * Ex: HD´s, SSD´s e etc.



@ Python
% Precisamos aprender python para conseguirmos comunicar intruções para a linguagem Python. Erros de sintaxe e utilização de códigos incorretos é completamente normal no começo do apredizado. Quando um erro é cometido, o mesmo será indicado pelo próprio computador como "syntax erro" e normalmente os editores atuais indicam qual pode ser a causa do erro e até mesmo apresentar soluções.

$ Mas sempre é bom pesquisar e aprender caso o erro seja algo que não seja erro de escrita!

@ Exemplos

% x = 2
$ Declaração de atribuição

% x = x + 2
$ Declaração com expressão

% print(x)
$ Atribuição de impressão (print)



@ Interactive vs Script

   @ Interactive
   % Você escreve diretamente para o Python uma linha por vez e o mesmo responde.

   @ Script
   % Você insere uma sequência de declarações (linhas) em um arquivo.py utilizando um editor de texto e pede para o Python executar este arquivo.



@ As etapas de um programa
% Parecido com uma receita ou instrução para instalar algum equipamento, um programa é uma sequência de etapas para serem realizadas em uma ordem, sendo algumas etapas podendo ser "puladas" e outras obrigatórias", algumas podendo ser repitidas ou sendo executadas apenas uma vez.

% As vezes nós armazenamos um grupo de etapas para serem usadas de novo e de novo durante a execução do programa.



@ Tipos de etapas

   @ Sequential Steps
   % Quando o programa está em execução, o seu fluxo é de uma etapa para a próxima. Como programadores, nós devemos definir um caminho para o programa seguir.

   * Ex:

      x = 2
      print(x)

      x = x + 2
      print(x)

   @ Conditional Steps
   % São etapas que vão depender de váriaves ao decorrer do código, que caso o valor seja diferente em outra execução do programa o resultado pode ser diferente do anterior.

   * Ex:

      x = 5
      if x < 10 :
         print("Smaller")
      elif x > 20 :
         print("Bigger")
      else
         print("Finis")


   @ Repeated Steps
   % Mais conhecido como 'Loops', eles possuem uma uma váriavel que muda constantemente a cada loop.

   * Ex:

      n = 5
      while n > 0 :
         print(n)
         n = n - 1
      print("Blastoff!")

"""
import time

time.sleep(1)
print("Hello Wordl!")


time.sleep(1)
x = 2
print(x)
time.sleep(1)
x = x + 2
print(x)


time.sleep(1)
x = int(input("Insira um número: "))
if x < 10 :
   print("Smaller")
elif x > 20 :
   print("Bigger")
else :
   print("Finis")


time.sleep(1)
n = 5
while n > 0 :
   print(n)
   time.sleep(1)
   n = n - 1
print("Blastoff!")
