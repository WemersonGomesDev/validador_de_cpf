"""
CPF = 168.995.350-09
    """


# 01234567891011
# 168995350-09


lista_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_3 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
CPF = '118.450.034-70'
CPF = CPF.replace('.', "")
CPF = CPF.replace('-', '')
CPF_N = []
for n in CPF:
    n = int(n)
    CPF_N.append(n)
    cpf_numero = (CPF_N[0:9])
valor_01 = [x*y for x, y in zip(lista_2, CPF_N)]
soma_01 = sum(valor_01)
teste_01 = (11 - (soma_01 % 11))
digito_01 = ''
if teste_01 > 9:
    digito_01 = 0
elif teste_01 <= 9:
    digito_01 = teste_01


digito_02 = ''
sgundo_digit = cpf_numero
sgundo_digit.append(digito_01)
valor_02 = [x*y for x, y in zip(lista_3, sgundo_digit)]
soma_02 = sum(valor_02)
teste_02 = (11 - (soma_02 % 11))
if teste_02 <= 9:
    digito_02 = teste_02
else:
    digito_02 = 0
print(f'Digito01: {digito_01}\nDigito02: {digito_02}')

validar = []
validar.append(digito_01)
validar.append(digito_02)

validacao = 'CPF valido'

for t in (CPF_N[9:11]):
    if t not in validar:
        validacao = 'CPF Invalido'


print(validacao)
