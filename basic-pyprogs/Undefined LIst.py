n = int(input ("Enter how many Students you want in list: "))
l1 = []

for i in range(0, n):
    nm = input ("Enter Name: ")
    l1.append(nm)
print("List of Student's:", l1)

s1 = []
for j in l1:
    v = len(j)
    s1.append(v)
print("Length is:", s1)


# def square(x):
#     return x ** 2

# def add(a, b):
#     return a + b

# result = add(square(3), square(4))
# print(result)  # Output: 25