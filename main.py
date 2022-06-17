
bill100 = 100
bill50 = 50
bill20 = 20
bill10 = 10
bill5 = 5
bill1 = 1
quarters = .25
dimes = .10
nickels = .05
pennies = .01



totalBill = 159.20

print ("Total billed amount: $%6.2f" % (totalBill))

bills100 = int(input ("Enter number of $100 bills: "))
bills50 = int(input ("Enter number of $50 bills: "))
bills20 = int(input ("Enter number of $20 bills: "))
bills10 = int(input ("Enter number of $10 bills: "))
bills5 = int(input ("Enter number of $5 bills: "))
bills1 = int(input ("Enter number of $1 bills: "))
quarter = int(input ("Enter number of quarters: "))
dime = int(input("Enter number of dimes: "))
nickel = int(input ("Enter number of nickles: "))
penny = int(input ("Enter number of pennies: "))

totalPaidAmt = float((bill100 * bills100) + (bills50 *bill50) + (bills20 * bill20)+ (bills10 * bill10) + (bill5 * bills5) + (bills1* bill1) + (quarters* quarter)+ (dimes * dime) + (nickels * nickel) + (penny * pennies))


print ("Total paid amount: $%6.2f" % (totalPaidAmt))
changeAmt = (totalPaidAmt - totalBill)
print ("Total change: $%.2f" % (changeAmt))