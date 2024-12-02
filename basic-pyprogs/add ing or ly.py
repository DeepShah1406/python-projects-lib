s = input("Enter String:")

print("Entered String is:", s)

if(len(s) >= 3):
    if(s[-3:] == "ing"):
        print("""String contain's 'ing', so after adding 'ly', The String is:""", s+"ly")
    else:
        print("""String does'nt contain 'ing', so after adding 'ing', The String is:""", s+"ing")
else:
    print("Enter String with more than 3 character's.")
