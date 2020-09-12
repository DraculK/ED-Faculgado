def primos(m):
  tot = 0
  for j in range(1, m+1):
    if m%j==0:
      tot+=1
  if tot == 2:
    return True
  else: 
    return False

def primos_gemeos(n):
  lista = []
  p1, p2 = 3,5
  i=0

  if n ==0:
    return lista
  elif n==1:
    lista.append((3,5))
    return lista
  elif n>1:
    while i<n:
      num1 = primos(p1)
      num2 = primos(p2)
      if(num1 == True and num2 == True):
        lista.append((p1,p2))
        i+=1
      p1=p2
      p2=p1+2
    return lista



