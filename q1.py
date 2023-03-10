# Given, N = No. of t-shirts in shop
# Also, string containing N t-shirts
# Then, required T-shirt numbers
# Size of those t-shirts

def main ():
    N = int(input()) # this is for the number of t-shirts in the shop
    sizes = input() #string containing all available t-shirt sizes
    reqn = int(input()) #this is required number of t-shirts
    reqsizes = input() # this is for the required t-shirts

    # let L = 1, M= 0, S = -1
    score_store= []
    score_req = []

    sizes = sizes.split (" ")
    reqsizes = reqsizes.split (" ")
    for i in sizes: # to sort the sizes in the store
        xcount = i.count ("X")
        letter = i[-1]
        if i[-1] == "S":
            score = -1 * (10**xcount)
        elif i[-1] == "M":
            score = 0 * (10**xcount)
        else:
            score = 1 * (10**xcount)
        score_store.append(score)
    
    # to sort the required sizes
    for j in reqsizes: # to sort the sizes in the store
        xcount = j.count ("X")
        letter = j[-1]
        if j[-1] == "S":
            score = -1 * (10**xcount)
        elif j[-1] == "M":
            score = 0 * (10**xcount)
        else:
            score = 1 * (10**xcount)
        score_req.append(score)
    
    score_store.sort()
    score_req.sort()

    flag = 0
    a = 0
    for i in score_req:
        for j in range (a, len(score_store)):
            if i <= score_store[j]:
                a = j+1
                flag = 0
                break
            else:
                flag = 1
    
    if flag == 1:
        print ("No")
    else:
        print ("Yes")
main()

    
        