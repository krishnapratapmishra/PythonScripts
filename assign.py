#Assugning Values
"""
Operator	Example	Equivalent
=			a=b		a=b
+=			a+=b	a=(a+b)
-=			a-=b	a=(a-b)
*=			a*=b 	a=(a*b)
/=			a/=b 	a=(a/b)
%=			a%=b 	a=(a%b)
//=			a//=b 	a=(a//b)
**=			a**=b 	a=(a**b)
"""

a=8
b=4
print('Assign values:\t\t', 'a =',a,'\tb =',b)
a+=b 
print('Add & Assign:\t\t','a =',a,'(8 += 4)')

a-=b 
print('Substract & Assign:\t','a =',a,'(12 -= 4)')

a*=b 
print('Multiply & Assign:\t','a =',a,'(8 x= 4)')

a/=b
print('Divide & Assign:\t','a =',a,'(32 %= 4)')

a%=b
print('Modulus & Assign:\t','a =',a,'(8 %= 4)')






