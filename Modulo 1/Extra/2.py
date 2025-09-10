qtd = int (input('quantos numeros voce vai digitar'))
           
positivos = 0
negativos = 0
zeros = 0

for i in range(qtd):
    n = int(input(f'digite o {i + 1}° numero: '))

    if n > 0:
        print (f'{n} é positivo')
        negativos += 1

    elif n < 0:
        print (f'{n}é zeros')
        zeros += 1

else:
   print(f'{n} é negativo')
   zeros += 1

   print ('\nRelatorio:')
   print (f'positivos: {positivos}')
   print (f'negativos: {negativos}')
   print (f'zeros: {zeros}')