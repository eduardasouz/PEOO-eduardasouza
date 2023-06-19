print('Informe seu ano de nascimento:')
a = int(input())
idade = 2023 - a
print('Você tem {} anos'.format(idade))
if idade >= 16:
    print('Já pode votar nas eleições!')
if idade >= 18:
    print('Já pode tirar a habilitação!')
else:
    print('Não pode nem votar e nem tirar a habilitação')