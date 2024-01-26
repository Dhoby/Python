BUY = input("what is the initial price? 18.6 for myself\n") 
ORI = float (BUY)* 500
COM_INI = max (ORI * 2.5 / 10000, 5)
GUOHU_INI = ORI * 0.01 / 1000

PRICE = input ("what is the price now?\n")
COM_SOLD = max (float (PRICE) * 500 * 2.5 / 10000, 5)
GUOHU_SOLD = float (PRICE) * 500 * 0.01 / 1000
STAMP = float (PRICE) * 500 * 0.05 / 100
Profit = float (PRICE) * 500 - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

COST = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
print ("the total cost is: " + '%.2f'%COST)

print ("your net profit is: " + '%.2f'%Profit)