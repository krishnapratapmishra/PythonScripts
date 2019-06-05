#Comparing Values
"""
Operator	Comparative test:
==			Equality
!=			Inequality
>			Greater than
<			Less Than
>=			Greater than or equal to
<=			Less than or euql to
"""
# A-Z uppercase characters have ASCII code values 65-90 and a-z lowercase characters have ASCII code values 97-122

nil=0
num=0
max=1
cap='A'
low='a'

print('Equality :\t',nil,'==',num,nil==num)
print('Equality :\t',cap,'==',low,cap==low)

print('Inequality :\t',nil,'!=',num,nil!=num)
print('Equality :\t',cap,'!=',low,cap!=low)

print('Greater :\t',nil,'>',max,nil>max)
print('Lesser :\t',nil,'<',max,nil<max)

print('Greater or equal to :',nil,'>=',num,nil>=num)
print('Lesser or equal to :',nil,'<=',num,nil<=num)