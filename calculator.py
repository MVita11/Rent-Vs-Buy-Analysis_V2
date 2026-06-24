def monthly_repayments(principal : float, annual_rate: float, years: int) -> float:    
    r = annual_rate / 12
    n = years * 12
    M = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return M

print(monthly_repayments(225000.00, 0.05, 25))

