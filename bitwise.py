#Manipulating Bits
"""
| 		OR
& 		AND
~ 		NOT
^ 		XOR
<< 		Shift Left
>> 		Shift Right
"""
#Swap the values without third variable

a=10
b=5

print('a =' ,a ,'\tb =',b)

#1010 ^ 0101 = 1111 (decimal 15)
a=a^b

#1111 ^ 0101 = 1010 (decimal 10)
b= a^b

#1111 ^ 1010 = 0101

a=a^b

print('a=',a,'\tb=',b)


