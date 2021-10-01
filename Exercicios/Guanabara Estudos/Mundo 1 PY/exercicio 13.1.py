from math import cos, sin, tan, radians

def raio(x):
    raio = radians(x)
    print(f'O angulo {x}, tem o radio {raio:.2f}, cosseno {cos(raio):.2f}, seno {sin(raio):.2f} e tangente {tan(raio):.2f}')

x = int(input('Digite o angulo para descobrir o Raio, Seno, Cosseno e Tangente: '))
raio(x)