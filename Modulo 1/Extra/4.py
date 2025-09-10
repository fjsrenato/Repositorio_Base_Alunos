estoque= 50

while True:
    print ('\ncontrole de estoque')
    print ('(1) adicionar unidades ao estoque')
    print ('(2) remover unidades do estoque')
    print ('(3) verificar estoque')
    print ('(4)sair')

    opção= input ('opção:')
    
    if opção == '1':
      quantidade = int(input("quantidade para adicionar:"))
      estoque += quantidade
      print ('unidades adicionadas com sucesso')

    elif opção == '2':
         quantidade = int(input('quantidade para remover:'))
         if quantidade < estoque:
             print (f'{quantidade}unidades removidas com sucesso')
         else:
            estoque += quantidade
            print ('nao é possivel remover')

    elif opção == '3':
        print (f'estoque atual: {estoque} unidades')

    elif opção == '4':
        print ('encerrando o programa')
        break 

    else:
        print ('opção invalida, tente novamente.')
   