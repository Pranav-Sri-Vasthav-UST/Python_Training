import math as m
inp = int(input('''please enter the operation number
                1.addition
                2.substaction
                3.multiplication
                4.divison
                5.modulus
                6.square root
                7. log
                
                :'''))
if(inp == 1 or inp == 2 or inp == 3 or inp == 4 or inp == 5):
    A = int(input("please enter integer 1: "))
    B = int(input("please enter integer 2: "))
elif(inp == 6 or inp == 7):
    C = int(input("please enter integer: "))
else:
    pass
    

if (inp == 1):
    print(A+B)
elif(inp == 2):
    print(A-B)
elif(inp == 3):
    print(A*B)
elif(inp == 4):
    print(A/B)
elif(inp == 5):
    print(A%B)
elif(inp == 6):
    print(m.sqrt(C))
elif(inp == 7):
    print(m.log(C))
else:
    print("please re-run the program and enter the number in the options given")
