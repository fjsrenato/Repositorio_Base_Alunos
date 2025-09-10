def dividir ():
    try:
        a= int(input('digite o valor de a:'))
        b= int(input('digite o valor de b:'))

        if b == 0:
          print ('erro: divisao por zero não é permitida')
          return None
    
        resultado = a / b 
        print(f'o resultado de {a} dividido por {b} é: {resultado}')

    
    except ValueError:
        print('erro, tente novamente')

dividir()
  