def get_first_last_elements(l):
    if len(l)==0:
        return []
    elif len(l)==1:
        return [l[0]]
    else:
        return [l[0],l[-1]]
    


a=[5,10,15,20,25]
result=get_first_last_elements(a)
print(f"list containing the first and last elements :{result}")