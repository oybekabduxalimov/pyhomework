a = int(input('firstnum: '))
b = int(input('secondnum: '))
if a%5==0 and b%5==0 and a%3==0 and b%3==0:
    print('Both Divisible by 3 and 5')
else:
    print('Either one is not divisible by 3 and 5')