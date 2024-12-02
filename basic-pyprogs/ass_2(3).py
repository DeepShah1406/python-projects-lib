#Create a d class which as 2 lists as a member of them.
#Print the list whose sum is higher than another. 




class compare_list:
    def __init__(self,lst1,lst2):
        self.lst1=lst1
        self.lst2=lst2

    def find_higher_list(self):

        sum_of_lst1=sum(self.lst1)
        sum_of_lst2=sum(self.lst2)

        if (sum_of_lst1 > sum_of_lst2):
            print(f"SUM Of LIST 1 IS HIGHER THAN SUM OF LIST 2 :{sum_of_lst1}")
        elif(sum_of_lst2 > sum_of_lst1):
            print(f"SUM OF LIST 2 IS HIGHER THAN SUM LIST 1 : {sum_of_lst2}")
        else:
            print(" LIST 1 :{sum_of_lst1} AND LIST 2 {sum_of_lst2} BOTH LIST ARE EQUAL ")


list_1=[1,2,3,4,5,6]
list_2=[10,20,30,40]

result= compare_list(list_1,list_2)
result.find_higher_list()
            
                        
        

           
