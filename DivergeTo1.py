'''
Concept:
You have any natural number n.
If n is even: divide it by 2
If n is odd: multiply it by 3 and add 1
Eventually these process will continue till number diverges to 1
'''
while True:
    x = int(input("Enter any natural number "))
    if x <= 0:
        print("Natural Numbers are positive integers greater than 1")
        continue
    else:
        break
t = 0
if x == 1:
    print("Single iteration and we have 1...Cheers!")
else:    
    while x != 1:
        if x % 2 == 0:
            x = x/2
            t += 1
        else:
            x = 3*x+1
            t +=1
        print(int(x))
    print(f"The number of iterations is {t}")
