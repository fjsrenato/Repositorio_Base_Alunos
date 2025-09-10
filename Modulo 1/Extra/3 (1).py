
def validar_senha(senha_correta, senha_digitada):
 
 if senha_digitada == senha_correta:
   return ('senha correta')
 else:
  return ('senha errada')
 
senha_correta = 'ayeshaeroticamamae'
senha_usuario = input('digite a sua senha:')

print (validar_senha(senha_correta, senha_usuario))