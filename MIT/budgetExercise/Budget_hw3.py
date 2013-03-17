# Homework Problem_Set_2: PROBLEM 3:

def budget_problem3(balance, annualInterestRate):
    """
        Uses bisection search to returns the smallest montly payment (to the cent) such that the balance can be paid off within a year.

        balance: the outstanding balance on the credit card

        annualInterestRate: the annual interest rate as a decimal     
    """
    remaining = balance

    # creating the following bounds assists with bisection search
    lo = balance/12
    hi = ((balance * (annualInterestRate/12))**12)/12
    payment = (lo + hi)/2

    while remaining != 0:
        for month in range(12):
            remaining = (remaining - payment) * (1 + (annualInterestRate/12))
        if remaining > 0:
            lo = payment
        elif round(remaining,2) < -0.11:
            hi = payment
        else:
            break
        payment = (lo + hi)/2
        remaining = balance
    print 'Lowest Payment: ' + str(round(payment,2))
    return round(payment,2)