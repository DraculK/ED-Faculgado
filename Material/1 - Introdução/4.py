def remove_duplicatas(thelist):
  teste = []
  for element in thelist:
    if element not in teste:
        teste.append(element)
  return teste
