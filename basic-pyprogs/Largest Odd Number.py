n = int(input ("Enter how many Number's you want in list: "))
l1 = []

for i in range(0, n):
    en = int(input ("Enter Number: "))
    l1.append(en)

##l1 = [33, 44, 55]
##print(l1)

el = []
ol = []

for j in l1:
    if (j % 2 == 0):
        el.append(j)
    else:
        ol.append(j)
print("List:", l1)
print("Even List:", el)
print("Odd List:", ol)
mol = max(ol)
print("Largest Odd Number:", mol)
