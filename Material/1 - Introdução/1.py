def primo(num):
  divisores = 0
  if(num==1):
    return "Não primo."
  for i in range(2,num):
    if (num%i==0):
      divisores += 1
      return "Não primo."
      break
    elif(divisores==0):
      return "Primo."
      break
