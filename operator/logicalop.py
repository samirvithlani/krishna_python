#
'''
    cond1 and cond2
    T     T     T
    F     -     F
    T     F     F
    
    cond1 or cond2
    T     -   T
    F    T    T
    F    F    F

'''

isPassed = False
hasTicket = False

if isPassed or hasTicket:
    print("can watch movie..")
else:
    print("not allowed...")    

