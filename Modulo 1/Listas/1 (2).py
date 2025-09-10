nomes = ['Renato', 'Joao', 'Cema']
print('Lista inicial:', nomes)

nomes.append('Carlos')
print('Apos append:', nomes)

nomes.insert(1, 'fernanda')
print ('apos insert', nomes)

nomes [1]= 'Paulo'
print ('apos modificação', nomes)

del nomes [3]
print ('apos del:', nomes)

removido = nomes.pop(2)
print(f'apos pop (removido)' '{removido}', nomes)

nomes.clear()
print('apos clear:', nomes)