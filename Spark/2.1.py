print ("enter 5 integers\n")
q = [int(i) for i in input().split()]
sum = q[0] + q[1] + q[2] + q[3] + q[4] 
if sum%2 !=0:
    print("no solution")
else:
    bench = sum/2
    first = 0
    while first < 4:
        second = first + 1;
        while second < 5:
            if (q[first] + q[second]) == bench:
                right1 = q[first]
                right2 = q[second]
                print ("\n")
                print(f"the first on the right is: {right1}\n")
                print(f"the second on the right is: {right2}\n")
            second = second + 1

        first = first + 1        