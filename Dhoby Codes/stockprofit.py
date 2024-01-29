
TYP = input("how many types of stocks?\n")
NUM = int (TYP)

i = 0
TOT_Profit = 0

while i < NUM: 
    QTY = input("how many do you carry?\n")
    HOL = int (QTY)
    BUY = input("what is the initial price? 18.61 for myself\n") 
    ORI = float (BUY)* HOL
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input ("what is the price now?\n")
    COM_SOLD = max (float (PRICE) * HOL * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * HOL * 0.01 / 1000
    STAMP = float (PRICE) * HOL * 0.05 / 100
    Profit = float (PRICE) *HOL - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print ("all cost for this stock is: " + '%.2f'%COST)

    print ("your net profit for this stock is: " + '%.2f'%Profit)
    print("/n")
    TOT_Profit = TOT_Profit + Profit
    i = i + 1;
    
print ("All your net profit is: " + '%.2f'%TOT_Profit)
