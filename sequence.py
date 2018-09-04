# take input from user
# print out first "n" numbers of the sequence (1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …)
count = 1
n1 = 1
n2 = 2
n3 = 3
n_sum = 1


n = int(input("Enter the length of the sequence: ")) 
while count <= n:
    if count == 1:
        print(n1)
    
    if count == 2:
        print(n2)

    if count == 3:
        print(n3)    
    
    if count > 3:
        n_sum = n1 + n2 + n3
        print(n_sum)
        n1 = n2
        n2 = n3
        n3 = n_sum
    count +=1


    
    


