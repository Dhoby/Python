def profit (buy, num, name):
    
    ORI = buy * num
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input (name + "现价?\n")
    COM_SOLD = max (float (PRICE) * num * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * num * 0.01 / 1000
    STAMP = float (PRICE) * num * 0.05 / 100
    Profit2 = float (PRICE) * num - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST2 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print (name + "total cost is: " + '%.2f'%COST2 + "\n")
    print (name + "net profit is: " + '%.2f'%Profit2)


CURRENT_STOCKS = ["同仁堂"]

print (CURRENT_STOCKS)

profit(46.4225, 800, CURRENT_STOCKS[0])
