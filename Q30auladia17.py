print('digite seu ano de nascimento')
anodenascimento = int(input())
print('digite o ano atual')
anoatual = int(input())
cal = anoatual - anodenascimento
idade2050 = 2050 - anodenascimento
print('sua idade atual é {} e sua idade em 2050 é {}'.format(cal,idade2050))
