nome = input('digite o nome:')
telefone = input ('digite o telefone:')
email = input ('digite o email')

arquivo= open('contatos.txt', 'a')
arquivo.write (f'{nome}, {telefone}, {email}\n')
arquivo.close()

conteudo =  open('contatos.txt','r')

print(conteudo.read())

conteudo.close()

