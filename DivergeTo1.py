'''
Concept:
You have any natural number n.
If n is even: divide it by 2
If n is odd: multiply it by 3 and add 1
Eventually these process will continue till number diverges to 1
'''
while True:
    num = int(input("Enter any natural number "))
    if num <= 0:
        print("Natural Numbers are positive integers greater than 1")
        continue
    else:
        break
counter = 0
if num == 1:
    print("Single iteration and we have 1...Cheers!")
else:    
    while num != 1:
        if num % 2 == 0:
            num = num/2
            counter += 1
        else:
            num = 3*num+1
            counter +=1
        print(int(num))
    print(f"The number of iterations is {counter}")
