#non- keyword

def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)

add(5,6)
add(3,4,5)
add(4,5,6,7,8)



#keyword

def intro(**data):
    print("\nData type of argument:",type (data))

    for key,value in data.items():
        print("{} is {}".format(key,value))


intro(First_Name="Deep", Last_Name="Shah", Age="23", Phone_Number=1234568790)
