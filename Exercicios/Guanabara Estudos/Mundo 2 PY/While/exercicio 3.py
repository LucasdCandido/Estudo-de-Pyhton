nome = str(input('Digite seu nome: ')).strip().upper()
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salario: '))
sexo = str(input('Digite seu sexo [f/m]: ')).upper()[0].strip()
esci = str(input('Digite seu estado civil [Solteiro(a)/Casado(a)/Viuvo(a)/Divorciado(a)]: ')).upper()[0].strip()
n = len(nome)
while (n<3):
    print('Nome muito curto, digite um nome com mais de 3 letras por favor!')
    nome = str(input('Digite seu nome: ')).strip().upper()
    n = len(nome)
while (0 < idade > 150):
    print('Idade invalida, por favor digite uma idade entre 0 e 150 anos')
    idade = int(input('Digite sua idade: '))
while salario < 0:
    print('Por favor, digite seu salario valido! ')
    salario = float(input('Digite seu salario: '))
while sexo not in 'fFmM':
    print('Sexo digitado invalido!')
    sexo = str(input('Digite seu sexo [F/M]: ')).upper()[0].strip()
while esci not in 'sScCvVdD':
    print('Estado civil invalido!')
    esci = str(input('Digite seu estado civil [Solteiro(a)/Casado(a)/Viuvo(a)/Divorciado(a)]')).upper()[0].strip()
print('Parabéns {}! Cadastro realizado com sucesso!'.format(nome))
"""Faça um programa que leia e valide as seguintes informações:
a. nome: maior que 3 caracteres;
b. idade: entre 0 e 150;
c. salario: maior que zero;
d. sexo: 'f' ou 'm';
e. estado civil: 's', 'c', 'v' e 'd';
use a função len(string) para saber o tamanho de um texto (numero de caracteres)
"""