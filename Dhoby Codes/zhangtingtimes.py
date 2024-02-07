a = input ("请输入现价\n")
b = input ("请输入卖价\n")

x = float(a)
y = float(b)

if x >= y:
    print("现价必须小于卖价，请重新输入")
    
else:
    i = 1
    
    while i > 0:
        c = x * 1.1**i
        if c >= y:
            break
        else:
            i = i + 1
        
    print(f"需要 {i} 个涨停就可以卖了\n")