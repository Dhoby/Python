def profit (buy, num, name):
    
    ORI = buy * num
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input (name + "现价?\n")
    COM_SOLD = max (float (PRICE) * num * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * num * 0.01 / 1000
    STAMP = float (PRICE) * num * 0.05 / 100
    Profit1 = float (PRICE) * num - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST2 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print (name + "total cost is: " + '%.2f'%COST2 + "\n")
    print (name + "net profit is: " + '%.2f'%Profit1 + "\n")


CURRENT_STOCKS = ["同仁堂","东阿阿胶"]

print (CURRENT_STOCKS)

while 1:
    
    CHOICE = input ("请选择查询的股票\n")


    if CHOICE == "1":
        profit(46.4225, 800, CURRENT_STOCKS[0])

    if CHOICE == "2":
        profit(59.1, 600, CURRENT_STOCKS[1])
