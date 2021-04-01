import numpy as n
def selection_sort(l) :

    for i in range(len(l)):
        swap = i+n.argmin(l[i:])
        l[swap] , l[i] = l[i] , l[swap] 
    
    return l
l = [1,2,5342,4,32,4,321,432,432,4,32,4,32,432,4324, 576,5,8756,75,6,34]
print(selection_sort(l))



# output -: [1, 2, 4, 4, 4, 4, 5, 6, 32, 32, 32, 34, 75, 321, 432, 432, 432, 576, 4324, 5342, 8756]

# explanation - : the np.argmin() function takes list as an argument and returns the index of the smallest 
# number in the list . 

# for example -: l =  [ 4, 5 ,6 , 1 , 0 , 9 , 8 , 4] 
# the np.argmin function will return the number 4 as "0" is the smallest number and its index in l is 4.
