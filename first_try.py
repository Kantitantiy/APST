import math

# Calculate the Economic Order Quantity
def calculate_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

# Suggest order if stock falls below critical level
def check_reorder(stock, critical):
    if stock < critical:
        print("Reorder needed.")
    else:
        print("Stock is OK.")

# Will the supply arrive before the stock reaches zero?
def check_supply_before_delivery(stock, daily_demand, days_until_delivery):
    day = 1
    while day <= days_until_delivery:
        stock -= daily_demand
        print(f"Day {day}: Stock = {stock}")
        day += 1

    if stock <= 0:
        print("Stockout occurred before delivery!")
    else:
        print("Delivery arrived in time.")

# Simulate weekly stock usage
def simulate_weekly_stock_usage(initial_stock, daily_demand, days=7):
    print("\nWeekly Stock Usage Simulation:")
    for day in range(1, days + 1):
        initial_stock -= daily_demand
        if initial_stock < 0:
            print(f"Day {day}: Stockout! No inventory left.")
            break
        else:
            print(f"Day {day}: Remaining Stock = {initial_stock}")

# How many days' supply will the current stock last?
def supply_last_for_days(stock, daily_demand):
    days_covered = stock // daily_demand
    print(f"Current stock is sufficient for {days_covered} full days.")

# How many days' supply can the EOQ meet?
def eoq_lasts_for_days(eoq, daily_demand):
    days_from_eoq = int(eoq) // daily_demand
    print(f"EOQ quantity will meet demand for approximately {days_from_eoq} days.")

# If the stock drops to zero before a new order arrives, on which day will it drop?
def simulate_stock_until_delivery(stock, daily_demand, delivery_days):
    for day in range(1, delivery_days + 1):
        stock -= daily_demand
        if stock <= 0:
            print(f"Stockout occurs on day {day}")
            break
        else:
            print(f"Day {day}: Stock = {stock}")

# Suggest order if stock falls below critical level; Re-evaluate by getting new stock value and critical level from the user.
def check_reorder_user():
    user_stock = int(input("Enter current stock level: "))
    user_critical = int(input("Enter critical level: "))

    if user_stock < user_critical:
        print("Reorder needed.")
    else:
        print("Stock level is sufficient.")

# assuming we always order the EOQ amount and it takes delivery_days to arrive, how frequently should we place orders so that we don’t run out of stock while waiting?


# main
stock = 40
daily_demand = 4
eoq = calculate_eoq(1200, 100, 5)
print("EOQ = ",round(eoq))
check_reorder(stock, 50)
check_supply_before_delivery(stock, daily_demand, 5)
simulate_weekly_stock_usage(stock, daily_demand)
supply_last_for_days(stock, daily_demand)
eoq_lasts_for_days(eoq, daily_demand)
simulate_stock_until_delivery(stock, daily_demand, 5)
check_reorder_user()