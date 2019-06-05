#Casting data Types

a=input('Enter A Number: ')
b=input('Now Enter Another Number: ')

sum=a+b
print('\ndata Type Sum :',sum,type(sum))

sum=int(a)+int(b)
print('data Type Sum:', sum,type(sum))

sum=float(sum)
print('data Type Sum:',sum, type(sum))

sum=chr(int(sum))

print('data Type Sum :',sum,type(sum))