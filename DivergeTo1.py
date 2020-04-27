x = int(input("Enter No. "))
t = 0
if x == 1:
    print(t)
    print("The number of iterations is 1")
else:    
    while x != 1:
        if x % 2 == 0:
            x = x/2
            t += 1
        else:
            x = 3*x+1
            t +=1
        print(x)
    print(f"The number of iterations is {t}")
