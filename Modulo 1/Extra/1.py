nome = input ('digite o nome:')
email= input ('digite o email')

arquivo = open ('pessoa.txt', 'a')
arquivo.write (nome + ' | ' +email + '\n') 
arquivo.close()