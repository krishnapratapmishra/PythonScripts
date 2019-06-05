#Examing Conditions
#if-true-do-this if( var != 1) else if-else-do-this

a=1
b=2

print('\nVariable a is :', 'One' if (a == 1) else 'Not One')
print('\nVariable a is :', 'Even' if (a % 2) else 'Odd')

print('\n Variable b is :', 'One' if (b == 1) else 'Not One')
print('\nVariable b is :', 'Even' if (b % 2) else 'Odd')

# add a statement to asign the result of a conditional evalutaion to a anew variable
max=a if( a > b) else b 
print('\nGreater Value is :', max)
