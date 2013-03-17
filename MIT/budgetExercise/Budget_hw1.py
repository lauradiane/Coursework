# Homework Problem_Set_2: PROBLEM 1:

def budget_problem1(balance, annualInterestRate, monthlyPaymentRate=0.01):

    """
        Returns (and prints) the credit card balance after one year of minimum monthly payments. 

        balance: the outstanding balance on the credit card 

        annualInterestRate: the annual interest rate as a decimal

        monthlyPaymentRate: the minimum monthly payment rate as a decimal
    """

    total_paid = 0
    for month in range(12):
        min_payment = balance * monthlyPaymentRate
        rem_bal = (balance - min_payment) * (1 + (annualInterestRate/12))
        balance = rem_bal
        total_paid += min_payment
        print 'Month: ' + str(month+1)
        print 'Minimum monthly payment: ' + str(round(min_payment,2))
        print 'Remaining balance:' + str(round(rem_bal,2))
    print 'Total paid: ' + str(round(total_paid,2))
    print 'Remaining balance: ' + str(round(rem_bal,2))
    return round(rem_bal,2)