from time import sleep
print("""Vemos hoje em dia a importancia de se cuidar, o que vem sendo cada dia mais importante
      ainda mais com os ocorridos os ultimos anos, aumento de depressão, ansiedade, alcoolismo entre outros.
      Dentre estes existe a obsidade, uma questão que anda afetando muitos jovens e idosos nos ultimos anos
      o que pode trazer com ela muitos agravantes, inclusive aumento na chance de infarto.
      Fazendo necessario cada dia mais estarmos cientes de como estamos, disponibilizamos aqui um app para fazer um
      aproximamento do seu IMC(Indice de Massa Corporea) o que pode trazer alguns avisos sobre como ou o que
      pode estar te trazendo algumas dificuldades na saude!
      A visita ao medico é indispensavel!""")
sleep(2)
nome = str(input('Qual o seu nome: ')).strip()
sleep(0.5)
print('Olá {}, vamos aqui pegar mais algumas informações então!'.format(nome))
sleep(0.5)
altura = float(input('Qual a sua altura em metros: '))

peso = float(input('Qual o seu peso em kg: '))

imc = peso/(altura**2)
sleep(1)
if imc<18.5:
    print('Seu IMC atual é de {:.1f}, esta muito baixo.'.format(imc))
elif imc<=25:
    print('Seu IMC atual é de {:.1f}, esta dentro da media saudavel.'.format(imc))
elif imc<=30:
    print('Seu IMC atual é de {:.1f}, esta um pouco acima do normal.'.format(imc))
elif imc<=40:
    print('Seu IMC atual é de {:.1f}, você esta numa categoria considerada obesidade, talvez seja melhor rever seus habitos.'.format(imc))
else:
    print('Seu IMC atual é de {:.1f}, seu nivel de IMC acusa obesidade morbida, é indispensavel o acompanhamento de um medico.'.format(imc))


"""Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo
com a tabela abaixo:
-Abaixo de 18.5: abaixo do peso
-Entre 18.5 e 25:peso ideal
-25 até 30:sobrepeso
-30 até 40:obesidade
-acima de 40:obesidade morbida"""