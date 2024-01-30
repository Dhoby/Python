

CURRENT_STOCKS = ["1电科网安","2同仁堂"]

CHOICE = input ("请选择查询的股票\n")

if CHOICE == "1":

    ORI = 18.61 * 500
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input ("电科网安现价?\n")
    COM_SOLD = max (float (PRICE) * 500 * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * 500 * 0.01 / 1000
    STAMP = float (PRICE) * 500 * 0.05 / 100
    Profit1 = float (PRICE) * 500 - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST1 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print ("电科网安 total cost is: " + '%.2f'%COST1)

    print ("电科网安 net profit is: " + '%.2f'%Profit1)

if CHOICE == "2":
    ORI = 49.1 * 200
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input ("同仁堂现价?\n")
    COM_SOLD = max (float (PRICE) * 200 * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * 200 * 0.01 / 1000
    STAMP = float (PRICE) * 200 * 0.05 / 100
    Profit2 = float (PRICE) * 200 - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST2 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print ("同仁堂 total cost is: " + '%.2f'%COST2)

    print ("同仁堂 net profit is: " + '%.2f'%Profit2)

    

if CHOICE == "3":

    ORI = 18.61 * 500
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input ("电科网安现价?\n")
    COM_SOLD = max (float (PRICE) * 500 * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * 500 * 0.01 / 1000
    STAMP = float (PRICE) * 500 * 0.05 / 100
    Profit1 = float (PRICE) * 500 - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST1 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print ("电科网安 total cost is: " + '%.2f'%COST1)

    print ("电科网安 net profit is: " + '%.2f'%Profit1)


    ORI = 49.1 * 200
    COM_INI = max (ORI * 2.5 / 10000, 5)
    GUOHU_INI = ORI * 0.01 / 1000

    PRICE = input ("同仁堂现价?\n")
    COM_SOLD = max (float (PRICE) * 200 * 2.5 / 10000, 5)
    GUOHU_SOLD = float (PRICE) * 200 * 0.01 / 1000
    STAMP = float (PRICE) * 200 * 0.05 / 100
    Profit2 = float (PRICE) * 200 - ORI - COM_INI - COM_SOLD - GUOHU_INI - GUOHU_SOLD - STAMP

    COST2 = COM_INI + COM_SOLD + GUOHU_INI + GUOHU_SOLD + STAMP
    print ("同仁堂 total cost is: " + '%.2f'%COST2)

    print ("同仁堂 net profit is: " + '%.2f'%Profit2)

    Profit = Profit1 + Profit2

    print("/n")
    print("合计"+ '%.2f'%Profit)