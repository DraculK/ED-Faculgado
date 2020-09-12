def maior_norma(thelist, list):
  teste = 0
  teste1 = 0
  for element in thelist:
    teste += element*element

  for i in list:
    teste1 += i*i

  if(teste>teste1):
    print ("PRIMEIRO")
  else:
    print ("SEGUNDO")
