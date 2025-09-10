saldo= 1000

while True:
    print ('\ncaixa eletronico')
    print ('(1)sacar')
    print ('(2)depositar')
    print ('(3)ver saldo')
    print ('(4)sair')

    opção= input ('opção:')
    
    if opção == '1':
      valor = int(input("valor para sacar:"))
      if valor < saldo:
         print ('saldo insuficiente')

      else:
         saldo -=valor
         print (f'saque de {valor} realizado com sucesso')

    elif opção == "2":
       valor = int(input('valor para depositar:'))
       saldo += valor
       print (f'deposito de {valor} reais')

    elif opção == '3':
      print (f'seu saldo atual é: {saldo} reais')

    elif opção == '4':
       print ('obrigado por usar nossos serviços')
       break 
    
    else:
       print ('opção invalida, tente novamente.')