### nome = str(input('Qual é o seu nome? '))
##if nome == 'João':
 ##   print('Que nome nonito!')
##else:
##    print('Seu nome é tão normal!')
##print('Bom dia, {}' .format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média foi {:.1f}' .format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')

### Condição Simplificada - print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')