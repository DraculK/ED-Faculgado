def fatorial(num):
  if num <= 1:
    print
    return 1
  else:
    fact = fatorial(num - 1)
    print
    fact
    result = num * fact
    print
    "return", result
    return result
