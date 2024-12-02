Sub1=int(input('Subject 1 :'))
Sub2=int(input('Subject 2 :'))
Sub3=int(input('Subject 3 :'))
Percentage = (Sub1+Sub2+Sub3)/3
if(Percentage>90):
    print("Class = Distinction",Percentage)
elif(Percentage>70):
    print("Class = First",Percentage)
elif(Percentage>40):
    print("Class = Second",Percentage)
else:
    print("Class = Fail",Percentage)
