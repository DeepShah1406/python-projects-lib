def check_length_name(name,length):
    result=[len(name)== length for name , lenght in zip(name,length)]
    return result


Name=['ankita','rina','madhuri','shilpa']
Ln=[5,2,6,6]
output=check_length_name(Name,Ln)
print(output)
