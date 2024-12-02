def star_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end=" ")
        print()
n = int(input("Insert number of rows :"))
star_pyramid(n)