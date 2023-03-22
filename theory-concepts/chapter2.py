"""
# Why Progam?


# Por que programar?
% Pois os computadores foram criados para nos auxiliar e fazer coisas por nós! Mas para isso precisamos falar a lingua deles e descrever o que queremos que seja feito. Para os usuários é mais fácil, pois as opções já são inseridas (no front-end) de maneira que eles apenas escolhem e o programa reconhece a opção escolhida (a estratura e código por trás está no back-end). A cada dia que se passa a programação ajuda mais e mais o mundo facilitando e resolvendo problemas e diminuindo o tempo de execução de tarefas.



@ Usuários vs Programadores
% Os usuários veem o computador como um conjunto de ferramentas como o processador de texto, mapas, listas de afazeres e etc. Já os programadores conseguem aprender os "meios" e a linguagem da computação.




# Por que ser um programador?
% Para as nossas tasks serem realizadas e para criar ferramentas que outros possam utilizar, facilitar a resolução de problemas e o tempo gasto para resolver os mesmos. Além disso você pode criar ferramentas para você mesmo! Não é nem precisa querer ser um programador profissional, você pode fazer planilhas que usam base de dados, scripts que realizam tarefas na sua profissão. As possibilidades vão além do limite!




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



# No fim, o que é um programa?
% Na definição de programa, é uma sequência de definições e regras que são criadas para realizar um fim desejado, como uma receita de bolo, você segue as etapas criadas por alguém ou por você mesmo para no fim ter um bolo.




@ A fase de aprendizado
% À medida que avança no restante do livro, não tenha medo se os conceitos parecerem não se encaixar bem na primeira vez. Quando você estava aprendendo a falar, não foi um problema nos primeiros anos que você apenas fizesse ruídos fofos e gorgolejantes. E tudo bem se levasse seis meses para você passar de um vocabulário simples para frases simples e levasse mais 5-6 anos para passar de frases para parágrafos, e mais alguns anos para ser capaz de escrever um conto completo interessante em seu ter.

% Queremos que você aprenda Python muito mais rapidamente, então ensinaremos tudo ao mesmo tempo nos próximos capítulos. Mas é como aprender um novo idioma que leva tempo para ser absorvido e compreendido antes de parecer natural. Isso leva a alguma confusão quando visitamos e revisitamos tópicos para tentar fazer com que você veja o quadro geral enquanto definimos os pequenos fragmentos que compõem esse quadro geral. Embora o livro seja escrito linearmente, e se você estiver fazendo um curso, ele progredirá de maneira linear, não hesite em ser muito não linear na maneira como aborda o material. Olhe para frente e para trás e leia com um leve toque. Ao examinar material mais avançado sem entender completamente os detalhes, você pode entender melhor o “por quê?” de programação. Ao revisar o material anterior e até mesmo refazer os exercícios anteriores, você perceberá que realmente aprendeu muito material, mesmo que o material que você está olhando pareça um pouco impenetrável.

% Normalmente, quando você está aprendendo sua primeira linguagem de programação, existem alguns maravilhosos “Ah Hah!” momentos em que você pode olhar para cima depois de bater em alguma rocha com um martelo e um cinzel e se afastar e ver que está realmente construindo uma bela escultura.

% Se algo parece particularmente difícil, geralmente não vale a pena ficar acordado a noite toda e ficar olhando para aquilo. Faça uma pausa, tire uma soneca, faça um lanche, explique o que você está tendo problema para alguém (ou talvez seu cachorro) e depois volte a isso com novos olhos. Garanto a você que, depois de aprender os conceitos de programação do livro, você olhará para trás e verá que tudo foi muito fácil e elegante e simplesmente demorou um pouco para você absorver tudo.

"""
# $ Just some random code that i did

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