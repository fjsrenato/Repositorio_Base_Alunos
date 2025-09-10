
idade= int(input('digite sua idade'))

estudante= (input('é estudante?'))

if idade<12:
 print ('RS 8,00')

 if estudante== 'sim':
  print ('RS 12,00')

elif idade >=65:
   print ('RS 10,00')

else:
    print ('RS 20,00')