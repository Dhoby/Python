
def profit (buy, num, name):
    
    ORI = buy * num
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input (name + "现价?\n")
    COM_SOLD = max (float (PRICE) * num * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * num * 0.01 / 1000
    STAMP = float (PRICE) * num * 0.05 / 100
    Profit = float (PRICE) * num - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP
    COST = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    return COST, Profit


CURRENT_STOCKS = ["同仁堂","东阿阿胶", "大华股份"]

print (CURRENT_STOCKS)

while 1:
    
    CHOICE = input ("请选择查询的股票\n")


    if CHOICE == "1":
        result1 = profit(46.4225, 800, CURRENT_STOCKS[0])
        print (CURRENT_STOCKS[0] + " cost is: " + '%.2f'%result1[0] + "\n")
        print (CURRENT_STOCKS[0] + " profit is: " + '%.2f'%result1[1])

    if CHOICE == "2":
        result2 = profit(59.1, 600, CURRENT_STOCKS[1])
        print (CURRENT_STOCKS[1] + " cost is: " + '%.2f'%result2[0] + "\n")
        print (CURRENT_STOCKS[1] + " profit is: " + '%.2f'%result2[1])

    if CHOICE == "3":
        result3 = profit(20.1, 300, CURRENT_STOCKS[2])
        print (CURRENT_STOCKS[2] + " cost is: " + '%.2f'%result3[0] + "\n")
        print (CURRENT_STOCKS[2] + " profit is: " + '%.2f'%result3[1])
    
    if CHOICE == "4":    
       result1 = profit(46.4225, 800, CURRENT_STOCKS[0])
       result2 = profit(59.1, 600, CURRENT_STOCKS[1])
       result3 = profit(20.1, 300, CURRENT_STOCKS[2])

       total_cost = result1[0] + result2[0] + result3[0]
       total_profit = result1[1] + result2[1] + result3[1]

       print ("Portfolio cost is: " + '%.2f'%total_cost + "\n")
       print ("Portfolio profit is: " + '%.2f'%total_profit)