ORI = 18.6 * 500
COM_INI = max (18.6 * 500 * 2.5 / 10000, 5)
PRICE = input ("what is the price now?\n")
COM_SOLD = max (float (PRICE) * 500 * 2.5 / 10000, 5)
Profit = float (PRICE) * 500 - ORI - COM_INI - COM_SOLD
print ("your profit is: ")
print ('%.2f'%Profit)
print ("your initial commission is: ")
print ('%.2f'%COM_INI)
print ("your sold commission is: ")
print ('%.2f'%COM_SOLD)
print ("\n")