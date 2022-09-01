varOne = True
varTwo = False

'''
AND - and 
Truth table for and
S1  S2  R=S1 and S2
T   T   T
T   F   F
F   T   F
F   F   F
'''
print("Logical AND " , (varOne and varTwo))


'''
OR - or 
Truth table for or
S1  S2  R=S1 or S2
T   T   T
T   F   T
F   T   T
F   F   F
'''
print("Logical OR " , (varOne or varTwo))

'''
Negation - not 
Truth table for not
S1  R = not S1
T   F
F   T
'''
print("Logical NOT " , (not varOne))