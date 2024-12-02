
'''
def descending(lst):
    
    for i in range(a):
        if (a[i] > a[i+1]):
            return True
        else:
            return False'''

        


def descending(l):
   
    if len(l) < 2:
        return True
    
   
    for i in range(1, len(l)):
       
        if l[i] > l[i - 1]:
            return False
    
  
    return True


my_list = [5, 4, 3, 2, 1]
result = descending(my_list)
print(result)  # Output: True
