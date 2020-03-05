#leituras e atribuições nas variáveis

print("Qual a nota 1?")
nota1 = int(input())                        #lê do teclado a nota 1 como um número inteiro
print("Qual a nota 2?")
nota2 = int(input())                        #lê do teclado a nota 2 como um número inteiro
print("Qual a nota 3?")
nota3 = int(input())                        #lê do teclado a nota 3 como um número inteiro
print("E a frequencia do aluno? " )
frequencia = int(input())                   #lê do teclado a frequencia como um número inteiro
#                                           #o correto seria fazer essas leituras como números reais, pq pode ter vírgula nas notas.


# aqui começa a lógica

notafinal = nota1+nota2+nota3               # soma das notas  em uma variável notafinal

#verifca se a nota é maior que 6 e a frequencia é maior que 75
if (notafinal >= 6) and (frequencia >= 75): 
    print("aluno aprovado")
else:
     print("aluno reprovado")

#o aluno só será aprovado se (if) as condições de (notafinal>=6) e (frequencia>=75) forem satisfeitas, se não (else) é reprovado
#apesar disso o algoritmo pode possuir falhas, pois não limita o peso das notas informadas como no enunciado
#poderiam haver condições que verifiquem se a primeira nota é maior que 2 classifica como inválida e faz a leitura novamente, assim por diante.
#Mesma coisa na frequencia, da maneira que está é possivel informar uma frequencia 13123131, por exemplo. 
#   A mesma deveria se limitar entre 0 e 100