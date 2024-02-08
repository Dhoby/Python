x = input("how many stocks bought at 48.045?\n")
a = int(x)

#y = input("what is the purchase price?\n")  
#b = float(y)
b = 48.045

z = input("what is the current price?\n")
c = float(z)
u = input("what is the proposed price?\n")
d = float(u)

f = ((b - c) * a)/ (d - c) - a
e = int(f)

print(f"you should buy at least {e} more stocks\n")





