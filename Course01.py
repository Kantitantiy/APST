import math

D = 1200
S = 100
H = 5

def EQO(D, S, H):
    eoq=math.sqrt((2*D*S)/H)
    return eoq

def check_supply(current_stock, critical_level):
    if current_stock < critical_level:
        print("Warning: Stock below critical level. Reorder required.")
    else:
        print("Stock level is sufficient.")

# Check Future stock level
stock = 10
daily_demand = 4
days_until_delivery = 3

day = 1
while day <= days_until_delivery:
    day = day + 1
    stock = stock - daily_demand

print("Stock level is ", stock)
if stock >= 0:
    print("Stock is OK.")
else:
    print("Stock is NOT OK.")

# Main Part
value = EQO(D, S, H)
print("EOQ=", round(value))

check_supply(40, 50)