string1=input("Enter a first string : ")
string2=input("Enter a second string : ")

length1=0
for char in string1:
    length1 += 1

length2=0
for char in string2:
    length2 +=1



if length1 > length2:
    print(f"The first string '{string1}' is larger.")
elif length1 < length2:
    print(f"The second string '{string2}' is larger.")
else:
    print("Both strings are of equal length.")
