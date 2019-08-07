def star(t):
    for i in range(t):
        for j in range(i+1):
            print("*",end="")
        print()
t = int(input("Enter No. "))
star(t)