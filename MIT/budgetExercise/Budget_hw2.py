# Homework Problem_Set_2: PROBLEM 1:

def budget_problem2(balance, annualInterestRate):
    """
        Returns the minimum fixed monthly payment needed in order to pay off a credit card balance within 12 months.

        balance: the outstanding balance on the credit card

        annualInterestRate: the annual interest rate as a decimal
    """
    remaining = balance
    payment = 10
    while remaining > 0:
        for month in range(12):
            remaining = (remaining - payment) * (1 + (annualInterestRate/12))
        if remaining <= 0:
            print 'Lowest Payment: ' + str(payment)
        else:
            payment += 10
            remaining = balance
    return payment