a=float(input('Enter the value of a: '))
b=float(input('Enter the value of b: '))
c=input('Enter the operation: ')
if c=='addition':
    print('The value after addition is {} '.format(a+b))
elif c=='subtraction':
    print('The value after subtraction is {} '.format(a-b))
elif c=='multiplication':
    print('The value after multiplication is {} '.format(a*b))
elif c=='Division':
    print('The value after division is {} '.format(a/b))
elif c=='Floor Division':
    print('The value after division is {} '.format(a//b))
else:
    print('Undefined operation')
