lista = [10, 20, 30]

try:
    indice_str = input('digite um indice para acessar um elemento da lista:')
    indice= int(indice_str)
    elemento = lista [indice]
    print (f'o elemento no indice {indice} é: {elemento}')

except ValueError:
    print ('erro: tente novamente')

except IndexError:
    print ('erro: o indice nao esta na lista')