def monthly_repayments(principal : float, annual_rate: float, years: int) -> float:    
    r = annual_rate / 12                                        # Monthly interest rate
    n = years * 12                                              # total number of monthly payments
    M = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)     # Fixed monthly payment
    return M

def stamp_duty(purchase_price: float, first_time_buyer: bool = False):
    
    # Normal stamp duty rates
    rates = [
        {"min": 0, "max": 250000, "rate": 0.0},
        {"min": 250000, "max": 925000, "rate": 0.05},
        {"min": 925000, "max": 1500000, "rate": 0.1},
        {"min": 1500000, "max": float('inf'), "rate": 0.12}
    ]

    # First time buyer stamp duty rates
    first_time_buyer_rates = [
        {"min": 0, "max": 300000, "rate": 0.0},
        {"min": 300000, "max": 500000, "rate": 0.05},
    ]
    
    # Checks if buyer is eligible for first time buyer rates
    if first_time_buyer and purchase_price <= 500000:
        applicable_rates = first_time_buyer_rates
    else:
        applicable_rates = rates
        
    # Calculates the total stamp duty based on the applicable rates
    total = 0.0
    for rate in applicable_rates:
        taxable_amount = min(purchase_price, rate["max"]) - rate["min"]
        if taxable_amount > 0:
            total += taxable_amount * rate["rate"]
    return total

