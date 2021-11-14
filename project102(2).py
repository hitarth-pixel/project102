# function declareations
def solveaxplusbeqc():
    a=int(input('please give value of a'))
    b=int(input('please give value of b'))
    c=int(input('please give value of c'))
    if a !=0:
        print('solving equations '+str(a)+'x+'+str(b)+'='+str(c))
        x=(c-b)/a
        print('answer x= '+str(x))
    else:
        print('equation cannot be solved by the given values. try again')

def solveaxplusbeqcxplusd():
    a=int(input('please give value of a'))
    b=int(input('please give value of b'))
    c=int(input('please give value of c'))
    d=int(input('please give value of d'))
    if (a-c) !=0:
        print('solving equations '+str(a)+'x+'+str(b)+'='+str(c)+'x+'+str(d))
        x=(d-b)/(a-c)
        print('answer x= '+str(x))
    else:
        print('equation cannot be solved by the given values. try again')

def getUserChoice():
    message='which type of equation you want to solve. enter the choice'
    return int(input(message))

# Main program
print("welcome to the equation solver")
choice1='1) ax+b=c'
choice2='2) ax+b=cx+d'
choice3='3) quit'
print(choice1)
print(choice2)
print(choice3)
choice=getUserChoice()
while choice !=3:
     if choice==1 or choice==2:
         print('choice= '+str(choice))
         if choice ==1:
             solveaxplusbeqc()
         else:solveaxplusbeqcxplusd()
     else:
         print('please enter valid choice')
     choice=getUserChoice()
print('thanks for using problem solver')

