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
def check_future_stock_level(stock_level, daily_demand, days_until_delivery):
    day = 1
    while day <= days_until_delivery:
        day = day + 1
        stock_level = stock_level - daily_demand
        if stock_level <= 0:
            print("Warning: Stock below critical level. Reorder required.")
            print(f"We have stock only for {day-1} days.")
            break

    print("Stock level is ", stock_level, " at end of ", day, " days.")
    if stock_level >= 0:
        print("Stock is OK.")
    else:
        print("Stock is NOT OK.")

def simulate_weekly_stock_usage(initial_stock, daily_demand, days=7):
    stock_level = initial_stock
    for day in range(days):
        stock_level -= daily_demand
        # stock_level =  daily_demand - stock_level
        print(f"{day+1} Stock level is {stock_level}")
        if stock_level < daily_demand:
            print("Warning: Stock below critical level. Reorder required.")
            break

def for_how_many_day_does_the_stock_level_support(initial_stock, daily_demand):
    return initial_stock // daily_demand

# Main Part
value = EQO(D, S, H)
print("EOQ=", round(value))
#check_supply(40, 50)
#check_future_stock_level(60, 3, 16)
#simulate_weekly_stock_usage(65, 12)
days = for_how_many_day_does_the_stock_level_support(value, 13)
print(days)
print(60/13)


current_stock = int(input("Enter the stock level: "))
critical_level=int(input("Enter the critical level: "))
check_supply(current_stock, critical_level)

