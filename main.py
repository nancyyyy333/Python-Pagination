def pagination(max_page,curr_page,index):
    sum = index//2
    #print the exception at the start
    if int(curr_page) < (index):
        return([*range(1,index+1)])
    #print the exception at the end 
    elif curr_page > (max_page - index):
        return([*range((max_page+1)-index, max_page+1)])
    else:
        if index%2 == 0:
            return([*range(curr_page-sum,curr_page+sum)])
        else:
            return([*range(curr_page-sum,curr_page+sum+1)])

