
print ("\n""\n"'        Seja Bem-Vindo ao Menu da HAMBURGUERIA!!!'"\n""\n")
from time import sleep
sleep(3)

print(  '========================================' "\n"  "\n"           
    '        Escolha seu Hamburger:'"\n"
    '        (1) Frango = $2.50'"\n"
    '        (2) Carne = $3.50'"\n"
    '        (3) Calabresa = $1.50'"\n"
    '        (4) Amôndega = $3.0'"\n""\n"
    '        *Digite a sua opção.*'"\n""\n"
)
a = float(input('>>>>>>> Insira a opção: '))
print ('Aguarde um momento. . .')
from time import sleep
sleep(3)

if a == 1:
    cliente= 2.50
if a == 2:
    cliente= 3.50
if a == 3:
    cliente= 1.50
if a == 4:
    cliente= 3.00
if a == 5:
    cliente=0


else :
    print(  "\n""\n"
    '        Escolha a bebida:'"\n"
    '        (1) Cerveja = $2.50'"\n"
    '        (2) Suco = $3.50'"\n"
    '        (3) Água = $1.50'"\n"
    '        (4) Coca-Cola = $3.0'"\n"
    '        (5) Nenhuma bebibda'"\n"
    '        *Digite a sua opção.*'"\n""\n"
)
b = float(input('>>>>>>> Insira a opção: '))

if b == 1:
    cliente+= 2.50
if b == 2:
    cliente+= 3.50
if b == 3:
    cliente+= 1.50
if b == 4:
    cliente+= 3.00
if b == 5:
    cliente+= 0

print ('Aguarde um momento. . .')
from time import sleep
sleep(3)

print(  "\n" "\n"
    '         Valor da Compra: %.2f'%cliente
)

print('         Obrigado pela compra!!!'"\n" "\n")
from time import sleep
sleep(3)


