t = int(input("Enter No. of Rows "))
k = 2*t - 1
for i in range (1,t+1):
    for j in range(1,k):
        print(end = " ")
    k = k - 1
    for j in range(1, i+1):
        print("* ",end = '')
    print()
