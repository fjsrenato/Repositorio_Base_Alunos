def saudacao (nome, horario):
 if horario == 'manha':
  return f'ola {nome}, bom dia'
 elif horario == 'tarde':
  return f'ola {nome}, bom tarde'
 elif horario == 'noite':
  return f'ola {nome}, bom noite'
 
nome_usuario = input('digite seu nome:')
 
horario_usuario = input ("digite o horario:")

print (saudacao(nome_usuario ,horario_usuario))