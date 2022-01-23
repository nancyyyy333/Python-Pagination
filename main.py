page = 63
num_pages = 100
max_pages = 65

if int(page) <= 5:
    print([*range(1,6)])
elif int(page) > (max_pages -5):
    print([*range(max_pages-4,max_pages+1)])
else:    
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 1)
    if rightIndex > num_pages:
        rightIndex = num_pages + 4
    custom_range = range(leftIndex, rightIndex)
    print([*custom_range])
