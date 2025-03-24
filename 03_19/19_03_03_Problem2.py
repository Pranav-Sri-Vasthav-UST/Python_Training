import math
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
a3 = int(input("Enter a3: "))
b3 = int(input("Enter b3: "))

def distance(m1,n1,m2,n2):
    distance = math.sqrt(math.pow((m1-m2),2)+math.pow((n1-n2),2))
    return distance

dis_of_AB = distance(a1,b1,a2,b2)
dis_of_BC = distance(a2,b2,a3,b3)
dis_of_CA = distance(a3,b3,a1,b1)
low1 = 0
low2 = 0

maxi = max(dis_of_AB,dis_of_BC,dis_of_CA)
if (dis_of_AB<dis_of_BC):
    if(dis_of_BC<dis_of_CA):
        low1 = dis_of_AB
        low2 = dis_of_BC
    elif(dis_of_BC<dis_of_CA):
        low1 = dis_of_AB
        low2 = dis_of_CA
elif (dis_of_AB<dis_of_CA):
    low1 = dis_of_AB
    low2 = dis_of_CA
else:
    low1 = dis_of_BC
    low2 = dis_of_CA

if ((dis_of_AB == dis_of_BC) or (dis_of_BC == dis_of_CA) or (dis_of_CA == dis_of_AB)):
    print("Isosceles triangle")
elif maxi == math.sqrt(math.pow(low1,2) + math.pow(low2,2)):
    print("Right angled triangle")
elif((maxi == math.sqrt(math.pow(low1,2) + math.pow(low2,2))) and low1 == low2):
    print("Right angled triangle")
else:
    print("Other triangle")