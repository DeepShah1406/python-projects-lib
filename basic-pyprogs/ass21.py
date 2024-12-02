mt_tuple=()

while True:
    print("-------------Menu-------------")
    print("a = Add an element to tuple ")
    print("b = Count particular element in tuple")
    print("c = Revere Tuple")
    print(" q = For exit ")
    user=input("Enter Your Choice :")
    if user == 'a':
        element= input("Enter element you want to add :")
        mt_tuple += (element,)
        print(f"your element '{element}' added to tuple")
    elif user == 'b':
        count_element=input("Enter element to count :")
        count=mt_tuple.count(count_element)
        print(f" Count of '{count_element}'  in the tuple: '{count}'")
    elif user == 'c':
        revers_tuple= (reversed(mt_tuple))
        print(f"original tuple : '{mt_tuple}'")
        print(f"Reversed tuple : '{revers_tuple}'")
    elif user == 'q':
        break
    else:
        print(f" '{user}' isInvalid input please Enter a,b,c or q") 
