def conversor(m):
    centimentos = m*1000
    milimentros = centimentos*1000
    print(f'{m} é equivalente a {centimentos} centimentos e {milimentros} milimentos')

m = int(input('Digite um valor de metros: '))
conversor(m)