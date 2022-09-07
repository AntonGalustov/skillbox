print('Hello world')
summ = 10
while summ < 200:
    n = int(input('введите число '))
    if n % 10 == 0: 
      summ += n
    else:
      break
      print('число неверное. попробуйте снова.')
print('число',summ)

    

