

def solve(meal_cost, tip_percent, tax_percent):
    meal_after_tip = (meal_cost / 100) * tip_percent
    meal_after_tax = (meal_cost / 100) * tax_percent

    tax_plus_tip = (meal_after_tax + meal_after_tip)
    total_cost = (meal_cost + tax_plus_tip)
    
    print(round(total_cost))
